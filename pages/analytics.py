import dash_bootstrap_components as dbc
from dash import html, dcc
import pandas as pd
from components.charts import *
from components.demo_notice import create_demo_notice

def create_analytics_layout(df):
    """Create the analytics deep-dive page"""

    # Prepare data for advanced analytics

    # 1. License ecosystem breakdown - OPTIMIZED
    # Use vectorized operations instead of loops
    license_series = df['License_Ecosystem'].str.split(',').explode().str.strip()
    license_counts = license_series.value_counts().reset_index()
    license_counts.columns = ['License', 'Count']

    # 2. Regional analysis - OPTIMIZED
    # Use vectorized string operations
    df['Region_Clean'] = df['Geographical_Presence'].str.split('operates across', n=1).str[-1].str.strip()
    df['Region_Clean'] = df['Region_Clean'].fillna('Unknown')

    region_summary = df.groupby('Region_Clean').agg({
        'Total_Optimization_Potential': 'mean',
        'Cloud_Optimization_Potential': 'mean',
        'ELO_Optimization_Potential': 'mean'
    }).round(1).reset_index()
    region_summary.columns = ['Region', 'Avg Total %', 'Avg Cloud %', 'Avg ELO %']

    # 3. Cloud vs ELO comparison by industry
    opt_comparison = df.groupby('Industry_Vertical').agg({
        'Cloud_Optimization_Potential': 'sum',
        'ELO_Optimization_Potential': 'sum'
    }).reset_index()
    opt_comparison.columns = ['Industry', 'Total Cloud Opt', 'Total ELO Opt']

    # 4. Decision maker distribution
    decision_makers = df['Decision_Maker'].value_counts().reset_index()
    decision_makers.columns = ['Role', 'Count']

    # 5. Trigger events analysis
    trigger_counts = df['Trigger_Event'].value_counts().head(10).reset_index()
    trigger_counts.columns = ['Trigger', 'Count']

    layout = dbc.Container(
        [
            # Demo Data Notice
            create_demo_notice(),

            # Header
            dbc.Row(
                dbc.Col(
                    [
                        html.H2("Analytics Deep-Dive", className="page-title mb-1"),
                        html.P("Advanced analysis and insights into customer opportunities", className="page-subtitle text-muted"),
                    ],
                    width=12
                ),
                className="mb-4"
            ),

            # Stats Cards
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H6("Unique Industries", className="text-muted mb-2"),
                                    html.H3(f"{df['Industry_Vertical'].nunique()}", className="mb-0 text-primary"),
                                ]
                            ),
                            className="text-center shadow-sm"
                        ),
                        xs=12, sm=6, md=3, className="mb-3"
                    ),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H6("Cloud Platforms", className="text-muted mb-2"),
                                    html.H3(f"{df['Cloud_Platforms'].nunique()}", className="mb-0 text-info"),
                                ]
                            ),
                            className="text-center shadow-sm"
                        ),
                        xs=12, sm=6, md=3, className="mb-3"
                    ),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H6("Avg Cloud Opt", className="text-muted mb-2"),
                                    html.H3(f"{df['Cloud_Optimization_Potential'].mean():.1f}%", className="mb-0 text-success"),
                                ]
                            ),
                            className="text-center shadow-sm"
                        ),
                        xs=12, sm=6, md=3, className="mb-3"
                    ),
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H6("Avg ELO Opt", className="text-muted mb-2"),
                                    html.H3(f"{df['ELO_Optimization_Potential'].mean():.1f}%", className="mb-0 text-warning"),
                                ]
                            ),
                            className="text-center shadow-sm"
                        ),
                        xs=12, sm=6, md=3, className="mb-3"
                    ),
                ],
            ),

            # Chart 1: License Ecosystem Usage
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("License Ecosystem Usage", className="chart-title text-center mb-3"),
                                dcc.Graph(
                                    id='chart-license-breakdown',
                                    figure=create_bar_chart(
                                        license_counts,
                                        'License',
                                        'Count',
                                        '',
                                        COLORS['accent1']
                                    ),
                                    config={'displayModeBar': False},
                                    style={'height': '600px'}
                                )
                            ]
                        ),
                        className="chart-card shadow-sm"
                    ),
                    xs=12, className="mb-5"
                ),
            ),

            # Chart 2: Optimization Potential by Region
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Optimization Potential by Region", className="chart-title text-center mb-3"),
                                dcc.Graph(
                                    id='chart-region-optimization',
                                    figure=create_grouped_bar_chart(
                                        region_summary.head(10),
                                        'Region',
                                        ['Avg Cloud %', 'Avg ELO %'],
                                        ''
                                    ),
                                    config={'displayModeBar': False},
                                    style={'height': '700px'}
                                )
                            ]
                        ),
                        className="chart-card shadow-sm"
                    ),
                    xs=12, className="mb-5"
                ),
            ),

            # Chart 3: Total Optimization Potential Cloud vs ELO
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Total Optimization Potential: Cloud vs ELO by Industry", className="chart-title text-center mb-3"),
                                dcc.Graph(
                                    id='chart-cloud-vs-elo',
                                    figure=create_stacked_bar_chart(
                                        opt_comparison.head(10),
                                        'Industry',
                                        ['Total Cloud Opt', 'Total ELO Opt'],
                                        ''
                                    ),
                                    config={'displayModeBar': False},
                                    style={'height': '650px'}
                                )
                            ]
                        ),
                        className="chart-card shadow-sm"
                    ),
                    xs=12, className="mb-5"
                ),
            ),

            # Chart 4: Decision Maker Distribution
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Decision Maker Distribution", className="chart-title text-center mb-3"),
                                dcc.Graph(
                                    id='chart-decision-makers',
                                    figure=create_pie_chart(
                                        decision_makers,
                                        'Role',
                                        'Count',
                                        ''
                                    ),
                                    config={'displayModeBar': False},
                                    style={'height': '600px'}
                                )
                            ]
                        ),
                        className="chart-card shadow-sm"
                    ),
                    xs=12, className="mb-5"
                ),
            ),

            # Insights Section
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                html.H5("Key Insights", className="mb-0"),
                                className="bg-primary text-white"
                            ),
                            dbc.CardBody(
                                [
                                    html.Ul(
                                        [
                                            html.Li([
                                                html.Strong("Top License System: "),
                                                f"{license_counts.iloc[0]['License']} used by {license_counts.iloc[0]['Count']} customers"
                                            ], className="mb-2"),
                                            html.Li([
                                                html.Strong("Highest Cloud Optimization: "),
                                                f"{df.loc[df['Cloud_Optimization_Potential'].idxmax()]['Customer_Name']} "
                                                f"with {df['Cloud_Optimization_Potential'].max()}% potential"
                                            ], className="mb-2"),
                                            html.Li([
                                                html.Strong("Highest ELO Optimization: "),
                                                f"{df.loc[df['ELO_Optimization_Potential'].idxmax()]['Customer_Name']} "
                                                f"with {df['ELO_Optimization_Potential'].max()}% potential"
                                            ], className="mb-2"),
                                            html.Li([
                                                html.Strong("Most Common Decision Maker: "),
                                                f"{decision_makers.iloc[0]['Role']} ({decision_makers.iloc[0]['Count']} customers)"
                                            ], className="mb-2"),
                                            html.Li([
                                                html.Strong("Top Industry: "),
                                                f"{df['Industry_Vertical'].value_counts().index[0]} "
                                                f"with {df['Industry_Vertical'].value_counts().values[0]} customers"
                                            ]),
                                        ],
                                        className="insights-list"
                                    )
                                ]
                            )
                        ],
                        className="shadow-sm"
                    ),
                    width=12, className="mb-4"
                ),
            ),
        ],
        fluid=True,
        className="page-container"
    )

    return layout
