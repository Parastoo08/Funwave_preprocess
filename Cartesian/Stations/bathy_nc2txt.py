# Bathy
# This code is to convert and interpolate bathymetry data from netcdf format to funwave input format
# It is in cartesian coordinates So projection has been done!
# load library
import netCDF4
import numpy as np
import scipy.interpolate as sp
from pyproj import Proj
import matplotlib.pylab as pl

# Read data
data = netCDF4.Dataset('gebco_2021_n42.0_s34.0_w20.0_e30.0.nc')
lat = data.variables['lat'][:]
lon = data.variables['lon'][:]
z1 = data.variables['elevation'][:]
data.close()

 #figure in lat lon
#pl.pcolor(lon,lat,z1,shading='nearest')
#pl.colorbar()

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

[x1,y1] = np.meshgrid(lon,lat)
del lon, lat
Ys=40.23
Xs=25.15
## from wgs84 to utm
p = Proj(proj='utm', zone=34, ellps='WGS84') # verify UTM ZONE !!!!
xn,yn = p(x1,y1)
del x1, y1
Xs1,Ys1=p(Xs,Ys)
## figure in cartesian
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

# maximum elevation to 500 m above msl, for fill nan value
eta[np.isnan(eta)] = 1000
#eta[eta>500] = 500

#eta1 = eta*-1

pl.pcolor(x0,y0,eta,shading='nearest')
pl.colorbar()

f = open('bathy.txt','w')
np.savetxt(f, eta, "%.3f ")
f.close()

print("For model FUNWAVE\n")
print("x = %0.2f \ny = %0.2f \ndx = %0.2f \ndy = %0.2f\n" % (xmin,ymin,x0[1]-x0[0],y0[1]-y0[0]))
