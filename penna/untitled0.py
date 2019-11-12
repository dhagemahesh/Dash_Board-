# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 22:55:40 2019

@author: Veda
"""

from math import pi
import pandas as pd
from bokeh.io import output_file, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.plotting import figure

output_file("pie.html")
df = pd.read_excel(r"C:/Users/Veda/Downloads/Book1.xlsx")

sales_data = df.groupby(['Grade Description','Region Description'])['Sales Qty'].sum()
print(sales_data)
data=[row for row in sales_data]
labels = ['OPC43','OPC53','PPC','PSC']
values = [data[0],data[1],data[2],data[3]]
source = ColumnDataSource(data=dict(
    start=['labels',0.2], end=['values',2*pi]))
states = source.data['Grade Description'].tolist()
p = figure()
p.wedge(x=0, y=0,start_angle='start', end_angle='end', radius=1,
         alpha=0.6, source=source)
def update(source=source, window=None):
    data = source.data
    #data['end'][0] = slider.value
    source.trigger('change')

#slider.js_on_change('value', CustomJS.from_py_func(update))

show(p)


