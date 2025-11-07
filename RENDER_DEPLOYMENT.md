# Render Deployment Configuration

This Next.js application is ready for deployment on Render.

## Quick Deploy

1. Connect your GitHub repository to Render
2. Render will automatically detect the `render.yaml` file
3. The service will be configured automatically

## Manual Configuration (if needed)

If you prefer to configure manually:

- **Build Command**: `npm install && npm run build`
- **Start Command**: `npm start`
- **Environment**: Node.js
- **Node Version**: 18.x or higher

## Environment Variables

No environment variables are required for basic functionality. The application uses static CSV data from `/public/data/customers.csv`.

## Build & Deploy

The application will:
1. Install dependencies (`npm install`)
2. Build the Next.js application (`npm run build`)
3. Start the production server (`npm start`)

## Health Check

The health check path is set to `/` (root).

## Notes

- The application is fully serverless-ready
- All data is loaded client-side from static CSV files
- No database or external API dependencies required
- Static assets are served from `/public` directory
