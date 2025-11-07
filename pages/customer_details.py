import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table
import pandas as pd
from components.demo_notice import create_demo_notice

def create_customer_details_layout(df):
    """Create the customer details page with interactive table"""

    # Prepare columns for the data table - COMPREHENSIVE VIEW (FIXED: removed invalid 'width' property)
    columns = [
        {"name": "Sr No", "id": "Sr_No", "type": "numeric"},
        {"name": "Customer Name", "id": "Customer_Name", "type": "text"},
        {"name": "Industry", "id": "Industry_Vertical", "type": "text"},
        {"name": "Cloud Platform", "id": "Cloud_Platforms", "type": "text"},

        # Financial Metrics
        {"name": "IT Spend ($M)", "id": "Annual_IT_Spend_M", "type": "numeric", "format": {"specifier": ",.0f"}},
        {"name": "Cloud Spend ($M)", "id": "Current_Cloud_Spend_M", "type": "numeric", "format": {"specifier": ",.2f"}},
        {"name": "License Spend ($M)", "id": "Current_License_Spend_M", "type": "numeric", "format": {"specifier": ",.2f"}},
        {"name": "Cloud Savings ($M)", "id": "Potential_Cloud_Savings_M", "type": "numeric", "format": {"specifier": ",.2f"}},
        {"name": "License Savings ($M)", "id": "Potential_License_Savings_M", "type": "numeric", "format": {"specifier": ",.2f"}},
        {"name": "Total Savings ($M)", "id": "Total_Potential_Savings_M", "type": "numeric", "format": {"specifier": ",.2f"}},

        # Optimization Percentages
        {"name": "Cloud Opt %", "id": "Cloud_Optimization_Potential", "type": "numeric"},
        {"name": "ELO Opt %", "id": "ELO_Optimization_Potential", "type": "numeric"},
        {"name": "Total Opt %", "id": "Total_Optimization_Potential", "type": "numeric"},

        # Organization Metrics
        {"name": "Employees", "id": "Number_of_Employees", "type": "numeric", "format": {"specifier": ","}},
        {"name": "IT Team", "id": "IT_Team_Size", "type": "numeric", "format": {"specifier": ","}},

        # Infrastructure
        {"name": "VMs", "id": "Number_of_VMs", "type": "numeric", "format": {"specifier": ","}},
        {"name": "Physical Servers", "id": "Physical_Servers", "type": "numeric", "format": {"specifier": ","}},
        {"name": "Databases", "id": "Number_of_Databases", "type": "numeric", "format": {"specifier": ","}},
        {"name": "Applications", "id": "Number_of_Applications", "type": "numeric", "format": {"specifier": ","}},

        # Licenses
        {"name": "MS Licenses", "id": "Microsoft_Licenses", "type": "numeric", "format": {"specifier": ","}},
        {"name": "SAP Licenses", "id": "SAP_Licenses", "type": "numeric", "format": {"specifier": ","}},
        {"name": "Oracle Licenses", "id": "Oracle_Licenses", "type": "numeric", "format": {"specifier": ","}},

        # Cloud Resources
        {"name": "Azure VMs", "id": "Azure_VMs", "type": "numeric", "format": {"specifier": ","}},
        {"name": "AWS EC2", "id": "AWS_EC2_Instances", "type": "numeric", "format": {"specifier": ","}},
        {"name": "GCP VMs", "id": "GCP_VMs", "type": "numeric", "format": {"specifier": ","}},

        # ROI
        {"name": "Monthly Savings ($K)", "id": "Monthly_Savings_K", "type": "numeric", "format": {"specifier": ",.1f"}},
        {"name": "ROI Months", "id": "ROI_Payback_Months", "type": "numeric", "format": {"specifier": ".1f"}},

        # Contact & Engagement
        {"name": "Decision Maker", "id": "Decision_Maker", "type": "text"},
        {"name": "Phone", "id": "Phone", "type": "text"},
        {"name": "Email", "id": "Email", "type": "text"},
        {"name": "Engagement Score", "id": "Engagement_Score", "type": "numeric"},
        {"name": "Last Contact (days)", "id": "Last_Contact_Days_Ago", "type": "numeric"},
    ]

    layout = dbc.Container(
        [
            # Demo Data Notice
            create_demo_notice(),

            # Header
            dbc.Row(
                dbc.Col(
                    [
                        html.H2("Customer Details", className="page-title mb-1"),
                        html.P("Detailed customer information and contact details", className="page-subtitle text-muted"),
                    ],
                    width=12
                ),
                className="mb-4"
            ),

            # Export button
            dbc.Row(
                dbc.Col(
                    dbc.Button(
                        [html.I(className="bi bi-download me-2"), "Export to CSV"],
                        id="export-csv-btn",
                        color="primary",
                        size="sm",
                        className="mb-3"
                    ),
                    width=12
                ),
            ),
            dcc.Download(id="download-csv"),

            # Data Table
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                dash_table.DataTable(
                                    id='customer-table',
                                    columns=columns,
                                    data=df.to_dict('records'),
                                    page_size=20,
                                    page_action='native',
                                    sort_action='native',
                                    sort_mode='multi',
                                    filter_action='native',
                                    style_table={'overflowX': 'auto'},
                                    style_cell={
                                        'textAlign': 'left',
                                        'padding': '12px',
                                        'fontFamily': 'Arial, sans-serif',
                                        'fontSize': '14px',
                                        'height': 'auto',
                                    },
                                    # FIXED: Proper column width styling using style_cell_conditional
                                    style_cell_conditional=[
                                        {'if': {'column_id': 'Sr_No'}, 'minWidth': '70px', 'width': '70px', 'maxWidth': '70px'},
                                        {'if': {'column_id': 'Customer_Name'}, 'minWidth': '200px', 'width': '200px', 'maxWidth': '200px'},
                                        {'if': {'column_id': 'Industry_Vertical'}, 'minWidth': '180px', 'width': '180px', 'maxWidth': '180px'},
                                        {'if': {'column_id': 'Cloud_Platforms'}, 'minWidth': '150px', 'width': '150px', 'maxWidth': '150px'},
                                        # Financial
                                        {'if': {'column_id': 'Annual_IT_Spend_M'}, 'minWidth': '120px', 'width': '120px', 'maxWidth': '120px'},
                                        {'if': {'column_id': 'Current_Cloud_Spend_M'}, 'minWidth': '130px', 'width': '130px', 'maxWidth': '130px'},
                                        {'if': {'column_id': 'Current_License_Spend_M'}, 'minWidth': '140px', 'width': '140px', 'maxWidth': '140px'},
                                        {'if': {'column_id': 'Potential_Cloud_Savings_M'}, 'minWidth': '140px', 'width': '140px', 'maxWidth': '140px'},
                                        {'if': {'column_id': 'Potential_License_Savings_M'}, 'minWidth': '150px', 'width': '150px', 'maxWidth': '150px'},
                                        {'if': {'column_id': 'Total_Potential_Savings_M'}, 'minWidth': '140px', 'width': '140px', 'maxWidth': '140px'},
                                        # Optimization
                                        {'if': {'column_id': 'Cloud_Optimization_Potential'}, 'minWidth': '100px', 'width': '100px', 'maxWidth': '100px'},
                                        {'if': {'column_id': 'ELO_Optimization_Potential'}, 'minWidth': '100px', 'width': '100px', 'maxWidth': '100px'},
                                        {'if': {'column_id': 'Total_Optimization_Potential'}, 'minWidth': '100px', 'width': '100px', 'maxWidth': '100px'},
                                        # Organization
                                        {'if': {'column_id': 'Number_of_Employees'}, 'minWidth': '110px', 'width': '110px', 'maxWidth': '110px'},
                                        {'if': {'column_id': 'IT_Team_Size'}, 'minWidth': '100px', 'width': '100px', 'maxWidth': '100px'},
                                        # Infrastructure
                                        {'if': {'column_id': 'Number_of_VMs'}, 'minWidth': '90px', 'width': '90px', 'maxWidth': '90px'},
                                        {'if': {'column_id': 'Physical_Servers'}, 'minWidth': '130px', 'width': '130px', 'maxWidth': '130px'},
                                        {'if': {'column_id': 'Number_of_Databases'}, 'minWidth': '110px', 'width': '110px', 'maxWidth': '110px'},
                                        {'if': {'column_id': 'Number_of_Applications'}, 'minWidth': '120px', 'width': '120px', 'maxWidth': '120px'},
                                        # Licenses
                                        {'if': {'column_id': 'Microsoft_Licenses'}, 'minWidth': '120px', 'width': '120px', 'maxWidth': '120px'},
                                        {'if': {'column_id': 'SAP_Licenses'}, 'minWidth': '110px', 'width': '110px', 'maxWidth': '110px'},
                                        {'if': {'column_id': 'Oracle_Licenses'}, 'minWidth': '120px', 'width': '120px', 'maxWidth': '120px'},
                                        # Cloud Resources
                                        {'if': {'column_id': 'Azure_VMs'}, 'minWidth': '100px', 'width': '100px', 'maxWidth': '100px'},
                                        {'if': {'column_id': 'AWS_EC2_Instances'}, 'minWidth': '100px', 'width': '100px', 'maxWidth': '100px'},
                                        {'if': {'column_id': 'GCP_VMs'}, 'minWidth': '100px', 'width': '100px', 'maxWidth': '100px'},
                                        # ROI
                                        {'if': {'column_id': 'Monthly_Savings_K'}, 'minWidth': '140px', 'width': '140px', 'maxWidth': '140px'},
                                        {'if': {'column_id': 'ROI_Payback_Months'}, 'minWidth': '110px', 'width': '110px', 'maxWidth': '110px'},
                                        # Contact
                                        {'if': {'column_id': 'Decision_Maker'}, 'minWidth': '150px', 'width': '150px', 'maxWidth': '150px'},
                                        {'if': {'column_id': 'Phone'}, 'minWidth': '140px', 'width': '140px', 'maxWidth': '140px'},
                                        {'if': {'column_id': 'Email'}, 'minWidth': '350px', 'width': '350px', 'maxWidth': '350px'},
                                        {'if': {'column_id': 'Engagement_Score'}, 'minWidth': '130px', 'width': '130px', 'maxWidth': '130px'},
                                        {'if': {'column_id': 'Last_Contact_Days_Ago'}, 'minWidth': '140px', 'width': '140px', 'maxWidth': '140px'},
                                    ],
                                    style_header={
                                        'backgroundColor': '#2E86AB',
                                        'color': 'white',
                                        'fontWeight': 'bold',
                                        'textAlign': 'left',
                                        'border': '1px solid #ddd',
                                    },
                                    style_data={
                                        'border': '1px solid #ddd',
                                        'whiteSpace': 'normal',
                                        'height': 'auto',
                                    },
                                    style_data_conditional=[
                                        {
                                            'if': {'row_index': 'odd'},
                                            'backgroundColor': '#f8f9fa',
                                        },
                                        {
                                            'if': {'column_id': 'Total_Optimization_Potential'},
                                            'fontWeight': 'bold',
                                            'color': '#06A77D',
                                        },
                                        {
                                            'if': {'column_id': 'Total_Potential_Savings_M'},
                                            'fontWeight': 'bold',
                                            'color': '#06A77D',
                                        },
                                    ],
                                    style_filter={
                                        'backgroundColor': '#f1f3f5',
                                        'fontWeight': 'normal',
                                    },
                                    tooltip_data=[
                                        {
                                            column: {'value': str(value), 'type': 'markdown'}
                                            for column, value in row.items()
                                        } for row in df.to_dict('records')
                                    ],
                                    tooltip_duration=None,
                                ),
                            ]
                        ),
                        className="shadow-sm"
                    ),
                    width=12
                ),
                className="mb-4"
            ),

            # Customer Details Cards
            html.Div(id='customer-detail-cards', className="mt-4"),
        ],
        fluid=True,
        className="page-container"
    )

    return layout

