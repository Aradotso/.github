import type { Maybe } from "@ara/types";
import React from "react";

export type ButtonVariant = "primary" | "secondary" | "danger" | "ghost";
export type ButtonSize = "sm" | "md" | "lg";

export interface ButtonProps {
  children: React.ReactNode;
  variant?: ButtonVariant;
  size?: ButtonSize;
  disabled?: Maybe<boolean>;
  onClick?: () => void;
  className?: string;
}

/** Stub Button component — wire up real styles in your app layer. */
export function Button({
  children,
  variant = "primary",
  size = "md",
  disabled,
  onClick,
  className,
}: ButtonProps): React.JSX.Element {
  return (
    <button
      className={["ara-btn", `ara-btn--${variant}`, `ara-btn--${size}`, className]
        .filter(Boolean)
        .join(" ")}
      disabled={disabled ?? false}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
