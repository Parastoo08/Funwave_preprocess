# -*- coding: utf-8 -*-
"""
initial
"""

# load library
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as pl
import scipy.interpolate as sp
from pyproj import Proj

# import data
file1 = 'raster100.nc'
data = Dataset(file1)
lat = data.variables['latitude'][:]
lon = data.variables['longitude'][:]
z1 = data.variables['layer'][:]
data.close()

n = len(lat)
m = len(lon)

pl.pcolor(lon,lat,z1,shading='nearest')
pl.colorbar()

z = np.reshape(z1,(n*m))
z  = np.array(z)

y  = np.arange(22.5,26.004,0.002)
x  = np.arange(57,67.504,0.004)
n1 = len(y)
m1 = len(x)

[x1,y1] = np.meshgrid(lon,lat)
del lon, lat

## from wgs84 to utm
p = Proj(proj='utm', zone=34, ellps='WGS84') # verify UTM ZONE !!!!
xn,yn = p(x1,y1)
del x1, y1

pl.pcolor(xn,yn,z1,shading='nearest')
pl.colorbar()

xn = np.array(xn)
yn = np.array(yn)

xn = np.reshape(xn,(n*m))
yn = np.reshape(yn,(n*m))

xmin,ymin = p(x[0],y[0])
xmax,ymax = p(x[-1],y[-1])

x0 = np.linspace(xmin,xmax,m1)
y0 = np.linspace(ymin,ymax,n1)

xi,yi = np.meshgrid(x0,y0)

eta  = sp.griddata((xn,yn),z,(xi,yi),'linear')

## fill nan value to 0
eta[np.isnan(eta)] = 0

#pl.pcolor(x0,y0,eta,shading='nearest')
#pl.colorbar()

f = open('eta.txt','w')
np.savetxt(f, eta, "%12.3E ")
f.close()

print("For model FUNWAVE\n")
print("x = %0.2f \ny = %0.2f \ndx = %0.2f \ndy = %0.2f\n" % (xmin,ymin,x0[1]-x0[0],y0[1]-y0[0]))
