# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 12:46:09 2019

@author: Veda
"""

import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.palettes import Spectral5
from bokeh.transform import factor_cmap
from bokeh.layouts import row
from bokeh.models import FactorRange
from bokeh.themes.theme import Theme
#from bokeh.plotting import Bar, output_file, show

output_file('Total Sales.html')

df = pd.read_excel(r"C:/Users/Veda/Downloads/Book1.xlsx")

#sales_data=df.groupby(df['Inv Date'].dt.month)['Sales Qty'].sum()
sales_data=df.groupby(df['Inv Date'].dt.strftime('%B'))['Sales Qty'].sum().to_frame().reset_index()
#sales_data1=df.sort_values(by='Inv Date', ascending= False)
grouped = sales_data / 1000
print(grouped)
sales_data.sort_values(by=['Inv Date'])
source = ColumnDataSource(pd.DataFrame(grouped))
states = source.data['Inv Date'].tolist()

p = figure(x_range=states, plot_width=300, plot_height=300)

color_map = factor_cmap(field_name='Inv Date',
                    palette=Spectral5, factors=states)
p.vbar(x='Inv Date',top='Sales Qty', source=source, width=0.70, color=color_map)
p.x_range = FactorRange(factors=df['states'].tolist())

p.title.text ='Total Sales'
p.title.align = 'center'
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

hover = HoverTool(tooltips=[("sales","@Sales%20Qty,")],mode='vline')
p.add_tools(hover)
show(p)
