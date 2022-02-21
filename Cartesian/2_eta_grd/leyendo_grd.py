# leer *.grd de SURFER
import numpy as np


def limites(str):
    aux = str.split(' ')
    n = len(aux)
    vector = []
    for i in range(n):
        try:
            vector.append(float(aux[i]))
        except ValueError:
            pass
    valores = np.array(vector)
    return valores

def read_grd(filename):
    # se abre el archivo
    infile = open(filename, 'r')
    
    #lectura linea a linea
    infile.readline(-1)
    nx, ny = limites(infile.readline(-1))
    xmin, xmax = limites(infile.readline(-1))
    ymin, ymax = limites(infile.readline(-1))
    zmin, zmax = limites(infile.readline(-1))
    data = []
    for line in infile:
        data.append(line)
    infile.close()
    
    mv = []
    m = len(data)
    for i in range(m):
        mv.append(limites(data[i]))
    
    n = len(mv)
    mb = []
    for i in range(n):
        na = len(mv[i][:])
        for j in range(na):
            mb.append(mv[i][j])
    z = np.array(mb)
    return int(nx), int(ny), xmin, xmax, ymin, ymax, zmin, zmax, z
    