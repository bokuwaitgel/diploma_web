# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc

# Define the navbar structure
def Navbar():

    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                #drop down menu
                # dbc.NavItem(dbc.NavLink("SARIMA", href="/sarima")),
                # dbc.NavItem(dbc.NavLink("LSTM", href="/lstm")),
                # dbc.NavItem(dbc.NavLink("Exponential Smoothing", href="/exp")),
                # dbc.NavItem(dbc.NavLink("Fusion", href="/fusion")),
                dbc.NavItem(dbc.NavLink("Exponential Smoothing", href="/exp_new")),
                dbc.NavItem(dbc.NavLink("LSTM", href="/lstm_new")),
            ] ,
            brand="Time series forecasting",
            brand_href="/",
            color="dark",
            dark=True,
        ), 
    ])

    return layout