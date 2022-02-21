# This code convert bathymetry data from netcdf format to funwave input format
# It is for spherical coordinate
# load library
import netCDF4
import numpy as np
import scipy.interpolate as sp
import matplotlib.pylab as pl

#Read data
data = netCDF4.Dataset('gebco_2021_n42.0_s34.0_w20.0_e30.0.nc') #data
lat = data.variables['lat'][:]
lon = data.variables['lon'][:]
z1 = data.variables['elevation'][:]
data.close()

## figure in lat lon
pl.figure()
pl.pcolor(lon,lat,z1,shading='nearest')
pl.colorbar()

n = len(lat)
m = len(lon)
z = np.reshape(z1,(n*m))
z  = np.array(z)
z1  = np.array(z1)

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

#interpolate

eta  = sp.griddata((xn,yn),z,(xi,yi),'linear')

#eta1 = eta*-1

pl.figure()
pl.pcolor(x,y,eta,shading='nearest')
pl.colorbar()

#Save in .txt format
f = open('bathy.txt','w') 
np.savetxt(f, eta, "%.3f ")
f.close()

#What is the cell number to input funwave
print("For model FUNWAVE\n")
print("x = %0.2f \ny = %0.2f \ndx = %0.3f \ndy = %0.3f\n" % (x[0],y[0],x[1]-x[0],y[1]-y[0]))
