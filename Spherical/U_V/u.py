# -*- coding: utf-8 -*-
"""
bathy
"""
# -*- coding: utf-8 -*-

# load library
import numpy as np

# import data
d=np.loadtxt('j1.txt')
n,m = d.shape
d1=d*0
f = open('u.txt','w')
for i in range(n):
    for j in range(m):
        f.write('%12.3E ' % (d1[i,j]))
    f.write('\n')
        
f.close()

