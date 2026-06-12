export default function HomePage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center px-6 py-24">
      {/* Logo / wordmark */}
      <div className="mb-8 flex flex-col items-center gap-4">
        <div className="flex h-20 w-20 items-center justify-center rounded-3xl bg-gradient-to-br from-pink-400 to-fuchsia-500 shadow-lg shadow-pink-300/50">
          <span className="text-4xl font-black tracking-tighter text-white">A</span>
        </div>
        <h1 className="bg-gradient-to-r from-pink-500 via-fuchsia-500 to-rose-400 bg-clip-text text-6xl font-black tracking-tight text-transparent">
          Ara
        </h1>
      </div>

      {/* Tagline */}
      <p className="mb-10 max-w-lg text-center text-lg text-rose-700/80">
        ✨ The agent-building agent. Build, run, and refine automated agents on your Mac.
      </p>

      {/* CTA */}
      <div className="flex flex-col items-center gap-4 sm:flex-row">
        <a
          href="/agents"
          className="rounded-2xl bg-gradient-to-r from-pink-500 to-fuchsia-500 px-8 py-3 text-base font-semibold text-white shadow-md shadow-pink-400/40 transition-all hover:scale-105 hover:shadow-lg hover:shadow-pink-400/50 focus:outline-none focus:ring-2 focus:ring-pink-400 focus:ring-offset-2"
        >
          🌸 Get Started
        </a>
        <a
          href="https://github.com/Aradotso/ara-cua"
          target="_blank"
          rel="noopener noreferrer"
          className="rounded-2xl border-2 border-pink-300 bg-white/60 px-8 py-3 text-base font-semibold text-pink-600 backdrop-blur-sm transition-all hover:scale-105 hover:border-pink-400 hover:bg-white/80 focus:outline-none focus:ring-2 focus:ring-pink-300 focus:ring-offset-2"
        >
          ✦ View on GitHub
        </a>
      </div>

      {/* Decorative blobs */}
      <div
        aria-hidden="true"
        className="pointer-events-none fixed left-0 top-0 -z-10 h-72 w-72 -translate-x-1/2 -translate-y-1/2 rounded-full bg-pink-300/30 blur-3xl"
      />
      <div
        aria-hidden="true"
        className="pointer-events-none fixed bottom-0 right-0 -z-10 h-96 w-96 translate-x-1/3 translate-y-1/3 rounded-full bg-fuchsia-300/30 blur-3xl"
      />
    </main>
  )
}
