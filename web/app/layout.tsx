import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Ara — Build, Run, and Monitor AI Agents',
  description:
    'Ara is the platform for building, running, and monitoring AI agents that actually work. ' +
    'Visual agent builder, multi-step workflow orchestration, and real-time execution traces — ' +
    'all in one place.',
  metadataBase: new URL('https://ara.so'),
  openGraph: {
    title: 'Ara — Build, Run, and Monitor AI Agents',
    description:
      'Build, run, and monitor AI agents that actually work. ' +
      'Visual builder, workflow orchestration, real-time traces.',
    url: 'https://ara.so',
    siteName: 'Ara',
    locale: 'en_US',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Ara — Build, Run, and Monitor AI Agents',
    description: 'Build, run, and monitor AI agents that actually work.',
  },
  icons: {
    icon: '/favicon.ico',
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="scroll-smooth">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="bg-[#0A0A0A] text-white antialiased min-h-screen relative">
        <div className="relative z-10">{children}</div>
      </body>
    </html>
  )
}
