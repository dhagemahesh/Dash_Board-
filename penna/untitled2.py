# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:18:27 2019

@author: Veda
"""

import numpy as np
import pandas as pd
from bokeh.models import ColumnDataSource, Plot, LinearAxis, Grid
from bokeh.models.tools import HoverTool
from bokeh.palettes import Spectral5
from bokeh.transform import factor_cmap
from bokeh.plotting import figure, output_file, show
from bokeh.io import curdoc, show
output_file('Naked Realization by state.html')
df=pd.read_excel("C:/Users/Veda/Downloads/Book1.xlsx")
grouped=df.groupby(['Region Description'])['Naked Realization(Rs'].sum()
grouped=(grouped)/10000000
source = ColumnDataSource(pd.DataFrame(grouped))
states = source.data['Region Description'].tolist()
p = figure(y_range=states)
color_map = factor_cmap(field_name='Region Description',
                    palette=Spectral5, factors=states)

p.hbar(y='Region Description',source=source,right="Naked Realization(Rs",left=0,height=0.5, color="#FFFF99")

p.title.text ='Naked Realization by state'
p.xaxis.axis_label = 'Naked Realization in Rs'
p.yaxis.axis_label = 'state'
hover = HoverTool()
hover.tooltips = [
    ("Totals","@Naked Realization(Rs")]

hover.mode = 'hline'

p.add_tools(hover)

show(p)
file:///C:/Users/Veda/Downloads/Book1.xlsx