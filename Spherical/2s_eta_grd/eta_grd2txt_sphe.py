# -*- coding: utf-8 -*-
"""
initial
"""
# This code is for converting .grd format to funwave input format 
# In this case for initial elevation
# It is in spherical coordinates
# load library
import numpy as np
import matplotlib.pyplot as pl
import scipy.interpolate as sp
from leyendo_grd import read_grd

# import data
m, n, xmin, xmax, ymin, ymax, zmin, zmax, z = read_grd('surface1.grd') 
# change your file, file in geographic!!

z1 = np.reshape(z,(int(n),int(m)))

lon = np.linspace(xmin,xmax,m)
lat = np.linspace(ymin,ymax,n)

pl.figure()
pl.pcolor(lon,lat,z1,shading='nearest')
pl.colorbar()

z  = np.array(z)

#Reshape based on resolution

y  = np.arange(35.5,40.5,0.004) #Resolution dx, dy
x  = np.arange(23.5,28.5,0.004)  
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

#Filling missing data

eta[np.isnan(eta)] = 0

pl.figure()
pl.pcolor(x,y,eta,shading='nearest')
pl.colorbar()

# save eta to funwave
f = open('eta.txt','w') 
np.savetxt(f, eta, "%12.3E ")
f.close()

print("For model FUNWAVE\n")
print("x = %0.2f \ny = %0.2f \ndx = %0.3f \ndy = %0.3f\n" % (x[0],y[0],x[1]-x[0],y[1]-y[0]))
