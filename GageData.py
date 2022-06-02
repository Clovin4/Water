import dash
from dash import Dash, dcc, html, Input, Output
import glob
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

app = Dash(__name__)

# Dataframe
xl_us = pd.read_csv("gageData_us.csv")
xl_ds = pd.read_csv("gageData_ds.csv")
df = pd.DataFrame(xl_us)
df_temp = pd.DataFrame(xl_ds)
df = df.append(df_temp)
df = df.rename(columns={'agency_cd': 'agency', 'X_00060_00000': 'Flow_Inst', 'X_00065_00000': 'Gage_Height'})
df = df.drop(["Unnamed: 0", "X_00060_00000_cd", "tz_cd", "X_00065_00000_cd"], axis=1)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

fig1 = px.line(df, x="dateTime", y="Gage_Height", color="site_no")
fig2 = px.line(df, x="dateTime", y="Flow_Inst", color="site_no")

# Data for the tip-graph

app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: A web application framework for Python.
        '''),

        dcc.Dropdown(
            

        ),

        dcc.Graph(
            id='graph1',
            figure=fig1
        ),  
    ]),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: A web application framework for Python.
        '''),

        dcc.Graph(
            id='graph2',
            figure=fig2
        ),  
    ]),
])

@app.callback(
    Output('graph2', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)