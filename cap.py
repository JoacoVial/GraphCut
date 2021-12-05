import cv2
import numpy as np
puntero = []
def puntos(fo):
    img=cv2.imread('mri-brain.jpg')

    def generador_matriz(lista,size_x,size_y):
        l=[]
        for i in range(0,size_x):
            l.append([])
            for e in range(0,size_y):
                boleano = True
                for j in lista:
                    if(j[0] == i and j[1] == e):
                        boleano = False
                        l[i].append(1)
                if boleano:
                    l[i].append(0)
        return l

    def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            xy = "%d,%d" % (x, y)
            cv2.circle(img, (x, y), 1, (255, 0, 0), thickness = -1)
            cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                        1.0, (0,0,0), thickness = 1)
            cv2.imshow(fo, img)
            global puntero
            puntero.append(xy)

    cv2.namedWindow(fo)
    cv2.setMouseCallback(fo, on_EVENT_LBUTTONDOWN)
    for i in range(1):
        cv2.imshow(fo, img)
        if cv2.waitKey(0)&0xFF==27:
            break
    cv2.destroyAllWindows()
    lista = []
    for i in puntero:
        lista.append(i.split(','))
    for i in lista:
        i[0] = int(i[0])
        i[1] = int(i[1])

    lista = generador_matriz(lista, 617, 617)
    return lista