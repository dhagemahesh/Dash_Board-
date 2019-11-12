# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:34:41 2019

@author: Veda
"""

import geopandas as gpd

# File path
metro_fp = (r"C:/Users/Veda/Desktop/penna/IND_adm3.kml")

# Read the data
metro = gpd.read_file(metro_fp)

import geopandas as gpd
import fiona
#fiona.drvsupport.supported_drivers['kml'] = 'rw' # enable KML support which is disabled by default
#fiona.drvsupport.supported_drivers['KML'] = 'rw' # enable KML support which is disabled by default



fiona.drvsupport.supported_drivers['libkml'] = 'rw' # enable KML support which is disabled by default
fiona.drvsupport.supported_drivers['LIBKML'] = 'rw' # enable KML support which is disabled by default
df=gpd.read_file(r"C:/Users/Veda/Desktop/penna/IND_adm3.kml")
print(df)
