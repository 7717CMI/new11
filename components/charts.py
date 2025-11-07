import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

# Standard professional color palette
COLORS = {
    'primary': '#2E86AB',      # Professional Blue
    'secondary': '#A23B72',    # Deep Magenta
    'success': '#06A77D',      # Emerald Green
    'warning': '#F18F01',      # Warm Orange
    'danger': '#C73E1D',       # Brick Red
    'info': '#6A4C93',         # Royal Purple
    'accent1': '#52B788',      # Mint Green
    'accent2': '#F77F00',      # Bright Orange
    'accent3': '#4ECDC4',      # Turquoise
    'accent4': '#FF6B6B',      # Coral Red
    'neutral': '#6C757D',      # Gray
    'light': '#F8F9FA',        # Light Gray
    'dark': '#212529',         # Dark Gray
}

COLOR_SEQUENCE = [
    COLORS['primary'], COLORS['success'], COLORS['warning'],
    COLORS['secondary'], COLORS['info'], COLORS['accent1'],
    COLORS['accent2'], COLORS['accent3'], COLORS['accent4'], COLORS['danger']
]

def create_bar_chart(df, x_col, y_col, title, color=COLORS['primary']):
    """Create a simple bar chart with improved readability and spacing"""
    fig = go.Figure(data=[
        go.Bar(
            x=df[x_col],
            y=df[y_col],
            marker=dict(
                color=color,
                line=dict(color='white', width=2)
            ),
            text=df[y_col],
            textposition='outside',
            textfont=dict(size=12, color='#212529'),
            hovertemplate='<b>%{x}</b><br>Count: %{y}<extra></extra>',
            width=0.7
        )
    ])

    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor='center', font=dict(size=16, color='#212529')),
        xaxis_title=dict(text=x_col, font=dict(size=14, color='#212529')),
        yaxis_title=dict(text=y_col, font=dict(size=14, color='#212529')),
        template='plotly_white',
        height=530,
        margin=dict(l=80, r=60, t=100, b=180),
        font=dict(family="Arial, sans-serif", size=12),
        plot_bgcolor='rgba(248,249,250,0.3)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            tickangle=-45,
            tickfont=dict(size=11.5),
            automargin=True,
            showgrid=False
        ),
        yaxis=dict(
            tickfont=dict(size=11.5),
            automargin=True,
            showgrid=True,
            gridcolor='rgba(200,200,200,0.3)',
            gridwidth=1
        ),
        bargap=0.2
    )

    return fig

def create_pie_chart(df, names_col, values_col, title):
    """Create a pie chart with proper legend visibility and improved readability"""
    fig = go.Figure(data=[
        go.Pie(
            labels=df[names_col],
            values=df[values_col],
            marker=dict(
                colors=COLOR_SEQUENCE,
                line=dict(color='white', width=2)  # Add white borders between slices
            ),
            textposition='auto',  # Auto position for better label placement
            textinfo='percent+label',  # Show both percentage and label
            textfont=dict(size=11, color='#212529'),
            insidetextfont=dict(size=11, color='white'),  # White text inside slices
            outsidetextfont=dict(size=11, color='#212529'),  # Dark text outside slices
            hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>',
            pull=[0.02] * len(df),  # Slight pull for all slices for better separation
            hole=0.3  # Create donut chart for better visual balance
        )
    ])

    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor='center', font=dict(size=16, color='#212529')),
        template='plotly_white',
        height=520,
        margin=dict(l=40, r=220, t=100, b=60),
        font=dict(family="Arial, sans-serif", size=12),
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="top",
            y=0.98,
            xanchor="left",
            x=1.05,
            font=dict(size=11),
            itemsizing='constant',
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='#ddd',
            borderwidth=1
        ),
    )

    return fig

