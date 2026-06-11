import React from 'react'

interface CapabilityCardProps {
  icon: React.ReactNode
  title: string
  description: string
  accentColor?: string
}

export function CapabilityCard({
  icon,
  title,
  description,
  accentColor = 'rgba(255, 45, 120, 0.2)',
}: CapabilityCardProps) {
  return (
    <div
      className="flex flex-col gap-4 p-7 rounded-2xl transition-all duration-300 group"
      style={{
        background: 'rgba(255, 255, 255, 0.04)',
        backdropFilter: 'blur(12px)',
        WebkitBackdropFilter: 'blur(12px)',
        border: '1px solid rgba(255, 255, 255, 0.08)',
        boxShadow: '0 4px 24px rgba(0,0,0,0.2)',
      }}
      onMouseEnter={(e) => {
        ;(e.currentTarget as HTMLDivElement).style.border =
          '1px solid rgba(236, 72, 153, 0.25)'
        ;(e.currentTarget as HTMLDivElement).style.boxShadow =
          '0 4px 32px rgba(0,0,0,0.3), 0 0 20px rgba(255, 45, 120, 0.08)'
      }}
      onMouseLeave={(e) => {
        ;(e.currentTarget as HTMLDivElement).style.border =
          '1px solid rgba(255, 255, 255, 0.08)'
        ;(e.currentTarget as HTMLDivElement).style.boxShadow =
          '0 4px 24px rgba(0,0,0,0.2)'
      }}
    >
      {/* Icon container */}
      <div
        className="w-12 h-12 rounded-xl flex items-center justify-center text-pink-400 flex-shrink-0"
        style={{ background: accentColor }}
      >
        {icon}
      </div>

      {/* Content */}
      <div className="flex flex-col gap-2">
        <h3
          className="text-lg font-semibold text-white"
          style={{ fontFamily: "'Plus Jakarta Sans', sans-serif" }}
        >
          {title}
        </h3>
        <p className="text-sm text-zinc-400 leading-relaxed">{description}</p>
      </div>
    </div>
  )
}
