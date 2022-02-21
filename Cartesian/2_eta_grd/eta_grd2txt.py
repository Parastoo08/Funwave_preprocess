# -*- coding: utf-8 -*-
"""
initial
"""

# load library
import numpy as np
import matplotlib.pyplot as pl
import scipy.interpolate as sp
from pyproj import Proj
from leyendo_grd import read_grd

# import data
m, n, xmin, xmax, ymin, ymax, zmin, zmax, z = read_grd('surface1.grd')

z1 = np.reshape(z,(int(n),int(m)))

lon = np.linspace(xmin,xmax,m)
lat = np.linspace(ymin,ymax,n)

pl.pcolor(lon,lat,z1,shading='nearest')
pl.colorbar()

z  = np.array(z)

#Reshape based on resolution

y  = np.arange(35.5,40.5,0.004) #Resolution dx, dy
x  = np.arange(23.5,28.5,0.004)  

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

pl.pcolor(x0,y0,eta,shading='nearest')
pl.colorbar()

f = open('eta.txt','w')
np.savetxt(f, eta, "%12.3E ")
f.close()

print("For model FUNWAVE\n")
print("x = %0.2f \ny = %0.2f \ndx = %0.2f \ndy = %0.2f\n" % (xmin,ymin,x0[1]-x0[0],y0[1]-y0[0]))
