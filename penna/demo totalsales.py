# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 00:17:41 2019

@author: Veda
"""

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import plotly
import plotly.offline as py
import plotly.graph_objs as go
fichier_html_graphs=open("TEST.html",'w')
fichier_html_graphs.write("<html><head></head><body>"+"\n")
sd = pd.read_excel(r"C:/Users/Veda/Downloads/Book1.xlsx")
print(sd.columns)
print(sd[['Inv Date','Sales Qty']])

#sales_data=sd.groupby(sd['Inv Date'].dt.strftime('%B'))['Sales Qty'].sum()
#sales_data=sd.groupby(pd.Grouper(key='Inv Date', freq='1M')).sum()
sales_data=sd.groupby(sd['Inv Date'].dt.month)['Sales Qty'].sum()
sd=sales_data/1000
print("RK",sd)

color1 = '#00bfff'
trace1 = go.Bar(
    x=['January','February','March','April'],
    y=[row for row in sd],
    hoverinfo="y",
    name='Actual',
    marker=dict(
            color=color1
    )
)
data=[trace1]
layout = go.Layout(
    margin=go.layout.Margin(l=100,r=100,b=1,t=50),
    autosize=True,
    title="Total Sales",
    titlefont=dict(
        family='Courier New, monospace',
        size=20
       
    ),
    paper_bgcolor='rgb(204,229,255)',
    plot_bgcolor='rgb(204,229,255)'
)
fig = go.Figure(data=data, layout=layout)
#fig.update_xaxes(zeroline=False)
#fig.update_yaxes(hoverformat=".2f")
plotly.offline.plot(fig, filename='chart_'+str(1)+'.html',auto_open=False)
fichier_html_graphs.write("  <object data=\""+'chart_'+str(1)+'.html'+"\" width=\"310\" height=\"300\"></object>"+"\n")
fichier_html_graphs.write("</body></html>")
print("CHECK YOUR DASHBOARD.html In the current directory")
