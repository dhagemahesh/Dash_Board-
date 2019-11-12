# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:07:12 2019

@author: Veda
"""

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import plotly
import plotly.offline as py
import plotly.graph_objs as go
sd = pd.read_excel(r"C:/Users/Veda/Desktop/penna/Raw_data.xlsx")
print(sd.columns)
print(sd[['Grade Description','Sales Qty']])
sales_data = sd.groupby(['Grade Description'])['Sales Qty'].sum()
print("RK",sales_data)
data=[row for row in sales_data]
print("RK",data[0],data[1],data[2],data[3])
labels = ['OPC43','OPC53','PPC','PSC']
values = [data[0],data[1],data[2],data[3]]

fig = go.Figure(data=[go.Pie(labels=labels, values=values,direction="clockwise")])
fig.show()