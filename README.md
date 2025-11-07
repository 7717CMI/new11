# Customer Intelligence Dashboard - TypeScript/Next.js

A professional, industrial-level customer intelligence dashboard built with Next.js 14, TypeScript, React, and Plotly.js for visualizing customer optimization opportunities across cloud platforms and enterprise licenses.

![Dashboard Preview](https://img.shields.io/badge/Status-Ready-brightgreen) ![Next.js](https://img.shields.io/badge/Next.js-14-black) ![TypeScript](https://img.shields.io/badge/TypeScript-5.3-blue) ![Plotly](https://img.shields.io/badge/Plotly-2.29-orange)

## Features

### 📊 Comprehensive Visualizations
- **KPI Cards**: Real-time metrics for total customers, optimization potential, and opportunities
- **Interactive Charts**: Bar charts, pie charts, scatter plots, grouped and stacked visualizations using Plotly.js
- **Data Tables**: Sortable, filterable customer data with detailed information
- **Advanced Analytics**: Deep-dive analysis with license breakdowns, regional insights, and trigger events

### 🎯 Multi-Dimensional Filtering
- Filter by Industry Vertical
- Filter by Cloud Platform (Azure, AWS, GCP, Multi-cloud)
- Filter by Geographic Region
- Filter by Optimization Type (Cloud FinOps, ELO, Both)
- Filter by License Ecosystem (Microsoft, SAP, Oracle, IBM)
- Filter by Optimization Potential range

### 📱 Responsive Design
- Mobile-friendly layout with collapsible navigation
- Professional industrial color scheme
- Smooth animations and transitions
- Tailwind CSS for modern styling

### 💾 Data Export
- Export filtered customer data to CSV
- Download functionality on Customer Details page

### 🏢 Industrial-Level Features
- **COHERENT MARKET INSIGHTS** branding in top-left corner
- Standard industrial color palette
- Professional chart styling matching original design
- Type-safe TypeScript implementation
- Server-side rendering with Next.js 14 App Router

## Dashboard Pages

### 1. Overview Dashboard
- Total customer count and average optimization potential
- Industry distribution analysis
- Cloud platform usage breakdown
- Optimization type distribution
- Customer-level optimization scatter plot

### 2. Customer Details
- Interactive data table with all customer information
- Sortable and filterable columns
- Detailed customer cards with:
  - Company overview and location
  - Technical infrastructure details
  - Optimization potential metrics
  - Contact information
  - Business context (pain points, triggers, stakeholders)

### 3. Analytics Deep-Dive
- License ecosystem usage analysis
- Regional optimization potential comparison
- Cloud vs ELO optimization breakdown by industry
- Decision maker distribution
- Top trigger events
- Key insights and statistics

## Installation

### Prerequisites
- Node.js 18+ 
- npm or yarn

### Setup Instructions

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Ensure data file exists:**
   The CSV data file should be located at `public/data/customers.csv`. If it doesn't exist, the app will handle it gracefully.

3. **Run the development server:**
   ```bash
   npm run dev
   ```

4. **Open your browser:**
   Navigate to [http://localhost:3000](http://localhost:3000)

## Deployment to Vercel (Serverless)

This application is fully optimized for serverless deployment on Vercel. No server configuration needed!

### Quick Deploy

**Option 1: GitHub Integration (Recommended)**
1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com) and sign in
3. Click "New Project" → Import your repository
4. Vercel auto-detects Next.js configuration
5. Click "Deploy" (takes ~2 minutes)

**Option 2: Vercel CLI**
```bash
npm i -g vercel
vercel
vercel --prod  # For production
```

### Serverless Features

- ✅ **Zero Configuration** - Works out of the box
- ✅ **Auto-scaling** - Handles traffic spikes automatically
- ✅ **Global CDN** - Fast loading worldwide
- ✅ **Free Tier** - Generous free tier for most use cases
- ✅ **Instant Deploys** - Deploy in seconds

See [VERCEL_DEPLOYMENT.md](./VERCEL_DEPLOYMENT.md) for detailed deployment guide.

## Project Structure

```
customer-intelligence-dashboard/
├── app/
│   ├── layout.tsx              # Root layout with branding
│   ├── page.tsx                 # Overview dashboard page
│   ├── customers/
│   │   └── page.tsx            # Customer details page
│   ├── analytics/
│   │   └── page.tsx            # Analytics deep-dive page
│   └── globals.css              # Global styles
├── components/
│   ├── charts.tsx              # Plotly.js chart components
│   ├── filters.tsx             # Filter components
│   └── sidebar.tsx              # Navigation sidebar
├── lib/
│   ├── types.ts                # TypeScript interfaces
│   ├── utils.ts                # Data loading and filtering utilities
│   └── cn.ts                   # Utility functions
├── public/
│   └── data/
│       └── customers.csv       # Customer data file
├── package.json
├── tsconfig.json
├── tailwind.config.ts
└── next.config.js
```

## Technologies Used

- **[Next.js 14](https://nextjs.org/)** - React framework with App Router
- **[TypeScript](https://www.typescriptlang.org/)** - Type-safe JavaScript
- **[Plotly.js](https://plotly.com/javascript/)** - Interactive visualizations
- **[Tailwind CSS](https://tailwindcss.com/)** - Utility-first CSS framework
- **[PapaParse](https://www.papaparse.com/)** - CSV parsing
- **Bootstrap Icons** - Icon library

## Development

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint
- `npm run type-check` - Run TypeScript type checking

### Color Palette

The dashboard uses a standard industrial color palette:

- **Primary**: `#2E86AB` (Professional Blue)
- **Secondary**: `#A23B72` (Deep Magenta)
- **Success**: `#06A77D` (Emerald Green)
- **Warning**: `#F18F01` (Warm Orange)
- **Danger**: `#C73E1D` (Brick Red)
- **Info**: `#6A4C93` (Royal Purple)

## Data Schema

The dashboard uses the following customer data fields:

| Field | Description |
|-------|-------------|
| Sr_No | Serial number |
| Customer_Name | Company name |
| Overview | Business description |
| Geographical_Presence | HQ location and operating regions |
| Product_Offering | Business segments and offerings |
| Industry_Vertical | Industry classification |
| Cloud_Platforms | Cloud infrastructure used |
| License_Ecosystem | Software licenses (MS/Oracle/SAP/IBM) |
| Optimization_Type | Cloud, ELO, or Both |
| Pain_Points | Customer challenges |
| Trigger_Event | Recent activity or catalyst |
| Key_Stakeholders | Relevant contacts |
| Cloud_Optimization_Potential | Cloud optimization % |
| ELO_Optimization_Potential | License optimization % |
| Total_Optimization_Potential | Combined optimization % |
| Decision_Maker | Primary decision maker role |
| Phone | Contact phone |
| Fax | Contact fax |
| Email | Contact email |
| Website | Company website |
| ... | Additional quantitative metrics |

## Customization

### Adding Your Own Data

1. Prepare a CSV file with the schema above
2. Save it as `public/data/customers.csv`
3. Restart the development server

### Modifying Colors

Edit the color palette in `lib/types.ts` and `tailwind.config.ts`:

```typescript
export const COLORS = {
  primary: '#2E86AB',
  // ... add more colors
}
```

### Adding New Charts

1. Create new chart functions in `components/charts.tsx`
2. Import and use them in any page component
3. Charts use Plotly.js for consistency with original design

## Performance Tips

- For large datasets (>1000 customers), consider implementing pagination
- Use server-side filtering for datasets with >5000 records
- Enable Next.js caching for expensive computations
- Consider using React Server Components for data fetching

## Migration Notes

This TypeScript/Next.js version maintains:
- ✅ Same chart styling and appearance as Python/Dash version
- ✅ All filtering functionality
- ✅ All visualization types
- ✅ Same color scheme and industrial design
- ✅ **COHERENT MARKET INSIGHTS** branding in top-left corner

## License

This project is provided as-is for use in customer intelligence and optimization analysis.

---

**Built with ❤️ using Next.js, TypeScript, React, and Plotly.js**

**COHERENT MARKET INSIGHTS**
