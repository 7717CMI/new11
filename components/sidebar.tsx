'use client'

import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { useState } from 'react'
import { cn } from '@/lib/cn'

interface SidebarProps {
  isOpen?: boolean
  onToggle?: () => void
}

export function Sidebar({ isOpen = true, onToggle }: SidebarProps) {
  const pathname = usePathname()

  const navItems = [
    { href: '/', label: 'Overview Dashboard', icon: 'bi-house-door' },
    { href: '/customers', label: 'Customer Details', icon: 'bi-people' },
    { href: '/analytics', label: 'Analytics Deep-Dive', icon: 'bi-graph-up' },
  ]

  return (
    <div className="hidden lg:block fixed left-0 top-0 h-screen w-[280px] bg-white border-r border-gray-200 shadow-sm z-50 overflow-y-auto pt-[60px]">
      <div className="p-5">
        <div className="mb-4">
          <h3 className="text-blue-600 text-xl font-bold mb-2">Customer Intelligence</h3>
          <hr className="border-t-2 border-gray-200 my-4" />
        </div>
        <nav className="space-y-1">
          {navItems.map((item) => {
            const isActive = pathname === item.href
            return (
              <Link
                key={item.href}
                href={item.href}
                className={cn(
                  'flex items-center px-4 py-3 rounded-lg transition-all duration-300 text-sm',
                  isActive
                    ? 'bg-blue-600 text-white font-semibold'
                    : 'text-gray-700 hover:bg-blue-50 hover:text-blue-600 hover:translate-x-1'
                )}
              >
                <i className={cn('bi', item.icon, 'mr-2 text-lg')}></i>
                <span>{item.label}</span>
              </Link>
            )
          })}
        </nav>
      </div>
    </div>
  )
}

export function MobileNavbar() {
  const pathname = usePathname()
  const [isOpen, setIsOpen] = useState(false)

  return (
    <nav className="lg:hidden bg-primary text-white shadow-md mb-3">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center">
            <i className="bi bi-speedometer2 mr-2 text-xl"></i>
            <span className="font-bold text-lg">Customer Intelligence Dashboard</span>
          </div>
          <button
            onClick={() => setIsOpen(!isOpen)}
            className="p-2 rounded-md hover:bg-primary/80"
          >
            <i className="bi bi-list text-2xl"></i>
          </button>
        </div>
        {isOpen && (
          <div className="pb-4 space-y-2">
            <Link
              href="/"
              className={cn(
                'block px-4 py-2 rounded hover:bg-primary/80',
                pathname === '/' && 'bg-primary/80'
              )}
            >
              Overview
            </Link>
            <Link
              href="/customers"
              className={cn(
                'block px-4 py-2 rounded hover:bg-primary/80',
                pathname === '/customers' && 'bg-primary/80'
              )}
            >
              Customers
            </Link>
            <Link
              href="/analytics"
              className={cn(
                'block px-4 py-2 rounded hover:bg-primary/80',
                pathname === '/analytics' && 'bg-primary/80'
              )}
            >
              Analytics
            </Link>
          </div>
        )}
      </div>
    </nav>
  )
}

