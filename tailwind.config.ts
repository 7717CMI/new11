import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#2563EB',      // Standard Blue
        secondary: '#1E40AF',     // Darker Blue
        success: '#10B981',       // Green
        warning: '#F59E0B',       // Orange
        danger: '#EF4444',        // Red
        info: '#3B82F6',         // Light Blue
        accent1: '#60A5FA',       // Light Blue
        accent2: '#93C5FD',       // Lighter Blue
        accent3: '#DBEAFE',       // Very Light Blue
        accent4: '#EFF6FF',       // Lightest Blue
        neutral: '#6B7280',       // Gray
        light: '#F9FAFB',         // Light Gray
        dark: '#111827',          // Dark Gray
      },
      fontFamily: {
        sans: ['Arial', 'Helvetica', 'sans-serif'],
      },
      animation: {
        'fade-in': 'fadeIn 0.6s ease-in-out',
        'slide-up': 'slideUp 0.6s ease-out',
        'slide-in': 'slideIn 0.5s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        slideIn: {
          '0%': { transform: 'translateX(-20px)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' },
        },
      },
    },
  },
  plugins: [],
}
export default config

