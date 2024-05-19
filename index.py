# Import necessary libraries 
from dash import html, dcc
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app

# Connect to your app pages
from pages import home, sarima, lstm, exp, transformer, prophet

# Connect the navbar to the index
from components import navbar

# Define the navbar
nav = navbar.Navbar()

# Define the index page layout and dark mode
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav, 
    html.Div(id='page-content', children=[]), 
], style={'color': '#000000', 'height': '100vh'})

# Create the callback to handle mutlipage inputs
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home.layout
    if pathname == '/sarima':
        return sarima.layout
    if pathname == '/lstm':
        return lstm.layout
    if pathname == '/exp':
        return exp.layout
    if pathname == '/fusion':
        return transformer.layout
    if pathname == '/prophet':
        return prophet.layout
    else: # if redirected to unknown link
        return "404 Page Error! Please choose a link"

# Run the app on localhost:8050
if __name__ == '__main__':
    app.run_server(host="0.0.0.0",debug=True)
    #debug
    # app.run_server(debug=True) 