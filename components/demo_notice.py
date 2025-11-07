import dash_bootstrap_components as dbc
from dash import html

def create_demo_notice():
    """Create a highlighted demo data notice banner"""
    return dbc.Alert(
        [
            html.Div(
                [
                    html.I(className="bi bi-exclamation-circle-fill me-3",
                           style={"fontSize": "1.5rem", "verticalAlign": "middle"}),
                    html.Span(
                        [
                            html.Strong("Demo Data Notice", className="me-2",
                                       style={"fontSize": "1.1rem"}),
                            html.Span("This dashboard uses synthetic/demo data for illustration purposes only. No real-world vaccine market data is associated with this application.",
                                     style={"fontSize": "1rem"})
                        ],
                        style={"verticalAlign": "middle"}
                    )
                ],
                className="d-flex align-items-center"
            )
        ],
        color="warning",
        className="demo-notice-banner mb-4",
        style={
            "borderLeft": "5px solid #F18F01",
            "borderRadius": "8px",
            "boxShadow": "0 2px 8px rgba(241, 143, 1, 0.15)",
            "padding": "1rem 1.5rem",
            "backgroundColor": "#FFF9E6",
            "border": "1px solid #FFE0B2"
        }
    )
