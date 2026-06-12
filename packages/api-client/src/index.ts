import type { ApiResult, PaginatedResult } from '@ara/types';

export interface ApiClientConfig {
  baseUrl: string;
  /** Default headers sent with every request */
  headers?: Record<string, string>;
  /** Request timeout in milliseconds (default: 10 000) */
  timeoutMs?: number;
}

/**
 * Lightweight HTTP client for the Ara backend API.
 * Wraps the native `fetch` API and normalises responses into `ApiResult<T>`.
 */
export class ApiClient {
  private readonly baseUrl: string;
  private readonly defaultHeaders: Record<string, string>;
  private readonly timeoutMs: number;

  constructor(config: ApiClientConfig) {
    this.baseUrl = config.baseUrl.replace(/\/$/, '');
    this.defaultHeaders = {
      'Content-Type': 'application/json',
      ...config.headers,
    };
    this.timeoutMs = config.timeoutMs ?? 10_000;
  }

  // ─── Auth helper ──────────────────────────────────────────────────────────

  setAuthToken(token: string): void {
    this.defaultHeaders['Authorization'] = `Bearer ${token}`;
  }

  clearAuthToken(): void {
    delete this.defaultHeaders['Authorization'];
  }

  // ─── Core request ─────────────────────────────────────────────────────────

  private async request<T>(
    method: string,
    path: string,
    body?: unknown,
  ): Promise<ApiResult<T>> {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), this.timeoutMs);

    try {
      const init: RequestInit = {
        method,
        headers: this.defaultHeaders,
        body: body !== undefined ? JSON.stringify(body) : null,
        signal: controller.signal,
      };
      const response = await fetch(`${this.baseUrl}${path}`, init);

      const json: ApiResult<T> = await response.json() as ApiResult<T>;
      return json;
    } catch (err) {
      return {
        success: false,
        error: {
          code: 'NETWORK_ERROR',
          message: err instanceof Error ? err.message : 'Unknown network error',
        },
        timestamp: new Date().toISOString(),
      };
    } finally {
      clearTimeout(timer);
    }
  }

  // ─── Convenience methods ──────────────────────────────────────────────────

  get<T>(path: string): Promise<ApiResult<T>> {
    return this.request<T>('GET', path);
  }

  post<T>(path: string, body: unknown): Promise<ApiResult<T>> {
    return this.request<T>('POST', path, body);
  }

  put<T>(path: string, body: unknown): Promise<ApiResult<T>> {
    return this.request<T>('PUT', path, body);
  }

  patch<T>(path: string, body: unknown): Promise<ApiResult<T>> {
    return this.request<T>('PATCH', path, body);
  }

  delete<T>(path: string): Promise<ApiResult<T>> {
    return this.request<T>('DELETE', path);
  }

  // ─── Paginated helper ──────────────────────────────────────────────────────

  async getPaginated<T>(
    path: string,
    params: { page?: number; pageSize?: number } = {},
  ): Promise<ApiResult<PaginatedResult<T>>> {
    const qs = new URLSearchParams();
    if (params.page !== undefined) qs.set('page', String(params.page));
    if (params.pageSize !== undefined) qs.set('pageSize', String(params.pageSize));
    const query = qs.toString();
    return this.get<PaginatedResult<T>>(query ? `${path}?${query}` : path);
  }
}
