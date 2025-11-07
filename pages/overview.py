import dash_bootstrap_components as dbc
from dash import html, dcc
import pandas as pd
from components.charts import *
from components.demo_notice import create_demo_notice

def create_kpi_card(title, value, icon, color="primary", subtitle=None):
    """Create a KPI card component"""
    return dbc.Card(
        dbc.CardBody(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.I(className=f"bi {icon} kpi-icon", style={"color": COLORS.get(color, COLORS['primary'])}),
                            ],
                            className="kpi-icon-container"
                        ),
                        html.Div(
                            [
                                html.H6(title, className="kpi-title mb-1"),
                                html.H3(value, className="kpi-value mb-0"),
                                html.P(subtitle, className="kpi-subtitle mt-1 mb-0") if subtitle else None,
                            ],
                            className="kpi-content"
                        ),
                    ],
                    className="d-flex align-items-center"
                ),
            ]
        ),
        className="kpi-card shadow-sm mb-3",
    )

def create_overview_layout(df):
    """Create the overview dashboard layout"""

    # Calculate KPIs
    total_customers = len(df)
    avg_opt_potential = df['Total_Optimization_Potential'].mean()
    total_cloud_opt = df['Cloud_Optimization_Potential'].sum()
    total_elo_opt = df['ELO_Optimization_Potential'].sum()

    # Industry distribution
    industry_counts = df['Industry_Vertical'].value_counts().reset_index()
    industry_counts.columns = ['Industry', 'Count']

    # Cloud platform distribution
    cloud_counts = df['Cloud_Platforms'].value_counts().reset_index()
    cloud_counts.columns = ['Platform', 'Count']

    # Optimization type distribution
    opt_type_counts = df['Optimization_Type'].value_counts().reset_index()
    opt_type_counts.columns = ['Type', 'Count']

    # Optimization potential by industry
    opt_by_industry = df.groupby('Industry_Vertical').agg({
        'Cloud_Optimization_Potential': 'mean',
        'ELO_Optimization_Potential': 'mean'
    }).round(1).reset_index()
    opt_by_industry.columns = ['Industry', 'Cloud Opt %', 'ELO Opt %']

    layout = dbc.Container(
        [
            # Demo Data Notice
            create_demo_notice(),

            # Header
            dbc.Row(
                dbc.Col(
                    [
                        html.H2("Customer Intelligence Overview", className="page-title mb-1"),
                        html.P("Comprehensive view of customer optimization opportunities", className="page-subtitle text-muted"),
                    ],
                    width=12
                ),
                className="mb-4"
            ),

            # KPI Cards
            dbc.Row(
                [
                    dbc.Col(
                        create_kpi_card(
                            "Total Customers",
                            f"{total_customers}",
                            "bi-people-fill",
                            "primary",
                            "Active in database"
                        ),
                        xs=12, sm=6, lg=3
                    ),
                    dbc.Col(
                        create_kpi_card(
                            "Avg Optimization Potential",
                            f"{avg_opt_potential:.1f}%",
                            "bi-graph-up-arrow",
                            "success",
                            "Combined Cloud + ELO"
                        ),
                        xs=12, sm=6, lg=3
                    ),
                    dbc.Col(
                        create_kpi_card(
                            "Total Cloud Potential",
                            f"{total_cloud_opt:.0f}%",
                            "bi-cloud-arrow-up",
                            "info",
                            "Across all customers"
                        ),
                        xs=12, sm=6, lg=3
                    ),
                    dbc.Col(
                        create_kpi_card(
                            "Total ELO Potential",
                            f"{total_elo_opt:.0f}%",
                            "bi-file-earmark-text",
                            "warning",
                            "License optimization"
                        ),
                        xs=12, sm=6, lg=3
                    ),
                ],
                className="mb-4"
            ),

            # Divider
            html.Hr(className="my-4"),

            # Section: Industry Analysis
            html.H4("Industry Analysis", className="section-title mb-3 mt-2"),
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Top 10 Industries by Customer Count", className="chart-title text-center mb-3"),
                                dcc.Graph(
                                    id='chart-industry-distribution',
                                    figure=create_bar_chart(
                                        industry_counts.head(10),
                                        'Industry',
                                        'Count',
                                        '',  # Empty title since we have card title
                                        COLORS['primary']
                                    ),
                                    config={'displayModeBar': False},
                                    style={'height': '580px'}
                                )
                            ]
                        ),
                        className="chart-card shadow-sm"
                    ),
                    xs=12, className="mb-5"
                ),
            ),

            # Section: Cloud Platform Distribution
            html.H4("Cloud Platform Distribution", className="section-title mb-3"),
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Cloud Platform Usage Across Customers", className="chart-title text-center mb-3"),
                                dcc.Graph(
                                    id='chart-cloud-distribution',
                                    figure=create_pie_chart(
                                        cloud_counts,
                                        'Platform',
                                        'Count',
                                        ''  # Empty title since we have card title
                                    ),
                                    config={'displayModeBar': False},
                                    style={'height': '580px'}
                                )
                            ]
                        ),
                        className="chart-card shadow-sm"
                    ),
                    xs=12, className="mb-5"
                ),
            ),

            # Section: Optimization Type Distribution
            html.H4("Optimization Type Distribution", className="section-title mb-3"),
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Cloud FinOps vs ELO Distribution", className="chart-title text-center mb-3"),
                                dcc.Graph(
                                    id='chart-optimization-type',
                                    figure=create_pie_chart(
                                        opt_type_counts,
                                        'Type',
                                        'Count',
                                        ''  # Empty title since we have card title
                                    ),
                                    config={'displayModeBar': False},
                                    style={'height': '580px'}
                                )
                            ]
                        ),
                        className="chart-card shadow-sm"
                    ),
                    xs=12, className="mb-5"
                ),
            ),

            # Section: Optimization Potential by Industry
            html.H4("Optimization Potential by Industry", className="section-title mb-3"),
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Average Cloud & ELO Optimization Potential", className="chart-title text-center mb-3"),
                                dcc.Graph(
                                    id='chart-opt-by-industry',
                                    figure=create_grouped_bar_chart(
                                        opt_by_industry.head(8),
                                        'Industry',
                                        ['Cloud Opt %', 'ELO Opt %'],
                                        ''  # Empty title since we have card title
                                    ),
                                    config={'displayModeBar': False},
                                    style={'height': '680px'}
                                )
                            ]
                        ),
                        className="chart-card shadow-sm"
                    ),
                    xs=12, className="mb-5"
                ),
            ),

            # Section: Customer-Level Optimization Potential
            html.H4("Customer-Level Optimization Potential", className="section-title mb-3"),
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Total Optimization Potential by Customer (Color = Industry)", className="chart-title text-center mb-3"),
                                dcc.Graph(
                                    id='chart-scatter-optimization',
                                    figure=create_scatter_chart(
                                        df,
                                        'Sr_No',
                                        'Total_Optimization_Potential',
                                        'Industry_Vertical',
                                        ''  # Empty title since we have card title
                                    ),
                                    config={'displayModeBar': False},
                                    style={'height': '630px'}
                                )
                            ]
                        ),
                        className="chart-card shadow-sm"
                    ),
                    xs=12, className="mb-5"
                ),
            ),
        ],
        fluid=True,
        className="page-container"
    )

    return layout
