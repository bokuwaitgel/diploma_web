# Import necessary libraries 
from dash import html, dcc, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output

#local data
from data import exp_new

# get data
df_main, df_pred = exp_new.get_data('0')

#get columns
column =  [
           'Jinquan Mongolia 5# Washed Coking', 
           'Baotou Washed Primary Coking',
           'Wuhai Washed 1/3 Coking',
           'Ganqimaodu Thermal 6000',
           'Ordos Grade III Met. Coke',
           ]

#remove Date from columns
# column.remove('Date')

# Define the page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("Exponential Smoothing")),
        html.Br(),
        html.Hr(),
        html.H3(children='HCC Нүүрсний үнийн таамаглал', style={'textAlign':'Left'}),
        html.H5(children='Төрөл'),
        dcc.Dropdown(column, 'Jinquan Mongolia 5# Washed Coking', id='dropdown-selection'),       
        html.Br(),
        html.Hr(),
        dcc.Graph(id='graph-content-exp_new')

    ], style={'margin-top': '25px'})
])

@callback(
    Output('graph-content-exp_new', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    #get column index by value
    index = column.index(value)
    test = df_main.iloc[-60:]
    pred = exp_new.get_pred(str(index))
    fig = go.Figure()
    
    # Add training data line plot
    fig.add_trace(go.Scatter(
        x=test['date'],
        y=test[value],
        mode='lines',
        name='Бодит өгөгдөл',
        line=dict(color='blue')
    ))

    # Add predictions line plot
    fig.add_trace(go.Scatter(
        x=pred['date'],
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