def create_grouped_bar_chart(df, x_col, y_cols, title):
    """Create a grouped bar chart with improved spacing and readability"""
    fig = go.Figure()

    for i, col in enumerate(y_cols):
        fig.add_trace(go.Bar(
            name=col,
            x=df[x_col],
            y=df[col],
            marker=dict(
                color=COLOR_SEQUENCE[i % len(COLOR_SEQUENCE)],
                line=dict(color='white', width=1.5)
            ),
            text=df[col].apply(lambda x: f'{x:.1f}'),
            textposition='outside',
            textfont=dict(size=11),
            hovertemplate=f'<b>%{{x}}</b><br>{col}: %{{y:.1f}}%<extra></extra>',
            width=0.4  # Wider bars for better visibility
        ))

    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor='center', font=dict(size=16, color='#212529')),
        xaxis_title=dict(text=x_col, font=dict(size=13, color='#212529')),
        yaxis_title=dict(text="Optimization Potential (%)", font=dict(size=13, color='#212529')),
        barmode='group',
        template='plotly_white',
        height=620,
        margin=dict(l=80, r=60, t=100, b=240),
        font=dict(family="Arial, sans-serif", size=12),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.48,
            xanchor="center",
            x=0.5,
            font=dict(size=12),
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='#ddd',
            borderwidth=1
        ),
        plot_bgcolor='rgba(248,249,250,0.3)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            tickangle=-45,
            tickfont=dict(size=10.5),
            automargin=True,
            showgrid=False
        ),
        yaxis=dict(
            tickfont=dict(size=11),
            automargin=True,
            showgrid=True,
            gridcolor='rgba(200,200,200,0.3)',
            gridwidth=1
        ),
        bargap=0.3,  # Gap between bar groups - increased for better separation
        bargroupgap=0.1  # Small gap between bars within a group
    )

    return fig

def create_stacked_bar_chart(df, x_col, y_cols, title):
    """Create a stacked bar chart with proper spacing and no overlapping"""
    fig = go.Figure()

    for i, col in enumerate(y_cols):
        fig.add_trace(go.Bar(
            name=col,
            x=df[x_col],
            y=df[col],
            marker=dict(
                color=COLOR_SEQUENCE[i % len(COLOR_SEQUENCE)],
                line=dict(color='white', width=1.5)  # Add white borders between stacks
            ),
            text=df[col].apply(lambda x: f'{x:.0f}' if x >= 10 else ''),  # Only show text if value >= 10
            textposition='inside',
            textfont=dict(size=11, color='white'),
            hovertemplate=f'<b>%{{x}}</b><br>{col}: %{{y:.1f}}<extra></extra>',
            width=0.65  # Reduce bar width for better spacing between categories
        ))

    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor='center', font=dict(size=16, color='#212529')),
        xaxis_title=dict(text=x_col, font=dict(size=13, color='#212529')),
        yaxis_title=dict(text="Optimization Potential (%)", font=dict(size=13, color='#212529')),
        barmode='stack',
        template='plotly_white',
        height=580,
        margin=dict(l=80, r=60, t=100, b=200),
        font=dict(family="Arial, sans-serif", size=12),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.38,
            xanchor="center",
            x=0.5,
            font=dict(size=12),
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='#ddd',
            borderwidth=1
        ),
        plot_bgcolor='rgba(248,249,250,0.3)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            tickangle=-45,
            tickfont=dict(size=10.5),
            automargin=True,
            showgrid=False
        ),
        yaxis=dict(
            tickfont=dict(size=11),
            automargin=True,
            showgrid=True,
            gridcolor='rgba(200,200,200,0.3)',
            gridwidth=1
        ),
        bargap=0.25,  # Gap between bars (categories) - increased for better separation
        bargroupgap=0.0  # No gap within groups since we're stacking
    )

    return fig

def create_scatter_chart(df, x_col, y_col, color_col, title):
    """Create a scatter plot with proper visibility"""
    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        color=color_col,
        hover_data=['Customer_Name'],
        title='',  # Title will be set in layout
        color_discrete_sequence=COLOR_SEQUENCE,
        size_max=15,
    )

    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor='center', font=dict(size=16, color='#212529')),
        xaxis_title=dict(text=x_col, font=dict(size=13, color='#212529')),
        yaxis_title=dict(text=y_col, font=dict(size=13, color='#212529')),
        template='plotly_white',
        height=550,
        margin=dict(l=60, r=200, t=80, b=60),
        font=dict(family="Arial, sans-serif", size=12),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            tickfont=dict(size=11),
            automargin=True
        ),
        yaxis=dict(
            tickfont=dict(size=11),
            automargin=True
        ),
        legend=dict(
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.02,
            font=dict(size=10),
            title=dict(text=color_col, font=dict(size=11))
        )
    )

    fig.update_traces(marker=dict(size=12, line=dict(width=1, color='white')))

    return fig

