
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

data = {
    'Month': ['jan', 'feb', 'march', 'april', 'may', 'june',
              'july', 'aug', 'sep', 'oct', 'nov', 'dec'],
    'sales': [120, 150, 170, 160, 180, 200,
              210, 230, 220, 240, 250, 270],
    'profit': [30, 40, 45, 42, 50, 55,
               60, 65, 63, 70, 75, 80],
    'region': ['East', 'West', 'North', 'South',
               'East', 'West', 'North', 'South',
               'East', 'West', 'North', 'South']
}

df = pd.DataFrame(data)

print(df)

# Line chart
line_fig = px.line(
    df, x='Month', y='sales',
    title='Monthly Sales Trend',
    markers=True
)

# Bar chart
bar_fig = px.bar(
    df, x='Month', y='profit',
    color='region',
    title='Monthly Profit by Region'
)

# Scatter plot
scatter_fig = px.scatter(
    df, x='sales', y='profit',
    color='region',
    size='profit',
    hover_data=['Month'],
    title='Sales vs Profit'
)

# Create Dash application
app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            children='Sales Dashboard',
            style={'textAlign': 'center'}
        ),
        dcc.Graph(id='line-chart', figure=line_fig),
        dcc.Graph(id='bar-chart', figure=bar_fig),
        dcc.Graph(id='scatter-chart', figure=scatter_fig)
    ]
)

if __name__ == '__main__':
    app.run(debug=True)
