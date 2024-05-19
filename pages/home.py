# Import necessary libraries 
import dash
from dash import html
import dash_bootstrap_components as dbc

#Define the page layout

#home page is about system information and loss function
layout = dbc.Container([
    dbc.Row([
        html.Hr(),
        #system information header
        html.H3("Үндсэн бүтэц"),
        html.Center(children=[
        #system information image from images folder
        html.Img(src='/assets/image.png', style={'height':'100%', 'width':'100%'})]),
        html.Br(),
        html.Hr(),
        html.H3("Горимын бүтэц"),
        html.Img(src='/assets/model.png', style={'height':'100%', 'width':'100%'}),
    ])
])