def create_horizontal_bar_chart(df, x_col, y_col, title, color=COLORS['primary']):
    """Create a horizontal bar chart with improved readability and spacing"""
    fig = go.Figure(data=[
        go.Bar(
            x=df[x_col],
            y=df[y_col],
            orientation='h',
            marker=dict(
                color=color,
                line=dict(color='white', width=2)
            ),
            text=df[x_col],
            textposition='outside',
            textfont=dict(size=12, color='#212529'),
            hovertemplate='<b>%{y}</b><br>Value: %{x}<extra></extra>',
            width=0.65
        )
    ])

    fig.update_layout(
        title=dict(text=title, x=0.5, xanchor='center', font=dict(size=16, color='#212529')),
        xaxis_title=dict(text=x_col, font=dict(size=14, color='#212529')),
        yaxis_title=dict(text=y_col, font=dict(size=14, color='#212529')),
        template='plotly_white',
        height=max(550, len(df) * 42),  # Dynamic height with better spacing
        margin=dict(l=280, r=120, t=100, b=80),
        font=dict(family="Arial, sans-serif", size=12),
        plot_bgcolor='rgba(248,249,250,0.3)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            tickfont=dict(size=12),
            automargin=True,
            showgrid=True,
            gridcolor='rgba(200,200,200,0.3)',
            gridwidth=1
        ),
        yaxis=dict(
            tickfont=dict(size=11.5),
            automargin=True,
            tickmode='linear',
            showgrid=False
        ),
        bargap=0.2
    )

    return fig

def create_kpi_card_data(value, title, delta=None, delta_color="green"):
    """Prepare data for KPI cards"""
    return {
        'value': value,
        'title': title,
        'delta': delta,
        'delta_color': delta_color
    }

def create_sunburst_chart(df, path_cols, values_col, title):
    """Create a sunburst chart for hierarchical data"""
    fig = px.sunburst(
        df,
        path=path_cols,
        values=values_col,
        title=title,
        color_discrete_sequence=COLOR_SEQUENCE,
    )

    fig.update_layout(
        template='plotly_white',
        height=500,
        margin=dict(l=40, r=40, t=60, b=40),
        font=dict(family="Arial, sans-serif", size=12),
    )

    return fig

def create_heatmap(df, x_col, y_col, z_col, title):
    """Create a heatmap"""
    pivot_df = df.pivot(index=y_col, columns=x_col, values=z_col)

    fig = go.Figure(data=go.Heatmap(
        z=pivot_df.values,
        x=pivot_df.columns,
        y=pivot_df.index,
        colorscale='Blues',
        text=pivot_df.values,
        texttemplate='%{text}',
        textfont={"size": 10},
        hovertemplate='<b>%{x}</b><br>%{y}<br>Value: %{z}<extra></extra>'
    ))

    fig.update_layout(
        title=title,
        template='plotly_white',
        height=max(400, len(pivot_df.index) * 30),
        margin=dict(l=150, r=40, t=60, b=100),
        font=dict(family="Arial, sans-serif", size=12),
        xaxis=dict(side='bottom'),
    )

    return fig

def create_treemap(df, path_cols, values_col, title):
    """Create a treemap for hierarchical data"""
    fig = px.treemap(
        df,
        path=path_cols,
        values=values_col,
        title=title,
        color=values_col,
        color_continuous_scale='Blues',
    )

    fig.update_layout(
        template='plotly_white',
        height=500,
        margin=dict(l=40, r=40, t=60, b=40),
        font=dict(family="Arial, sans-serif", size=12),
    )

    return fig
