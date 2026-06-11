'use client'

import React from 'react'

// Aeroplane SVG icon for hero motif
function AeroplaneIcon({ className }: { className?: string }) {
  return (
    <svg
      className={className}
      viewBox="0 0 24 24"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      aria-hidden="true"
    >
      <path
        d="M21.5 2.5L2.5 10.5L9.5 13.5L12.5 21.5L21.5 2.5Z"
        stroke="currentColor"
        strokeWidth="1.5"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
      <path
        d="M9.5 13.5L14.5 8.5"
        stroke="currentColor"
        strokeWidth="1.5"
        strokeLinecap="round"
      />
    </svg>
  )
}

export function HeroSection() {
  return (
    <section className="relative flex flex-col items-center justify-center min-h-screen px-6 pt-20 pb-24 text-center overflow-hidden">
      {/* Background glow */}
      <div
        className="absolute inset-0 pointer-events-none"
        style={{
          background:
            'radial-gradient(ellipse 70% 50% at 50% 0%, rgba(255, 45, 120, 0.18) 0%, transparent 70%)',
        }}
      />

      {/* Aeroplane icon — top right decoration */}
      <div className="absolute top-8 right-12 opacity-20 rotate-45">
        <AeroplaneIcon className="w-12 h-12 text-pink-400" />
      </div>
      {/* Aeroplane icon — bottom left decoration */}
      <div className="absolute bottom-20 left-10 opacity-10 -rotate-12">
        <AeroplaneIcon className="w-8 h-8 text-rose-400" />
      </div>

      {/* Pill badge */}
      <div className="inline-flex items-center gap-2 mb-6 px-4 py-1.5 rounded-full bg-white/5 border border-white/10 text-sm text-pink-300 font-medium backdrop-blur-sm">
        <AeroplaneIcon className="w-4 h-4 text-pink-400" />
        Now in early access
      </div>

      {/* Main headline */}
      <h1
        className="text-5xl md:text-7xl font-extrabold tracking-tight mb-6 max-w-4xl leading-[1.08]"
        style={{ fontFamily: "'Plus Jakarta Sans', sans-serif" }}
      >
        Build agents that{' '}
        <span
          style={{
            background: 'linear-gradient(135deg, #f472b6 0%, #ec4899 45%, #fb7185 100%)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            backgroundClip: 'text',
          }}
        >
          actually work
        </span>
      </h1>

      {/* Subheadline */}
      <p className="text-lg md:text-xl text-zinc-400 max-w-2xl mb-10 leading-relaxed">
        Ara is the all-in-one platform for building, running, and monitoring AI agents.
        From visual workflow design to real-time execution traces — ship agents with confidence.
      </p>

      {/* CTA */}
      <a
        href="#signup"
        className="btn-pink text-base px-8 py-3.5 inline-flex items-center gap-2 no-underline"
        style={{
          background: 'linear-gradient(135deg, #FF2D78, #EC4899)',
          color: '#fff',
          fontWeight: 600,
          borderRadius: '0.625rem',
          padding: '0.875rem 2rem',
          display: 'inline-flex',
          alignItems: 'center',
          gap: '0.5rem',
          boxShadow: '0 0 24px rgba(255, 45, 120, 0.4)',
          transition: 'all 0.2s ease',
          textDecoration: 'none',
          fontSize: '1rem',
        }}
      >
        <AeroplaneIcon className="w-4 h-4" />
        Join Early Access
      </a>

      {/* Demo video placeholder */}
      <div
        className="relative mt-16 w-full max-w-4xl rounded-2xl overflow-hidden"
        style={{
          background: '#111111',
          border: '1px solid rgba(236, 72, 153, 0.3)',
          boxShadow:
            '0 0 0 1px rgba(255, 45, 120, 0.08), 0 0 60px rgba(236, 72, 153, 0.15), 0 32px 64px rgba(0,0,0,0.5)',
        }}
      >
        {/* Window chrome */}
        <div className="flex items-center gap-2 px-4 py-3 border-b border-white/5">
          <span className="w-3 h-3 rounded-full bg-red-500/70" />
          <span className="w-3 h-3 rounded-full bg-yellow-500/70" />
          <span className="w-3 h-3 rounded-full bg-green-500/70" />
          <span className="ml-3 text-xs text-zinc-500 font-mono">ara.so — agent playground</span>
        </div>
        {/* 16:9 video area */}
        <div
          className="relative w-full"
          style={{ paddingBottom: '56.25%' /* 16:9 */ }}
        >
          <div className="absolute inset-0 flex flex-col items-center justify-center gap-3">
            <div
              className="w-14 h-14 rounded-full flex items-center justify-center"
              style={{
                background: 'rgba(255, 45, 120, 0.15)',
                border: '1px solid rgba(255, 45, 120, 0.3)',
              }}
            >
              <svg className="w-6 h-6 text-pink-400 ml-0.5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M8 5v14l11-7z" />
              </svg>
            </div>
            <span className="text-zinc-500 text-sm font-medium tracking-wide">Agent demo video</span>
            <span className="text-zinc-700 text-xs">Coming soon</span>
          </div>
        </div>
      </div>
    </section>
  )
}
