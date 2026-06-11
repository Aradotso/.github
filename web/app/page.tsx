import React from 'react'
import { HeroSection } from './components/HeroSection'
import { CapabilityCard } from './components/CapabilityCard'
import { SignupSection } from './components/SignupSection'

// Icons for capability cards
function BuildIcon() {
  return (
    <svg
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.75"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <rect x="3" y="3" width="18" height="18" rx="3" />
      <path d="M9 3v18" />
      <path d="M3 9h6" />
      <path d="M3 15h6" />
      <path d="M14 8l4 4-4 4" />
    </svg>
  )
}

function RunIcon() {
  return (
    <svg
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.75"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="12" cy="12" r="9" />
      <path d="M10 8l6 4-6 4V8z" fill="currentColor" stroke="none" />
    </svg>
  )
}

function MonitorIcon() {
  return (
    <svg
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.75"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <polyline points="22 12 18 12 15 21 9 3 6 12 2 12" />
    </svg>
  )
}

const capabilities = [
  {
    icon: <BuildIcon />,
    title: 'Build Agents',
    description:
      "Design agents visually with Ara's drag-and-drop builder. Connect tools, define goals, and wire up logic -- no boilerplate, just flow.",
    accentColor: 'rgba(255, 45, 120, 0.15)',
  },
  {
    icon: <RunIcon />,
    title: 'Run Workflows',
    description:
      "Orchestrate multi-step workflows with automatic retries, branching, and parallelism. Run locally or deploy to Ara's managed cloud in one click.",
    accentColor: 'rgba(236, 72, 153, 0.15)',
  },
  {
    icon: <MonitorIcon />,
    title: 'Monitor Execution',
    description:
      'See everything your agents do in real time. Full execution traces, step-by-step logs, and alerts when something goes wrong.',
    accentColor: 'rgba(251, 113, 133, 0.15)',
  },
]

export default function HomePage() {
  return (
    <main className="flex flex-col min-h-screen">
      {/* Nav */}
      <nav
        className="fixed top-0 left-0 right-0 z-50 flex items-center justify-between px-8 py-4"
        style={{
          background: 'rgba(10, 10, 10, 0.8)',
          backdropFilter: 'blur(12px)',
          WebkitBackdropFilter: 'blur(12px)',
          borderBottom: '1px solid rgba(255,255,255,0.05)',
        }}
      >
        <span
          className="text-xl font-bold text-white tracking-tight"
          style={{ fontFamily: "'Plus Jakarta Sans', sans-serif" }}
        >
          <span style={{ color: '#FF2D78' }}>A</span>ra
        </span>
        <div className="flex items-center gap-6">
          <a
            href="https://docs.ara.so"
            target="_blank"
            rel="noopener noreferrer"
            className="text-sm text-zinc-400 hover:text-white transition-colors"
          >
            Docs
          </a>
          <a
            href="#signup"
            className="text-sm font-semibold text-white px-4 py-2 rounded-lg transition-all"
            style={{
              background: 'rgba(255, 45, 120, 0.15)',
              border: '1px solid rgba(255, 45, 120, 0.3)',
            }}
          >
            Get access
          </a>
        </div>
      </nav>

      {/* Hero */}
      <HeroSection />

      {/* Capabilities */}
      <section className="px-6 py-20">
        <div className="max-w-5xl mx-auto">
          <div className="text-center mb-14">
            <h2
              className="text-3xl md:text-4xl font-extrabold text-white mb-4"
              style={{ fontFamily: "'Plus Jakarta Sans', sans-serif" }}
            >
              Everything you need to ship agents
            </h2>
            <p className="text-zinc-400 text-base max-w-xl mx-auto">
              Ara covers the full lifecycle -- from design to deployment to observability.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
            {capabilities.map((cap) => (
              <CapabilityCard
                key={cap.title}
                icon={cap.icon}
                title={cap.title}
                description={cap.description}
                accentColor={cap.accentColor}
              />
            ))}
          </div>
        </div>
      </section>

      {/* Divider */}
      <div
        className="mx-auto w-full max-w-5xl px-6"
        style={{
          height: '1px',
          background:
            'linear-gradient(90deg, transparent, rgba(255,255,255,0.06), transparent)',
        }}
      />

      {/* Signup */}
      <SignupSection />

      {/* Footer */}
      <footer
        className="border-t px-8 py-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-sm text-zinc-500"
        style={{ borderColor: 'rgba(255,255,255,0.06)' }}
      >
        <span
          className="font-bold text-base text-white"
          style={{ fontFamily: "'Plus Jakarta Sans', sans-serif" }}
        >
          <span style={{ color: '#FF2D78' }}>A</span>ra
        </span>
        <nav className="flex items-center gap-6">
          <a
            href="https://docs.ara.so"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-white transition-colors"
          >
            Docs
          </a>
          <a href="https://ara.so" className="hover:text-white transition-colors">
            ara.so
          </a>
        </nav>
        <span className="text-xs text-zinc-600">
          &copy; {new Date().getFullYear()} Ara. All rights reserved.
        </span>
      </footer>
    </main>
  )
}
