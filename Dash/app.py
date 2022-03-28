from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

app = Dash(name=__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(['LA', 'NYC', 'MTL'],
        'LA',
        id='dropdown'
    ),
    html.Div(id='display-value')
])


@app.callback(Output('display-value', 'children'),
                [Input('dropdown', 'value')])
def display_value(value):
    return f'You have selected {value}'


if __name__ == '__main__':
    app.run_server(debug=True)