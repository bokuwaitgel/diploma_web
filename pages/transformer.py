# Import necessary libraries 
from dash import html, dcc, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output

#local data
from data import fusion

# get data
df_main, df_pred = fusion.get_data('0','Jingtang Australia EXW')

#get columns
column = list(df_main.columns)

#remove Date from columns
column.remove('Date')

# Define the page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("Fusion Model")),
        html.Br(),
        html.Hr(),
        html.H3(children='HCC Нүүрсний үнийн таамаглал', style={'textAlign':'Left'}),
        html.H5(children='Төрөл'),
        dcc.Dropdown(column, 'Jingtang Australia EXW', id='dropdown-selection'),
        dcc.Graph(id='graph-content-fusion')
        
    ], style={'margin-top': '25px'})

])

@callback(
    Output('graph-content-fusion', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    #get column index by value
    index = column.index(value)
    
    test = df_main.iloc[-100:]
    pred = fusion.get_pred(str(index), value)
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

    return fig