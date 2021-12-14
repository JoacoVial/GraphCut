import cv2
import numpy as np
puntero = []
def puntos(fo,imName):
    global puntero
    puntero = []
    img=cv2.imread(imName)
    def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            xy = "%d,%d" % (x, y)
            if fo == "SELECCIONE LOS PUNTOS DEL OBJETO":
                cv2.circle(img, (x, y), 0, (0, 0, 255), thickness = -1)
            if fo == "SELECCIONE LOS PUNTOS DEL FONDO":
                cv2.circle(img, (x, y), 0, (0, 255, 0), thickness = -1)
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
    return lista


