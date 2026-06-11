'use client'

import React, { useState } from 'react'

export function SignupSection() {
  const [email, setEmail] = useState('')
  const [submitted, setSubmitted] = useState(false)

  function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault()
    if (email.trim()) {
      setSubmitted(true)
    }
  }

  return (
    <section
      id="signup"
      className="relative px-6 py-28 flex flex-col items-center text-center overflow-hidden"
    >
      {/* Section glow */}
      <div
        className="absolute inset-0 pointer-events-none"
        style={{
          background:
            'radial-gradient(ellipse 60% 60% at 50% 50%, rgba(255, 45, 120, 0.08) 0%, transparent 70%)',
        }}
      />

      <div className="relative max-w-xl w-full">
        {/* Heading */}
        <h2
          className="text-4xl md:text-5xl font-extrabold mb-4"
          style={{
            fontFamily: "'Plus Jakarta Sans', sans-serif",
            background: 'linear-gradient(135deg, #f472b6 0%, #ec4899 45%, #fb7185 100%)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            backgroundClip: 'text',
          }}
        >
          Get early access
        </h2>

        <p className="text-zinc-400 mb-10 text-base leading-relaxed">
          Be among the first to build with Ara. We&apos;re onboarding teams in batches — leave your
          email and we&apos;ll reach out when your spot is ready.
        </p>

        {submitted ? (
          <div
            className="flex flex-col items-center gap-3 py-8 px-6 rounded-2xl"
            style={{
              background: 'rgba(255, 45, 120, 0.08)',
              border: '1px solid rgba(255, 45, 120, 0.2)',
            }}
          >
            <svg className="w-10 h-10 text-pink-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
            </svg>
            <p className="text-white font-semibold text-lg">You&apos;re on the list!</p>
            <p className="text-zinc-400 text-sm">We&apos;ll be in touch soon with next steps.</p>
          </div>
        ) : (
          <form
            onSubmit={handleSubmit}
            className="flex flex-col sm:flex-row gap-3 w-full"
            aria-label="Early access signup"
          >
            <input
              type="email"
              required
              placeholder="you@company.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="flex-1 px-4 py-3.5 rounded-xl text-white placeholder-zinc-500 text-sm outline-none focus:ring-2 focus:ring-pink-500/50 transition-all"
              style={{
                background: 'rgba(255, 255, 255, 0.06)',
                border: '1px solid rgba(255, 255, 255, 0.1)',
              }}
            />
            <button
              type="submit"
              className="shrink-0 px-6 py-3.5 rounded-xl text-sm font-semibold text-white transition-all duration-200"
              style={{
                background: 'linear-gradient(135deg, #FF2D78, #EC4899)',
                boxShadow: '0 0 20px rgba(255, 45, 120, 0.35)',
              }}
            >
              Request access
            </button>
          </form>
        )}

        <p className="mt-4 text-zinc-600 text-xs">No spam. No credit card required.</p>
      </div>
    </section>
  )
}