def create_customer_detail_card(customer_data):
    """Create a detailed card for a selected customer"""
    if not customer_data or len(customer_data) == 0:
        return html.Div()

    customer = customer_data[0]  # Get first selected row

    card = dbc.Card(
        [
            dbc.CardHeader(
                html.H4(customer.get('Customer_Name', 'N/A'), className="mb-0"),
                className="bg-primary text-white"
            ),
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.H6("Overview", className="text-primary mb-3"),
                                    html.P([html.Strong("Industry: "), customer.get('Industry_Vertical', 'N/A')]),
                                    html.P([html.Strong("Location: "), customer.get('Geographical_Presence', 'N/A')]),
                                    html.P([html.Strong("Product Offering: "), customer.get('Product_Offering', 'N/A')], className="text-wrap"),
                                ],
                                md=6
                            ),
                            dbc.Col(
                                [
                                    html.H6("Technical Details", className="text-primary mb-3"),
                                    html.P([html.Strong("Cloud Platform: "), customer.get('Cloud_Platforms', 'N/A')]),
                                    html.P([html.Strong("License Ecosystem: "), customer.get('License_Ecosystem', 'N/A')], className="text-wrap"),
                                    html.P([html.Strong("Optimization Type: "), customer.get('Optimization_Type', 'N/A')]),
                                ],
                                md=6
                            ),
                        ],
                        className="mb-3"
                    ),
                    html.Hr(),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.H6("Optimization Potential", className="text-success mb-3"),
                                    html.P([html.Strong("Cloud Optimization: "), f"{customer.get('Cloud_Optimization_Potential', 0)}%"]),
                                    html.P([html.Strong("ELO Optimization: "), f"{customer.get('ELO_Optimization_Potential', 0)}%"]),
                                    html.P([html.Strong("Total Potential: "), f"{customer.get('Total_Optimization_Potential', 0)}%"], className="text-success fw-bold"),
                                ],
                                md=6
                            ),
                            dbc.Col(
                                [
                                    html.H6("Contact Information", className="text-info mb-3"),
                                    html.P([html.Strong("Decision Maker: "), customer.get('Decision_Maker', 'N/A')]),
                                    html.P([html.Strong("Phone: "), customer.get('Phone', 'N/A')]),
                                    html.P([html.Strong("Email: "), customer.get('Email', 'N/A')]),
                                ],
                                md=6
                            ),
                        ],
                        className="mb-3"
                    ),
                    html.Hr(),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.H6("Business Context", className="text-warning mb-3"),
                                    html.P([html.Strong("Pain Points: "), customer.get('Pain_Points', 'N/A')], className="text-wrap"),
                                    html.P([html.Strong("Trigger Event: "), customer.get('Trigger_Event', 'N/A')], className="text-wrap"),
                                    html.P([html.Strong("Key Stakeholders: "), customer.get('Key_Stakeholders', 'N/A')], className="text-wrap"),
                                ],
                                md=12
                            ),
                        ],
                    ),
                ]
            )
        ],
        className="shadow-sm mb-4"
    )

    return card
