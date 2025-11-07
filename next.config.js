/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  // Optimize for Vercel serverless deployment
  // Note: 'standalone' is for self-hosting, Vercel uses its own output
  // output: 'standalone', // Commented out for Vercel deployment
  // Enable static optimization where possible
  experimental: {
    optimizePackageImports: ['plotly.js', 'react-plotly.js'],
  },
  // Headers for better caching
  async headers() {
    return [
      {
        source: '/data/:path*',
        headers: [
          {
            key: 'Cache-Control',
            value: 'public, max-age=3600, stale-while-revalidate=86400',
          },
        ],
      },
    ]
  },
}

module.exports = nextConfig

