#http://pmneila.github.io/PyMaxflow/tutorial.html#getting-started
#https://notebook.community/long0612/randProbs/graphcut/graphcut
import maxflow
import cv2
import numpy as np
from math import exp, pow, log
#import tracemalloc
from matplotlib import pyplot as ppl
import Prob
import cap as K
#import sys
#np.set_printoptions(threshold=sys.maxsize)

#tracemalloc.start()

def boundaryPenalty(ip, iq):
    bp = exp(-pow(int(ip) - int(iq), 2) / (2 * pow(4, 2)))
    return bp

def cap_tlinks(lista):
    k = 0
    for i in lista:
        for j in i:
            k += j
    return k

def tlinks(cap, meter, sacar, K):
    link = [ [ 0 for i in range(617) ] for j in range(617) ]
    for i in range(len(meter)):
        for j in range(len(meter)):
            if meter[i][j] == 1:
                link[i][j] = K
            if sacar[i][j] == 1:
                link[i][j] = 0
            else:
                link[i][j] = cap[i][j]
    return link
        



img = cv2.imread('mri-brain.jpg', cv2.IMREAD_GRAYSCALE).astype(np.float)

g = maxflow.Graph[int]()

B = 0
nodeids = g.add_grid_nodes(img.shape)

structure = np.array([  [0, 0, 0],
                        [0, 0, 1],
                        [0, 0, 0]])

W = []
vecinos = []

for i in range(len(img)):
    for j in range(len(img[i])):
        if j == 616:
            B = 0
            vecinos.append(B)
        else:
            B = boundaryPenalty(img[i][j], img[i][j+1])
            vecinos.append(B)
        
    W.append(vecinos)
    vecinos = []

peso = cap_tlinks(W)
W = np.array(W)
vecinos = []
g.add_grid_edges(nodeids, weights=W, structure=structure, symmetric=True)

W = []
structure = np.array([  [0, 0, 0],
                        [0, 0, 0],
                        [0, 1, 0]])

for i in range(len(img)):
    for j in range(len(img[i])):
        if i == 616:
            B = 0
            vecinos.append(B)
        else:
            B = boundaryPenalty(img[i][j], img[i+1][j])
            vecinos.append(B)
        
    W.append(vecinos)
    vecinos = []

peso += cap_tlinks(W)
W = np.array(W)

g.add_grid_edges(nodeids, weights=W, structure=structure, symmetric=True)

obj, bkg = Prob.prob('mri-brain.jpg', 1)
KOBJ = K.puntos("SELECCIONE LOS PUNTOS DEL OBJETO")
KBKG = K.puntos("SELECCIONE LOS PUNTOS DEL FONDO")

TLINKS_OBJ = tlinks(obj, KOBJ, KBKG, peso)
TLINKS_BGK = tlinks(bkg, KBKG, KOBJ, peso)

g.add_grid_tedges(nodeids, TLINKS_OBJ, TLINKS_BGK)

flow = g.maxflow()
print(f"\n\nFlujo máximo: {flow}\n")

# sgm.shape == nodeids.shape
sgm = g.get_grid_segments(nodeids) #False pertenece a S y True a T
print(sgm)
img2 = np.int_(np.logical_not(sgm))

#ppl.imshow(img2)
#ppl.show()

#print("Memoria utilizada: {} bytes\n\n".format(tracemalloc.get_traced_memory()[1] - tracemalloc.get_tracemalloc_memory()))
#tracemalloc.stop()