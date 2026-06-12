import React from 'react';
import { Button, useTheme } from '@ara/ui';
import type { User } from '@ara/types';

const placeholderUser: User = {
  id: 'user_1' as import('@ara/types').UserId,
  email: 'hello@ara.so',
  name: 'Ara User',
  createdAt: new Date().toISOString(),
  updatedAt: new Date().toISOString(),
};

export default function App() {
  const { resolvedScheme } = useTheme();

  return (
    <div
      style={{
        minHeight: '100vh',
        padding: '2rem',
        fontFamily: 'sans-serif',
        background: resolvedScheme === 'dark' ? '#0f0f0f' : '#ffffff',
        color: resolvedScheme === 'dark' ? '#fafafa' : '#0f0f0f',
      }}
    >
      <h1>Ara Mobile</h1>
      <p>Welcome, {placeholderUser.name}.</p>
      <Button variant="primary" onClick={() => alert('Hello from Ara!')}>
        Say hello
      </Button>
    </div>
  );
}
