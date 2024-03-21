import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load your data
bias_data = pd.read_csv('allsides_bias_data.csv')
if 'Total' not in bias_data.columns:
    bias_data['Total'] = bias_data['agree'] + bias_data['disagree']

# Read the data for both wars and drop NaN values instead of filling them
israel_hamas_data = pd.read_csv('article_data.csv').dropna()
ukraine_russia_data = pd.read_csv('ukraine_war_article_data.csv').dropna()

israel_hamas_data = israel_hamas_data.dropna(subset=['Date'])
ukraine_russia_data = ukraine_russia_data.dropna(subset=['Date'])

# Convert 'Date' columns to datetime objects
israel_hamas_data['Date'] = pd.to_datetime(israel_hamas_data['Date'], errors='coerce')
ukraine_russia_data['Date'] = pd.to_datetime(ukraine_russia_data['Date'], errors='coerce')

israel_hamas_data = israel_hamas_data[israel_hamas_data['Date'] >= '2016-01-01']
ukraine_russia_data = ukraine_russia_data[ukraine_russia_data['Date'] >= '2016-01-01']

# Group by Date and Bias Rating, and count the number of articles
israel_hamas_agg = israel_hamas_data.groupby([israel_hamas_data['Date'].dt.to_period('M'), 'Bias Rating']).size().unstack()
ukraine_russia_agg = ukraine_russia_data.groupby([ukraine_russia_data['Date'].dt.to_period('M'), 'Bias Rating']).size().unstack()

# Keep only left, right, and center bias ratings
israel_hamas_agg = israel_hamas_agg[['left', 'right', 'center']]
ukraine_russia_agg = ukraine_russia_agg[['left', 'right', 'center']]

# Initialize Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)  # Suppress callback exceptions

# App layout with tabs
app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label="Bias and Public Opinion", value='tab-1', children=[
            html.H1('News Source Bias and Public Opinion'),
            html.Div('Bubble chart representing the agree vs. disagree counts for each news source.'),
            dcc.Graph(
                figure=px.scatter(
                    bias_data, x='agree', y='disagree', size='Total', color='news_source',
                    hover_name='news_source', size_max=60
                )
            )
        ]),
        dcc.Tab(label='International Events', value='tab-2')
    ]),
    html.Div(id='tab-content')
])

@app.callback(
    Output('tab-content', 'children'),
    [Input('tabs', 'value')]
)
def render_content(tab):
    if tab == 'tab-2':
        return html.Div([
            dcc.Tabs(id='subtabs', children=[
                dcc.Tab(label='Israel-Hamas War', value='israel-hamas'),
                dcc.Tab(label='Ukraine-Russia War', value='ukraine-russia')
            ]),
            html.Div(id='subtab-content')
        ])
    elif tab == 'tab-1':
        # Since we're directly setting the figure in the layout, we don't need to update it here
        return dash.no_update
    return dash.no_update

@app.callback(
    Output('subtab-content', 'children'),
    [Input('subtabs', 'value')]
)
def render_subtab_content(subtab):
    if subtab == 'israel-hamas':
        # israel_hamas_agg.index = israel_hamas_agg.index.to_timestamp()
        if isinstance(israel_hamas_agg.index, pd.PeriodIndex):
            israel_hamas_agg.index = israel_hamas_agg.index.to_timestamp()
        fig = px.area(
            israel_hamas_agg, x=israel_hamas_agg.index, y=israel_hamas_agg.columns,
            title='Articles Count by Bias Rating'
        )
        return dcc.Graph(figure=fig)
    elif subtab == 'ukraine-russia':
        # ukraine_russia_agg.index = ukraine_russia_agg.index.to_timestamp()
        if isinstance(ukraine_russia_agg.index, pd.PeriodIndex):
            ukraine_russia_agg.index = ukraine_russia_agg.index.to_timestamp()
        fig = px.area(
            ukraine_russia_agg, x=ukraine_russia_agg.index, y=ukraine_russia_agg.columns,
            title='Articles Count by Bias Rating'
        )
        return dcc.Graph(figure=fig)
    return dash.no_update  # No content for other subtabs

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
