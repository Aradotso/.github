import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
  display: 'swap',
})

export const metadata: Metadata = {
  title: 'Ara – Agent-Building Agent',
  description: '✨ Build, run, and refine automated agents on your Mac.',
  keywords: ['agents', 'automation', 'mac', 'AI', 'ara'],
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en" className={inter.variable}>
      <body className="min-h-screen bg-gradient-to-br from-pink-50 via-rose-50 to-fuchsia-50 font-sans antialiased">
        {children}
      </body>
    </html>
  )
}
