import type { User } from '@ara/types';
import React from 'react';

// ─── Button component ─────────────────────────────────────────────────────────

export type ButtonVariant = 'primary' | 'secondary' | 'ghost' | 'danger';
export type ButtonSize = 'sm' | 'md' | 'lg';

export interface ButtonProps {
  variant?: ButtonVariant;
  size?: ButtonSize;
  disabled?: boolean;
  loading?: boolean;
  onClick?: () => void;
  children: React.ReactNode;
  className?: string;
}

/**
 * Placeholder Button component.
 * Replace with a real implementation using your UI library of choice.
 */
export function Button({
  variant = 'primary',
  size = 'md',
  disabled = false,
  loading = false,
  onClick,
  children,
  className,
}: ButtonProps): React.ReactElement {
  return React.createElement(
    'button',
    {
      className: [`btn btn--${variant} btn--${size}`, className].filter(Boolean).join(' '),
      disabled: disabled || loading,
      onClick,
      'aria-busy': loading,
    },
    loading ? React.createElement('span', { 'aria-hidden': 'true' }, '\u2026') : null,
    children,
  );
}

// ─── Avatar component ─────────────────────────────────────────────────────────

export interface AvatarProps {
  user: Pick<User, 'name' | 'avatarUrl'>;
  size?: 'sm' | 'md' | 'lg';
}

export function Avatar({ user, size = 'md' }: AvatarProps): React.ReactElement {
  if (user.avatarUrl) {
    return React.createElement('img', {
      src: user.avatarUrl,
      alt: user.name,
      className: `avatar avatar--${size}`,
    });
  }
  const initials = user.name
    .split(' ')
    .map((n) => n[0] ?? '')
    .join('')
    .toUpperCase()
    .slice(0, 2);
  return React.createElement(
    'span',
    { className: `avatar avatar--${size} avatar--initials` },
    initials,
  );
}

// ─── Theme hook ───────────────────────────────────────────────────────────────

export type ColorScheme = 'light' | 'dark' | 'system';

export interface ThemeState {
  colorScheme: ColorScheme;
  resolvedScheme: 'light' | 'dark';
  setColorScheme: (scheme: ColorScheme) => void;
}

/**
 * Placeholder useTheme hook.
 * Wire this up to a real context provider in your app.
 */
export function useTheme(): ThemeState {
  return {
    colorScheme: 'system',
    resolvedScheme:
      typeof window !== 'undefined' && window.matchMedia('(prefers-color-scheme: dark)').matches
        ? 'dark'
        : 'light',
    setColorScheme: (_scheme: ColorScheme) => {
      console.warn('useTheme: setColorScheme is not yet wired up to a provider.');
    },
  };
}
