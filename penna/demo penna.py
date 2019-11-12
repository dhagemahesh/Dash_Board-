# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:44:24 2019

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

output_file('Total Sales.html')

df = pd.read_excel(r"C:/Users/Veda/Downloads/Book1.xlsx")

#sales_data=df.groupby(df['Inv Date'].dt.month)['Sales Qty'].sum()
sales_data = (df.groupby('Inv Date')
                            .sum()
                            .loc[:,['Sales Qty']]
                            .sort_values('Inv Date'))
sales_data=df.groupby(df['Inv Date'].dt.strftime('%B')).sum().loc[:,['Sales Qty']].sort_values('Sales Qty', reverse=True)
#sales_data1=df.sort_values(by='Inv Date', ascending= False)
grouped = sales_data/ 1000

print(grouped)
s=grouped.sort_values()
print(s)
source = ColumnDataSource(pd.DataFrame(grouped))
states = source.data['Inv Date'].tolist()
p = figure(x_range=states, plot_width=250, plot_height=200)

color_map = factor_cmap(field_name='Inv Date',
                    palette=Spectral5, factors=states)
p.vbar(x='Inv Date',top='Sales Qty', source=source, width=0.70, color=color_map)


p.title.text ='Total Sales'
p.title.align = 'center'
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

p1 = figure(x_range=states, plot_width=250, plot_height=200)

color_map = factor_cmap(field_name='Inv Date',
                    palette=Spectral5, factors=states)
p1.vbar(x='Inv Date',top='Sales Qty', source=source, width=0.70, color=color_map)


p1.title.text ='Realization'
p1.title.align = 'center'
p1.xgrid.grid_line_color = None
p1.ygrid.grid_line_color = None

p2 = figure(x_range=states, plot_width=250, plot_height=200)

color_map = factor_cmap(field_name='Inv Date',
                    palette=Spectral5, factors=states)
p2.vbar(x='Inv Date',top='Sales Qty', source=source, width=0.70, color=color_map)


p2.title.text ='Collections'
p2.title.align = 'center'
p2.xgrid.grid_line_color = None
p2.ygrid.grid_line_color = None

p3 = figure(x_range=states, plot_width=250, plot_height=200)

color_map = factor_cmap(field_name='Inv Date',
                    palette=Spectral5, factors=states)
p3.vbar(x='Inv Date',top='Sales Qty', source=source, width=0.70, color=color_map)


p3.title.text ='Over Due'
p3.title.align = 'center'
p3.xgrid.grid_line_color = None
p3.ygrid.grid_line_color = None

layout=row(p,p1,p2,p3)
hover = HoverTool(tooltips=[("sales","@Sales%20Qty,")],mode='vline')
#layout.add_tools(hover)
show(layout)
