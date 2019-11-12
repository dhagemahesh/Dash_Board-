# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:56:35 2019

@author: Veda
"""

import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from pandas import ExcelWriter
from pandas import ExcelFile


df = pd.read_excel(r"C:/Users/Veda/Downloads/Yreal_OneDaySampleData.xlsx")
app=dash.Dash()

layout = html.Div([
    html.H1("Total Sales", style={"textAlign": "center"}),
    html.Div([html.Div([dcc.Dropdown(id='states',
                                     options=[{'label': i.title(), 'value': i} for i in df.columns.values[0:]],
                                     value="poultry")], className="six columns",
                       style={"width": "40%", "float": "right"}),
              
    dcc.Graph(id='my-graph'),

    # dcc.Link('Go to Source Code', href='{}/code'.format(app_name))
], className="container")


@app.callback(
    dash.dependencies.Output('my-graph', 'figure'),
    [dash.dependencies.Input('product-selected1', 'value'),
     dash.dependencies.Input('product-selected2', 'value')])
def update_graph(selected_product1, selected_product2):
    dff = df[(df[selected_product1] >= 2) & (df[selected_product2] >= 2)]
    trace1 = go.Bar(x=dff['state'], y=dff[selected_product1], name=selected_product1.title(), )
    trace2 = go.Bar(x=dff['state'], y=dff[selected_product2], name=selected_product2.title(), )

    return {
        'data': [trace1, trace2],
        'layout': go.Layout(title=f'State vs Export: {selected_product1.title()}, {selected_product2.title()}',
                            colorway=["#EF963B", "#EF533B"], hovermode="closest",
                            xaxis={'title': "State", 'titlefont': {'color': 'black', 'size': 14},
                                   'tickfont': {'size': 9, 'color': 'black'}},
                            yaxis={'title': "Export price (million USD)", 'titlefont': {'color': 'black', 'size': 14, },
                                   'tickfont': {'color': 'black'}})}