/** Generic API response wrapper */
export type ApiResponse<T> = {
  data: T;
  status: number;
  ok: boolean;
  message?: string;
};

/** A nullable / undefined-safe type alias */
export type Maybe<T> = T | null | undefined;

/** Core user record */
export type User = {
  id: string;
  email: string;
  name: string;
  createdAt: Date;
  updatedAt: Date;
};

/** Pagination metadata */
export type PaginationMeta = {
  page: number;
  pageSize: number;
  total: number;
  totalPages: number;
};

/** Paginated API response */
export type PaginatedResponse<T> = ApiResponse<T[]> & {
  meta: PaginationMeta;
};

/** Generic record ID type */
export type ID = string;
