# Vercel Deployment Guide

This Next.js application is fully optimized for serverless deployment on Vercel.

## Quick Deploy to Vercel

### Option 1: Deploy via Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Deploy to production
vercel --prod
```

### Option 2: Deploy via GitHub Integration

1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Click "New Project"
4. Import your GitHub repository
5. Vercel will automatically detect Next.js and configure everything
6. Click "Deploy"

## Environment Variables

No environment variables are required for basic functionality. The application:
- Loads data from `/public/data/customers.csv` (static file)
- Uses client-side rendering for all pages
- Works completely serverless

### Optional Environment Variables

If you want to customize the base URL:

```env
NEXT_PUBLIC_BASE_URL=https://your-domain.com
```

## Serverless Architecture

This application is fully serverless:

- ✅ **No API Routes** - All data loading happens client-side
- ✅ **Static Assets** - CSV data served from `/public` folder
- ✅ **Client Components** - All pages use `'use client'` directive
- ✅ **Edge-Compatible** - No Node.js-specific dependencies
- ✅ **Optimized Build** - Uses Next.js standalone output

## Performance Optimizations

- **Data Caching**: Customer data is cached after first load
- **Static Generation**: All pages are client-side rendered
- **CDN Caching**: CSV file cached for 1 hour with stale-while-revalidate
- **Code Splitting**: Automatic code splitting by Next.js
- **Tree Shaking**: Unused code automatically removed

## Build Configuration

The `vercel.json` file configures:
- Build command: `npm run build`
- Framework detection: Next.js
- Function timeout: 10 seconds (more than enough for static pages)
- Region: `iad1` (US East)

## Monitoring

After deployment, you can monitor:
- Function execution times
- Error rates
- Traffic analytics
- Performance metrics

All available in your Vercel dashboard.

## Troubleshooting

### Build Fails

1. Check Node.js version (should be 18+)
2. Ensure all dependencies are in `package.json`
3. Check build logs in Vercel dashboard

### Data Not Loading

1. Verify `public/data/customers.csv` exists
2. Check browser console for errors
3. Verify file is committed to Git (Vercel needs it)

### Slow Performance

1. Check Vercel analytics for function execution times
2. Consider enabling Vercel Edge Caching
3. Optimize CSV file size if very large

## Cost

Vercel's free tier includes:
- 100GB bandwidth
- 100 hours of serverless function execution
- Unlimited deployments

This application uses minimal resources and fits comfortably in the free tier.

