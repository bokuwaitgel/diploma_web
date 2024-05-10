# Import necessary libraries 
from dash import html, dcc, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output

# Define the page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("Exponential Smoothing")),
        html.Br(),
        html.Hr(),
        html.H1(children='Coming soon', style={'textAlign':'Center'}),

    ], style={'margin-top': '25px'})
])
