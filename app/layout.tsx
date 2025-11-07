'use client'

import type { Metadata } from 'next'
import { Sidebar, MobileNavbar } from '@/components/sidebar'
import './globals.css'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <link
          href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css"
          rel="stylesheet"
        />
        <title>Customer Intelligence Dashboard</title>
        <meta name="description" content="Comprehensive view of customer optimization opportunities" />
      </head>
      <body>
        <div className="min-h-screen bg-gray-50">
          {/* Branding with Logo in top left */}
          <div className="logo-container fixed top-0 left-0 z-[60]">
            <img 
              src="/logo.png" 
              alt="COHERENT MARKET INSIGHTS" 
            />
          </div>
          <MobileNavbar />
          <Sidebar />
          <div className="min-h-screen transition-all duration-300 lg:ml-[280px]">
            <div className="p-8 pt-20">
              <div className="mb-6">
                <h1 className="text-center text-3xl font-bold text-blue-600 mb-2 tracking-tight">
                  Customer Database - U.S. Cloud FinOps Market
                </h1>
              </div>
              {children}
            </div>
          </div>
        </div>
      </body>
    </html>
  )
}

