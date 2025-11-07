import dash_bootstrap_components as dbc
from dash import html, dcc

def create_filter_section(df):
    """Create the filter section with HORIZONTAL multi-select dropdowns"""

    # Extract unique values for each filter
    industries = sorted(df['Industry_Vertical'].unique().tolist())
    cloud_platforms = sorted(df['Cloud_Platforms'].unique().tolist())
    regions = sorted(df['Geographical_Presence'].str.extract(r'operates across (.+)$')[0].unique().tolist())
    opt_types = sorted(df['Optimization_Type'].unique().tolist())

    # Extract license ecosystems (split comma-separated values)
    all_licenses = set()
    for licenses in df['License_Ecosystem'].dropna():
        all_licenses.update([lic.strip() for lic in licenses.split(',')])
    license_systems = sorted(list(all_licenses))

    filters = html.Div(
        [
            # Row 1 - Main filters
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Label("Industry Vertical", className="filter-label"),
                            dcc.Dropdown(
                                id='filter-industry',
                                options=[{'label': ind, 'value': ind} for ind in industries],
                                value=[],
                                multi=True,
                                placeholder="Select industries...",
                                className="filter-dropdown",
                                optionHeight=50
                            ),
                        ],
                        md=3, sm=6, xs=12, className="mb-3"
                    ),
                    dbc.Col(
                        [
                            html.Label("Cloud Platform", className="filter-label"),
                            dcc.Dropdown(
                                id='filter-cloud',
                                options=[{'label': cloud, 'value': cloud} for cloud in cloud_platforms],
                                value=[],
                                multi=True,
                                placeholder="Select cloud platforms...",
                                className="filter-dropdown"
                            ),
                        ],
                        md=3, sm=6, xs=12, className="mb-3"
                    ),
                    dbc.Col(
                        [
                            html.Label("Geographic Region", className="filter-label"),
                            dcc.Dropdown(
                                id='filter-region',
                                options=[{'label': region, 'value': region} for region in regions],
                                value=[],
                                multi=True,
                                placeholder="Select regions...",
                                className="filter-dropdown"
                            ),
                        ],
                        md=3, sm=6, xs=12, className="mb-3"
                    ),
                    dbc.Col(
                        [
                            html.Label("Optimization Type", className="filter-label"),
                            dcc.Dropdown(
                                id='filter-optimization',
                                options=[{'label': opt, 'value': opt} for opt in opt_types],
                                value=[],
                                multi=True,
                                placeholder="Select optimization types...",
                                className="filter-dropdown"
                            ),
                        ],
                        md=3, sm=6, xs=12, className="mb-3"
                    ),
                ],
                className="mb-2"
            ),

            # Row 2 - License and range filter
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Label("License Ecosystem", className="filter-label"),
                            dcc.Dropdown(
                                id='filter-license',
                                options=[{'label': lic, 'value': lic} for lic in license_systems],
                                value=[],
                                multi=True,
                                placeholder="Select license systems...",
                                className="filter-dropdown"
                            ),
                        ],
                        md=4, sm=6, xs=12, className="mb-3"
                    ),
                    dbc.Col(
                        [
                            html.Label("Optimization Potential Range (%)", className="filter-label"),
                            dcc.RangeSlider(
                                id='filter-opt-potential',
                                min=0,
                                max=50,
                                step=5,
                                value=[0, 50],
                                marks={i: f'{i}%' for i in range(0, 51, 10)},
                                tooltip={"placement": "bottom", "always_visible": False},
                                className="filter-slider"
                            ),
                        ],
                        md=6, sm=12, xs=12, className="mb-3"
                    ),
                    dbc.Col(
                        [
                            html.Label(html.Br(), className="filter-label"),  # Spacer to align button
                            dbc.Button(
                                [html.I(className="bi bi-arrow-clockwise me-2"), "Reset"],
                                id="reset-filters-btn",
                                color="secondary",
                                size="sm",
                                className="w-100"
                            ),
                        ],
                        md=2, sm=6, xs=12, className="mb-3"
                    ),
                ],
                className="mb-2"
            ),
        ],
        className="filters-container-horizontal p-3 shadow-sm mb-4"
    )

    return filters

def apply_filters(df, industries, clouds, regions, opt_types, licenses, opt_range):
    """Apply all filters to the dataframe"""
    filtered_df = df.copy()

    # Industry filter
    if industries and len(industries) > 0:
        filtered_df = filtered_df[filtered_df['Industry_Vertical'].isin(industries)]

    # Cloud platform filter
    if clouds and len(clouds) > 0:
        filtered_df = filtered_df[filtered_df['Cloud_Platforms'].isin(clouds)]

    # Region filter
    if regions and len(regions) > 0:
        filtered_df = filtered_df[filtered_df['Geographical_Presence'].str.contains('|'.join(regions), case=False, na=False)]

    # Optimization type filter
    if opt_types and len(opt_types) > 0:
        filtered_df = filtered_df[filtered_df['Optimization_Type'].isin(opt_types)]

    # License ecosystem filter (check if any of the selected licenses are in the comma-separated string)
    if licenses and len(licenses) > 0:
        license_pattern = '|'.join(licenses)
        filtered_df = filtered_df[filtered_df['License_Ecosystem'].str.contains(license_pattern, case=False, na=False)]

    # Optimization potential range filter
    if opt_range and len(opt_range) == 2:
        filtered_df = filtered_df[
            (filtered_df['Total_Optimization_Potential'] >= opt_range[0]) &
            (filtered_df['Total_Optimization_Potential'] <= opt_range[1])
        ]

    return filtered_df
