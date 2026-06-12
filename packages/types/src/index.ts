// Shared types for the Ara platform

// ─── Identity ────────────────────────────────────────────────────────────────

export type UserId = string & { readonly __brand: 'UserId' };

export interface User {
  id: UserId;
  email: string;
  name: string;
  avatarUrl?: string;
  createdAt: string; // ISO 8601
  updatedAt: string; // ISO 8601
}

// ─── API primitives ───────────────────────────────────────────────────────────

export interface ApiResponse<T> {
  data: T;
  success: true;
  timestamp: string; // ISO 8601
}

export interface ApiError {
  success: false;
  error: {
    code: string;
    message: string;
    details?: Record<string, unknown>;
  };
  timestamp: string;
}

export type ApiResult<T> = ApiResponse<T> | ApiError;

// ─── Pagination ───────────────────────────────────────────────────────────────

export interface PaginationMeta {
  page: number;
  pageSize: number;
  totalItems: number;
  totalPages: number;
  hasNextPage: boolean;
  hasPrevPage: boolean;
}

export interface PaginatedResult<T> {
  items: T[];
  pagination: PaginationMeta;
}

// ─── Utilities ────────────────────────────────────────────────────────────────

/** Make all properties of T (recursively) readonly */
export type DeepReadonly<T> = {
  readonly [K in keyof T]: T[K] extends object ? DeepReadonly<T[K]> : T[K];
};

/** Narrow a union to only the members that satisfy a constraint */
export type Satisfies<T, U extends T> = U;
