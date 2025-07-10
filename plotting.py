import plotly.graph_objects as go

def plot_simulation(df):
    fig = go.Figure()
    for col in df.columns[:100]:  # Limit for clarity
        fig.add_trace(go.Scatter(y=df[col], mode='lines', line=dict(width=1), opacity=0.2))
    fig.update_layout(
        title="Retirement Monte Carlo Simulation",
        xaxis_title="Years After Retirement",
        yaxis_title="Portfolio Value",
        template="plotly_dark"
    )
    return fig.to_html(full_html=False)
