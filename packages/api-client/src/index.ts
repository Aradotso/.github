import type { ApiResponse, Maybe } from "@ara/types";

export interface ClientConfig {
  baseUrl: string;
  headers?: Record<string, string>;
  timeout?: Maybe<number>;
}

export interface AraClient {
  get<T>(path: string): Promise<ApiResponse<T>>;
  post<T>(path: string, body: unknown): Promise<ApiResponse<T>>;
  put<T>(path: string, body: unknown): Promise<ApiResponse<T>>;
  delete<T>(path: string): Promise<ApiResponse<T>>;
}

/** Create a typed fetch client bound to a base URL. */
export function createClient(config: ClientConfig): AraClient {
  const { baseUrl, headers: defaultHeaders = {} } = config;

  async function request<T>(
    method: string,
    path: string,
    body?: unknown,
  ): Promise<ApiResponse<T>> {
    const url = `${baseUrl}${path}`;
    const res = await fetch(url, {
      method,
      headers: {
        "Content-Type": "application/json",
        ...defaultHeaders,
      },
      body: body !== undefined ? JSON.stringify(body) : undefined,
    });

    const data = (await res.json()) as T;
    return { data, status: res.status, ok: res.ok };
  }

  return {
    get: <T>(path: string) => request<T>("GET", path),
    post: <T>(path: string, body: unknown) => request<T>("POST", path, body),
    put: <T>(path: string, body: unknown) => request<T>("PUT", path, body),
    delete: <T>(path: string) => request<T>("DELETE", path),
  };
}
