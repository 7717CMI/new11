import dash_bootstrap_components as dbc
from dash import html, dcc

def create_sidebar():
    """Create the navigation sidebar"""
    sidebar = html.Div(
        [
            html.Div(
                [
                    html.H3("Customer Intelligence", className="sidebar-title"),
                    html.Hr(className="sidebar-divider"),
                ],
                className="sidebar-header",
            ),
            dbc.Nav(
                [
                    dbc.NavLink(
                        [
                            html.I(className="bi bi-house-door me-2"),
                            html.Span("Overview Dashboard")
                        ],
                        href="/",
                        active="exact",
                        id="nav-overview",
                        className="nav-link-custom"
                    ),
                    dbc.NavLink(
                        [
                            html.I(className="bi bi-people me-2"),
                            html.Span("Customer Details")
                        ],
                        href="/customers",
                        active="exact",
                        id="nav-customers",
                        className="nav-link-custom"
                    ),
                    dbc.NavLink(
                        [
                            html.I(className="bi bi-graph-up me-2"),
                            html.Span("Analytics Deep-Dive")
                        ],
                        href="/analytics",
                        active="exact",
                        id="nav-analytics",
                        className="nav-link-custom"
                    ),
                ],
                vertical=True,
                pills=True,
                className="sidebar-nav",
            ),
        ],
        className="sidebar",
        id="sidebar",
    )

    return sidebar

def create_navbar():
    """Create the top navbar for mobile responsiveness"""
    navbar = dbc.Navbar(
        dbc.Container(
            [
                dbc.NavbarBrand(
                    [
                        html.I(className="bi bi-speedometer2 me-2"),
                        "Customer Intelligence Dashboard"
                    ],
                    className="navbar-brand-custom"
                ),
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavItem(dbc.NavLink("Overview", href="/")),
                            dbc.NavItem(dbc.NavLink("Customers", href="/customers")),
                            dbc.NavItem(dbc.NavLink("Analytics", href="/analytics")),
                        ],
                        className="ms-auto",
                        navbar=True,
                    ),
                    id="navbar-collapse",
                    is_open=False,
                    navbar=True,
                ),
            ],
            fluid=True,
        ),
        color="primary",
        dark=True,
        className="mb-3 navbar-custom",
    )

    return navbar
