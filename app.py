import dash
from dash import Dash, html, dcc, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
import pandas as pd
import os

# Import components and pages
from components.sidebar import create_sidebar, create_navbar
from components.filters import create_filter_section, apply_filters
from pages.overview import create_overview_layout
from pages.customer_details import create_customer_details_layout, create_customer_detail_card
from pages.analytics import create_analytics_layout

# Initialize the Dash app
app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css'
    ],
    suppress_callback_exceptions=True,
    title="Customer Intelligence Dashboard"
)

# Configure server for better performance
server = app.server
server.config['TIMEOUT'] = 300  # 5 minutes timeout

# Load data
data_path = os.path.join('data', 'customers.csv')
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
else:
    # Generate sample data if CSV doesn't exist
    print("Generating sample data...")
    from data.data_generator import generate_customer_data
    df = generate_customer_data(30)
    os.makedirs('data', exist_ok=True)
    df.to_csv(data_path, index=False)
    print(f"Sample data saved to {data_path}")

# Store original data
original_df = df.copy()

# Define the app layout - HORIZONTAL FILTERS
app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        dcc.Store(id='filtered-data-store', data=df.to_dict('records')),

        # Navbar for mobile
        html.Div(
            create_navbar(),
            className="d-lg-none"
        ),

        # Main container with sidebar + content
        html.Div(
            [
                # Sidebar (navigation only, no filters)
                html.Div(
                    [
                        create_sidebar(),
                    ],
                    className="sidebar-container d-none d-lg-block",
                ),

                # Main content area
                html.Div(
                    [
                        # Main heading at the top
                        html.Div(
                            html.H1("Customer Database - U.S. Cloud FinOps Market",
                                    className="text-center mb-4 mt-3",
                                    style={
                                        'color': '#2E86AB',
                                        'fontWeight': '700',
                                        'fontSize': '2.2rem',
                                        'letterSpacing': '-0.5px'
                                    }),
                            className="main-heading-container"
                        ),
                        # Horizontal filters at top (conditionally rendered per page)
                        html.Div(id='filters-container'),
                        # Page content below filters
                        html.Div(id='page-content', className="content-area")
                    ],
                    className="main-content",
                ),
            ],
            className="app-container"
        ),
    ],
    className="app-wrapper"
)

# Callback for navbar toggle (mobile)
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# Callback to conditionally show/hide filters based on current page
@app.callback(
    Output('filters-container', 'children'),
    [Input('url', 'pathname')]
)
def update_filters_visibility(pathname):
    # Show filters on Overview and Analytics pages, hide on Customer Details page
    if pathname == '/customers':
        return html.Div()  # Empty div - no filters on Customer Details page
    else:
        # Show filters on Overview and Analytics pages
        return html.Div(
            create_filter_section(original_df),
            className="filters-section-horizontal"
        )

# Callback for filtering data
@app.callback(
    Output('filtered-data-store', 'data'),
    [
        Input('filter-industry', 'value'),
        Input('filter-cloud', 'value'),
        Input('filter-region', 'value'),
        Input('filter-optimization', 'value'),
        Input('filter-license', 'value'),
        Input('filter-opt-potential', 'value'),
        Input('reset-filters-btn', 'n_clicks'),
    ],
    prevent_initial_call=False
)
def update_filtered_data(industries, clouds, regions, opt_types, licenses, opt_range, reset_clicks):
    ctx = callback_context

    # Check if reset button was clicked
    if ctx.triggered and ctx.triggered[0]['prop_id'] == 'reset-filters-btn.n_clicks':
        return original_df.to_dict('records')

    # Apply filters
    filtered_df = apply_filters(original_df, industries, clouds, regions, opt_types, licenses, opt_range)

    return filtered_df.to_dict('records')

# Callback for page routing and content - OPTIMIZED
@app.callback(
    Output('page-content', 'children'),
    [
        Input('url', 'pathname'),
        Input('filtered-data-store', 'data')
    ],
    prevent_initial_call=False
)
def display_page(pathname, filtered_data):
    # Convert stored data back to DataFrame
    if not filtered_data:
        filtered_data = original_df.to_dict('records')

    df = pd.DataFrame(filtered_data)

    if df.empty:
        return html.Div(
            dbc.Alert(
                [
                    html.I(className="bi bi-exclamation-triangle-fill me-2"),
                    "No customers match the selected filters. Please adjust your filter criteria."
                ],
                color="warning",
                className="m-4"
            )
        )

    # Create a copy to avoid modifying original data
    df_copy = df.copy()

    if pathname == '/customers':
        return create_customer_details_layout(df_copy)
    elif pathname == '/analytics':
        return create_analytics_layout(df_copy)
    else:  # Default to overview
        return create_overview_layout(df_copy)

# Callback for customer detail card (on row selection in table)
@app.callback(
    Output('customer-detail-cards', 'children'),
    [Input('customer-table', 'selected_rows')],
    [State('customer-table', 'data')]
)
def display_customer_details(selected_rows, table_data):
    if not selected_rows or len(selected_rows) == 0:
        return html.Div(
            dbc.Alert(
                "Click on a row in the table above to view detailed customer information.",
                color="info",
                className="mt-4"
            )
        )

    selected_data = [table_data[i] for i in selected_rows]
    return create_customer_detail_card(selected_data)

# Callback for CSV export
@app.callback(
    Output("download-csv", "data"),
    [Input("export-csv-btn", "n_clicks")],
    [State('filtered-data-store', 'data')],
    prevent_initial_call=True,
)
def export_to_csv(n_clicks, filtered_data):
    if n_clicks:
        df = pd.DataFrame(filtered_data)
        return dcc.send_data_frame(df.to_csv, "customer_intelligence_export.csv", index=False)

# Callback to reset filters
@app.callback(
    [
        Output('filter-industry', 'value'),
        Output('filter-cloud', 'value'),
        Output('filter-region', 'value'),
        Output('filter-optimization', 'value'),
        Output('filter-license', 'value'),
        Output('filter-opt-potential', 'value'),
    ],
    [Input('reset-filters-btn', 'n_clicks')],
    prevent_initial_call=True
)
def reset_filters(n_clicks):
    if n_clicks:
        return [], [], [], [], [], [0, 50]
    return dash.no_update

# Run the app
if __name__ == '__main__':
    print("\n" + "="*60)
    print("  Customer Intelligence Dashboard")
    print("="*60)
    print(f"\n  Loaded {len(df)} customer records")
    print(f"  Industries: {df['Industry_Vertical'].nunique()}")
    print(f"  Cloud Platforms: {df['Cloud_Platforms'].nunique()}")

    # Get host and port from environment variables (for production deployment)
    # Default to localhost:8050 for local development
    host = os.getenv('HOST', '127.0.0.1')
    port = int(os.getenv('PORT', 8050))
    debug = os.getenv('DASH_DEBUG', 'True').lower() == 'true'

    print(f"\n  Starting server at http://{host}:{port}")
    print(f"  Debug mode: {debug}")
    print(f"  Press Ctrl+C to quit")
    print("="*60 + "\n")

    app.run_server(debug=debug, host=host, port=port)
