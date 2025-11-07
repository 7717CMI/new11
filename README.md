# Customer Intelligence Dashboard

A professional, interactive dashboard built with Python, Plotly, and Dash for visualizing customer optimization opportunities across cloud platforms and enterprise licenses.

![Dashboard Preview](https://img.shields.io/badge/Status-Ready-brightgreen) ![Python](https://img.shields.io/badge/Python-3.9+-blue) ![Dash](https://img.shields.io/badge/Dash-2.14+-orange)

## Features

### 📊 Comprehensive Visualizations
- **KPI Cards**: Real-time metrics for total customers, optimization potential, and opportunities
- **Interactive Charts**: Bar charts, pie charts, scatter plots, grouped and stacked visualizations
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
- Mobile-friendly layout
- Collapsible sidebar navigation
- Professional color scheme with standard business colors
- Smooth animations and transitions

### 💾 Data Export
- Export filtered customer data to CSV
- Download functionality on Customer Details page

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
- Python 3.9 or higher
- pip package manager

### Setup Instructions

1. **Navigate to the project directory:**
   ```bash
   cd customer-intelligence-dashboard
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Generate sample data (optional - will auto-generate on first run):**
   ```bash
   cd data
   python data_generator.py
   cd ..
   ```

## Usage

### Running the Dashboard

1. **Start the application:**
   ```bash
   python app.py
   ```

2. **Open your web browser and navigate to:**
   ```
   http://127.0.0.1:8050
   ```

3. **The dashboard will automatically:**
   - Load customer data from `data/customers.csv`
   - Generate 30 sample customers if no data file exists
   - Display the Overview Dashboard by default

### Navigation

- **Sidebar Navigation** (desktop): Click on any page link in the left sidebar
- **Top Navbar** (mobile): Use the hamburger menu to access pages
- **Filters**: Use the filter section in the sidebar to narrow down customer data
- **Reset Filters**: Click the "Reset Filters" button to clear all filters

### Using Filters

1. Select one or more options from any dropdown filter
2. Adjust the optimization potential slider to set a range
3. All visualizations update automatically
4. Click "Reset Filters" to return to the full dataset

### Exporting Data

1. Navigate to the **Customer Details** page
2. Apply any desired filters
3. Click the **"Export to CSV"** button
4. The filtered data will download as `customer_intelligence_export.csv`

## Project Structure

```
customer-intelligence-dashboard/
├── app.py                          # Main application file
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── assets/
│   └── styles.css                 # Custom CSS styling
│
├── components/
│   ├── sidebar.py                 # Navigation sidebar component
│   ├── filters.py                 # Multi-select filter components
│   └── charts.py                  # Reusable Plotly chart functions
│
├── data/
│   ├── customers.csv              # Customer data (auto-generated)
│   └── data_generator.py          # Sample data generator script
│
└── pages/
    ├── overview.py                # Overview dashboard page
    ├── customer_details.py        # Customer details page with table
    └── analytics.py               # Analytics deep-dive page
```

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

## Customization

### Adding Your Own Data

1. Prepare a CSV file with the schema above
2. Save it as `data/customers.csv`
3. Restart the application

### Modifying Colors

Edit the color palette in `components/charts.py`:

```python
COLORS = {
    'primary': '#2E86AB',      # Professional Blue
    'secondary': '#A23B72',    # Deep Magenta
    'success': '#06A77D',      # Emerald Green
    'warning': '#F18F01',      # Warm Orange
    # ... add more colors
}
```

### Adding New Charts

1. Create new chart functions in `components/charts.py`
2. Import and use them in any page module
3. Add to the page layout with `dcc.Graph()`

## Technologies Used

- **[Dash](https://dash.plotly.com/)** - Web framework for Python
- **[Plotly](https://plotly.com/python/)** - Interactive visualizations
- **[Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)** - Responsive layout components
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation and analysis
- **Bootstrap Icons** - Icon library

## Troubleshooting

### Port Already in Use
If port 8050 is already in use, modify the port in `app.py`:
```python
app.run_server(debug=True, host='127.0.0.1', port=8051)  # Change to 8051 or any available port
```

### Missing Data File
The app will automatically generate sample data if `data/customers.csv` doesn't exist.

### Module Import Errors
Ensure all dependencies are installed:
```bash
pip install -r requirements.txt --upgrade
```

## Performance Tips

- For large datasets (>1000 customers), consider implementing pagination
- Use server-side filtering for datasets with >5000 records
- Enable caching for expensive computations using `@cache.memoize()`

## Future Enhancements

- [ ] User authentication and role-based access
- [ ] Database integration (PostgreSQL, MongoDB)
- [ ] Advanced filtering with saved filter presets
- [ ] PDF report generation
- [ ] Email integration for stakeholder outreach
- [ ] API endpoints for data integration
- [ ] Dark mode theme toggle
- [ ] Interactive map for geographical visualization

## Support

For issues or questions:
1. Check the [Dash documentation](https://dash.plotly.com/)
2. Review the [Plotly documentation](https://plotly.com/python/)
3. Examine the code comments in each module

## License

This project is provided as-is for use in customer intelligence and optimization analysis.

## Acknowledgments

Inspired by modern data visualization best practices and the need for clear, actionable customer intelligence dashboards.

---

**Built with ❤️ using Python, Plotly, and Dash**
