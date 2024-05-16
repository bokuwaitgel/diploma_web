# Import necessary libraries 
from dash import html, dcc, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output

#local data
from data import exp

# get data
df_main, df_pred = exp.get_data('0')

#get columns
column = list(df_main.columns)

#remove Date from columns
column.remove('Date')

# Define the page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("Exponential Smoothing")),
        html.Br(),
        html.Hr(),
        html.H3(children='HHC Нүүрсний үнийн таамаглал', style={'textAlign':'Left'}),
        html.H5(children='Төрөл'),
        dcc.Dropdown(column, 'Jingtang Australia EXW', id='dropdown-selection'),
        dcc.Graph(id='graph-content-exp')

    ], style={'margin-top': '25px'})
])

@callback(
    Output('graph-content-exp', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    #get column index by value
    index = column.index(value)
    
    test = df_main.iloc[-100:]
    pred = exp.get_pred(str(index))
    fig = go.Figure()
    
    # Add training data line plot
    fig.add_trace(go.Scatter(
        x=test['Date'],
        y=test[value],
        mode='lines',
        name='Бодит өгөгдөл',
        line=dict(color='blue')
    ))

    # Add predictions line plot
    fig.add_trace(go.Scatter(
        x=pred['Date'],
        y=pred[value],
        mode='lines',
        name='Таамаглал',
        line=dict(color='green')
    ))

    fig.update_layout(
        title="Бодит өгөгдөл VS Таамаглал",
        xaxis_title="Он сар",
        yaxis_title=value,
        legend_title="Өгөгдөл",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        ),
        height=600
    )
    return fig
