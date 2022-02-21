# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:53:44 2020

@author: paras
"""

# load library
import numpy as np
from matplotlib.pylab import where

# import data
d=np.loadtxt('bathypositive.txt')
n,m = d.shape
#list = [50,25]
#for i in list:
px, py = where((d<=5) & (d>=0)) 
cx=np.array([px,py])
np.savetxt('cx0.csv', cx, delimiter=',')
 
 #del  px, py, cx
#del i

#heigh=d[1683,2853],d[1234,1906],d[1108,1558],d[984,1243],d[1204,2029],\
#d[1161,1714],d[256,600],d[1211,1814],d[1068,2133],d[1136,2048],d[617,806],\
#d[1034,2231],d[621,802],d[624,825],d[1079,2140],d[1152,2054],d[1043,2231],\
#d[954,1562]
heigh2=d[886,1495],d[1003,643],d[820,577],d[654,511],d[1067,627],\
d[902,604],d[316,128],d[955,631],d[1122,555],d[1078,591],d[424,318],\
d[1174,538],d[422,320],d[434,322],d[1126,561],d[1081,600],d[1174,542],\
d[822,495]
np.savetxt('stationheight.csv', heigh2, delimiter=',')
