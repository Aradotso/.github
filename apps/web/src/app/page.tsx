import type { User } from '@ara/types';
import { Button } from '@ara/ui';
import { ApiClient } from '@ara/api-client';

// Instantiate the API client (base URL would come from env in a real app)
const apiClient = new ApiClient({ baseUrl: process.env['NEXT_PUBLIC_API_URL'] ?? '/api' });

export default function HomePage() {
  return (
    <main style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>Ara</h1>
      <p>Welcome to the Ara web app.</p>
      <Button onClick={() => console.log('clicked')}>Get started</Button>
    </main>
  );
}
