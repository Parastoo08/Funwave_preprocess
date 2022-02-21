# -*- coding: utf-8 -*-
"""
initial
"""

# load library
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as pl
import scipy.interpolate as sp

# import data
file1 = 'raster100.nc'
data = Dataset(file1)
lat = data.variables['latitude'][:]
lon = data.variables['longitude'][:]
z1 = data.variables['layer'][:]
data.close()

n = len(lat)
m = len(lon)

pl.figure()
pl.pcolor(lon,lat,z1,shading='nearest')
pl.colorbar()

z = np.reshape(z1,(n*m))
z  = np.array(z)

y  = np.arange(22.5,26.004,0.004) # for dx and dy, change here!!
x  = np.arange(57,67.504,0.004)
n1 = len(y)
m1 = len(x)

[xn,yn] = np.meshgrid(lon,lat)
del lon, lat

xn = np.array(xn)
yn = np.array(yn)

xn = np.reshape(xn,(n*m))
yn = np.reshape(yn,(n*m))

xi,yi = np.meshgrid(x,y)

eta  = sp.griddata((xn,yn),z,(xi,yi),'linear')

pl.figure()
pl.pcolor(x,y,eta,shading='nearest')
pl.colorbar()

f = open('eta.txt','w')
np.savetxt(f, eta, "%12.3E ")
f.close()

print("For model FUNWAVE\n")
print("x = %0.2f \ny = %0.2f \ndx = %0.3f \ndy = %0.3f\n" % (x[0],y[0],x[1]-x[0],y[1]-y[0]))
