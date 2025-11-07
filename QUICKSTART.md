# Quick Start Guide

Get your Customer Intelligence Dashboard running in 3 easy steps!

## Step 1: Install Dependencies

```bash
cd customer-intelligence-dashboard
pip install -r requirements.txt
```

## Step 2: Run the Dashboard

```bash
python app.py
```

## Step 3: Open in Browser

Navigate to: **http://127.0.0.1:8050**

---

## What You'll See

### 📊 Overview Dashboard (Default)
- 4 KPI cards showing key metrics
- Industry distribution bar chart
- Cloud platform pie chart
- Optimization type distribution
- Customer optimization scatter plot

### 👥 Customer Details
- Interactive data table with all customers
- Click on any row to see detailed customer information
- Export filtered data to CSV

### 📈 Analytics Deep-Dive
- License ecosystem breakdown
- Regional optimization analysis
- Cloud vs ELO comparison by industry
- Decision maker distribution
- Trigger events analysis
- Key insights summary

---

## Using Filters

### Left Sidebar (Desktop)
1. Select filter criteria (industry, cloud platform, region, etc.)
2. All charts update automatically
3. Click "Reset Filters" to clear selections

### Sample Filters to Try
- **Filter by Industry**: Select "Food & Beverage" to see beverage companies
- **Filter by Cloud**: Select "Microsoft Azure" to see Azure customers
- **Filter by Optimization**: Adjust slider to show customers with 20%+ potential

---

## Exporting Data

1. Go to **Customer Details** page
2. Apply filters (optional)
3. Click **"Export to CSV"** button
4. File saves as `customer_intelligence_export.csv`

---

## Sample Data

The dashboard comes with **30 pre-generated sample customers** including:
- Coca-Cola Bottling Company
- PepsiCo Inc.
- Halliburton Company
- Kennametal Inc.
- And 26 more Fortune 500 companies

Data includes:
- ✅ Customer overview and details
- ✅ Cloud platforms (Azure, AWS, GCP)
- ✅ License ecosystems (MS, SAP, Oracle, IBM)
- ✅ Optimization potential (Cloud + ELO)
- ✅ Contact information
- ✅ Pain points and trigger events

---

## Tips

💡 **Mobile Friendly**: Access from any device - responsive design adjusts automatically

💡 **Real-time Updates**: Filters update all visualizations instantly

💡 **Interactive Charts**: Hover over any chart element for detailed information

💡 **Multi-Select**: Select multiple filter values at once

---

## Troubleshooting

### Can't access the dashboard?
- Make sure Python is installed: `python --version`
- Check that dependencies are installed: `pip list`
- Try a different port: Edit `app.py` and change `port=8050` to `port=8051`

### No data showing?
- The app will auto-generate sample data on first run
- Check that `data/customers.csv` exists
- Verify filters aren't excluding all customers

---

## Next Steps

1. ✅ Explore all three dashboard pages
2. ✅ Try different filter combinations
3. ✅ Click on customers in the table to see details
4. ✅ Export data to CSV
5. ✅ Customize with your own customer data

---

**Need help?** Check the full [README.md](README.md) for detailed documentation.

Enjoy your Customer Intelligence Dashboard! 🚀
