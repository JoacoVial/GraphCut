#http://pmneila.github.io/PyMaxflow/tutorial.html#getting-started
#https://notebook.community/long0612/randProbs/graphcut/graphcut
import maxflow
import cv2
import numpy as np
from math import exp, pow, log
import tracemalloc
from matplotlib import pyplot as ppl
import Prob
import cap as K
import pintar
import corte

#import sys
#np.set_printoptions(threshold=sys.maxsize)

tracemalloc.start()

def boundaryPenalty(ip, iq):
    bp = exp(-pow(int(ip) - int(iq), 2) / (2 * pow(4, 2)))
    return bp

def cap_tlinks(lista):
    k = 0
    for i in lista:
        for j in i:
            k += j
    return k
"""
def tlinks(cap, meter, sacar, K):
    link = [ [ 0 for i in range(256) ] for j in range(256) ]
    for i in range(len(meter)):
        for j in range(len(meter)):
            if meter[i][j] == 1:
                link[i][j] = K
            if sacar[i][j] == 1:
                link[i][j] = 0
            else:
                link[i][j] = cap[i][j]
    return link
 """       
imgName = 'mri-brain.jpg'
ori_corte, img2, img ,lista = corte.corte()
ori_corte = corte.corte2(lista)
size_x = len(img)
size_y = len(img[0]) 

g = maxflow.Graph[int]()
B = 0
nodeids = g.add_grid_nodes(img.shape)

structure = np.array([  [0, 0, 0],
                        [0, 0, 1],
                        [0, 0, 0]])

W = []
vecinos = []

for i in range(size_x):
    for j in range(size_y):
        if j == size_y-1:
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

for i in range(size_x):
    for j in range(size_y):
        if i == size_x-1:
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

print(peso)

KOBJ = K.puntos("SELECCIONE LOS PUNTOS DEL OBJETO",img2)
KBKG = K.puntos("SELECCIONE LOS PUNTOS DEL FONDO",img2)

obj, bkg = Prob.prob(ori_corte, 1, KOBJ, KBKG, peso)
g.add_grid_tedges(nodeids, obj, bkg)

flow = g.maxflow()
print(f"\n\nFlujo máximo: {flow}\n")

sgm = g.get_grid_segments(nodeids) #False pertenece a S y True a T

cut = np.int_(sgm)

cut = pintar.rojo(ori_corte, cut)
ppl.imshow(cut)
ppl.savefig("prueba.jpg")
img=cv2.imread('mri-brain.jpg')
img2 = corte.pegar(img, cut, lista)
ppl.imshow(img2)
ppl.show()
#ppl.savefig("prueba.jpg")

#print("Memoria utilizada: {} bytes\n\n".format(tracemalloc.get_traced_memory()[1] - tracemalloc.get_tracemalloc_memory()))
#tracemalloc.stop()
