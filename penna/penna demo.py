# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 22:41:49 2019

@author: Veda
"""
from math import pi
import numpy as np
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Plot, LinearAxis, Grid
from bokeh.models.tools import HoverTool
from bokeh.palettes import Spectral5
from bokeh.transform import factor_cmap
from bokeh.layouts import row,column
from bokeh.io import *
from bokeh.layouts import *
from bokeh.plotting import *
from bokeh.models.widgets import *
from bokeh.models.widgets import MultiSelect
from bokeh.layouts import widgetbox
from bokeh.layouts import gridplot
output_file("dropdown.html")
df = pd.read_excel(r"C:/Users/Veda/Downloads/Book1.xlsx")
menu = [("TELANGANA", "item_1"), ("ANDHRA PRADESH", "item_2")]
dropdown = Dropdown(label="REGION/STATE", button_type="default", width=130, menu=menu)

menu1 = [("KARIMNAGAR", "item_1"), ("MAHABUBNAGAR", "item_2")]
dropdown1 = Dropdown(label="DISTRICTS", button_type="default", width=123
                    , menu=menu1)

bt = Button(label="MTD", button_type="default", width=48)
bt1 = Button(label="QTD", button_type="default", width=48)
bt2 = Button(label="YTD", button_type="default", width=48)
bt3 = Button(label="CUSTOM", button_type="default", width=85)

menu2 = [("Trade", "item_1"), ("Non-Trade", "item_2")]
dropdown2 = Dropdown(label="CUSTOMER TYPE", button_type="default", menu=menu2,width=144)

menu3 = [("OPC53", "item_1"), ("OPC43", "item_2"),("PPC", "item_3"),("PSC", "item_4")]
dropdown3 = Dropdown(label="PRODUCT GRADE", button_type="default", menu=menu3, width=140)

menu4 = [None]
dropdown4 = Dropdown(label="OFFICER LEVEL", button_type="default", menu=menu4, width=140)

menu5 = [("Bulk", "item_1"), ("Bag", "item_2")]
dropdown5 = Dropdown(label="PACKING TYPE", button_type="default", menu=menu5,width=140
                    )

bt8 = Button(label="DEFAULT/RESET", button_type="default",width=140)    


layout=layout(column(row(dropdown,dropdown1,bt, bt1, bt2, bt3, dropdown2,dropdown3, dropdown4,dropdown5, bt8)))
#show(layout)



sales_data=df.groupby(df['Inv Date'].dt.strftime('%B'))['Sales Qty'].sum().sort_values()
#sales_data1=df.sort_values(by='Inv Date', ascending= False)
grouped = sales_data/ 1000
print(grouped)

source = ColumnDataSource(pd.DataFrame(grouped))
states = source.data['Inv Date'].tolist()
p = figure(x_range=states, plot_width=250, plot_height=200)

color_map = factor_cmap(field_name='Inv Date',
                    palette=Spectral5, factors=states)
p.vbar(x='Inv Date',top='Sales Qty', source=source, width=0.70,color="#FFFF99")


p.title.text ='Total Sales'
p.title.align = 'center'
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.yaxis.visible = False
p.xaxis.visible=True
p.outline_line_width = 7
p.outline_line_alpha = 0.3
p.outline_line_color = "#E5FFCC"

p1 = figure(x_range=states, plot_width=250, plot_height=200)

color_map = factor_cmap(field_name='Inv Date',
                    palette=Spectral5, factors=states)
p1.vbar(x='Inv Date',top='Sales Qty', source=source, width=0.70,color="#FFCC99")


p1.title.text ='Realization'
p1.title.align = 'center'
p1.xgrid.grid_line_color = None
p1.ygrid.grid_line_color = None
p1.yaxis.visible = False
p1.xaxis.visible=True
p1.outline_line_width = 7
p1.outline_line_alpha = 0.3
p1.outline_line_color = "#E5FFCC"

p2 = figure(x_range=states, plot_width=250, plot_height=200)

color_map = factor_cmap(field_name='Inv Date',
                    palette=Spectral5, factors=states)
p2.vbar(x='Inv Date',top='Sales Qty', source=source, width=0.70,color="#CCFFCC")


p2.title.text ='Collections'
p2.title.align = 'center'
p2.xgrid.grid_line_color = None
p2.ygrid.grid_line_color = None
p2.yaxis.visible = False
p2.xaxis.visible=True
p2.outline_line_width = 7
p2.outline_line_alpha = 0.3
p2.outline_line_color = "#E5FFCC"
p3 = figure(x_range=states, plot_width=250, plot_height=200)

color_map = factor_cmap(field_name='Inv Date',
                    palette=Spectral5, factors=states)
p3.vbar(x='Inv Date',top='Sales Qty', source=source, width=0.70,color="#CCE5FF")


p3.title.text ='Over Due'
p3.title.align = 'center'
p3.xgrid.grid_line_color = None
p3.ygrid.grid_line_color = None
p3.yaxis.visible = False
p3.xaxis.visible=True
p3.outline_line_width = 7
p3.outline_line_alpha = 0.3
p3.outline_line_color = "#E5FFCC"

grouped=df.groupby(['Region Description'])['Naked Realization(Rs'].sum()
grouped=(grouped)/10000000
source = ColumnDataSource(pd.DataFrame(grouped))
states = source.data['Region Description'].tolist()
p5 = figure(y_range=states,plot_width=300, plot_height=300)
color_map = factor_cmap(field_name='Region Description',
                    palette=Spectral5, factors=states)

p5.hbar(y='Region Description',source=source,right="Naked Realization(Rs",left=0,height=0.5, color="#FFFF99")

p5.title.text ='Naked Realization by state'
p5.title.align = 'center'
p5.xgrid.grid_line_color = None
p5.ygrid.grid_line_color = None
p5.xaxis.visible=False
p5.outline_line_width = 7
p5.outline_line_alpha = 0.3
p5.outline_line_color = "#E5FFCC"
hover = HoverTool()
hover.tooltips = [
    ("Totals","@Naked Realization(Rs")]

hover.mode = 'hline'

p5.add_tools(hover)
sales_data = df.groupby(['Grade Description','Region Description'])['Sales Qty'].sum()
print(sales_data)
data=[row for row in sales_data]
labels = ['OPC43','OPC53','PPC','PSC']
values = [data[0],data[1],data[2],data[3]]
source = ColumnDataSource(data=dict(
    start=['labels',0], end=['values',2*pi]))
#states = source.data['Grade Description'].tolist()
p6 = figure(plot_width=180, plot_height=180)
p6.wedge(x=0, y=0,start_angle='start', end_angle='end', radius=1,
         alpha=0.6, source=source)
def update(source=source, window=None):
    data = source.data
    #data['end'][0] = slider.value
    source.trigger('change')
p6.title.text ='Product Mix'
p6.title.align = 'center'
p6.xgrid.grid_line_color = None
p6.ygrid.grid_line_color = None
p6.outline_line_width = 7
p6.outline_line_alpha = 0.3
p6.yaxis.visible = False
p6.xaxis.visible=False
p6.outline_line_color = "#E5FFCC"

hover = HoverTool(tooltips=[("sales","@Sales%20Qty,")],mode='vline')
#layout.add_tools(hover)

layout1= row (p,p1,p2,p3,p6)
layout2= column(layout,layout1,p5)

#curdoc().add_root(layout)
show(layout2)

