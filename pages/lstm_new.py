# Import necessary libraries 
from dash import html, dcc, callback,dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output

#local data
from data import lstm_new

# get data
df_main = lstm_new.get_main()
print(df_main)

#get columns
column =  [
           'Jinquan Mongolia 5# Washed Coking', 
           'Baotou Washed Primary Coking',
           'Wuhai Washed 1/3 Coking',
           'Ganqimaodu Thermal 6000',
           'Ordos Grade III Met. Coke',
           ]

res = [
    1627.0192,
    2062.4287,
    1699.2125,
    689.65436,
    1440.3883
]
#get df main last row as a list
last_row = df_main.iloc[-1].tolist()

before_res = [
    1565.0, 
    1951.5, 
    1673.525, 
    680.0, 
    1329.19
]


# Define the final page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("LSTM / Long Short-Term Memory")),
        html.Br(),
        html.Hr(),
        html.H3(children='HCC Нүүрсний үнийн таамаглал', style={'textAlign':'Left'}),
        html.H5(children='Төрөл'),
        html.Br(),
        html.Hr(),

        html.Div(id='before-output'),
        html.Div(id='next-output'),
        html.Div(id='dif-output'),
        html.Br(),
        html.Hr(),
        dcc.Dropdown(column, 'Jinquan Mongolia 5# Washed Coking', id='dropdown-selection'),
        dcc.Graph(id='graph-content-lstm_new')
    ], style={'margin-top': '25px'})
])

@callback(
    Output(component_id='before-output', component_property='children'),
    Input('dropdown-selection', 'value')
)

def update_output_div(value):
    return f'Before price: {before_res[column.index(value)]}'

@callback(
    Output(component_id='next-output', component_property='children'),
    Input('dropdown-selection', 'value')
)

def update_output_div(value):
    return f'Next price: {res[column.index(value)]}'


@callback(
    Output(component_id='dif-output', component_property='children'),
    Input('dropdown-selection', 'value')
)

def update_output_div(value):
    return f'dif price: {res[column.index(value)] - before_res[column.index(value)]}'

@callback(
    Output('graph-content-lstm_new', 'figure'),
    Input('dropdown-selection', 'value')
)

def update_graph(value):
    #get column index by value
    index = column.index(value)
    
    test = df_main.iloc[-50:]
    fig = go.Figure()
    
    # Add training data line plot
    fig.add_trace(go.Scatter(
        x=test['date'],
        y=test[value],
        mode='lines',
        name='Бодит өгөгдөл',
        line=dict(color='blue')
    ))


    fig.update_layout(
        title='test',
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