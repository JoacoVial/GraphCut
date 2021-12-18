import cv2
import numpy as np
puntero = []

def corte(nombre):
    fo = "Seleccione los pixeles para recortar la imagen"
    global puntero
    puntero = []
    img=cv2.imread(nombre)
    def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            xy = "%d,%d" % (x, y)
            cv2.circle(img, (x, y), 3, (0, 0, 255), thickness = -1)
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
    l = []
    for i in puntero:
        l.append(i.split(','))
    for i in l:
        i[0] = int(i[0])
        i[1] = int(i[1])
    """if l[1][0]-l[0][0]>l[1][1]-l[0][1]:
        l[1][1]+=((l[1][0]-l[0][0])-(l[1][1]-l[0][1]))
    else:
        l[1][0]+=((l[1][1]-l[0][1])-(l[1][0]-l[0][0]))"""
    
    img = cv2.imread(nombre)
    crop_img = img[l[0][1]:l[1][1],l[0][0]:l[1][0]]
    cut_orig = img[l[0][1]:l[1][1],l[0][0]:l[1][0]]
    img = cv2.imread(nombre, cv2.IMREAD_GRAYSCALE).astype(np.float)
    crop_img_gris = img[l[0][1]:l[1][1],l[0][0]:l[1][0]]
    #cv2.imshow("Imagen recortada", crop_img)
    #cv2.waitKey(0)

    return cut_orig, crop_img, crop_img_gris,l

#img,lista = corte()
#print(lista)

def pegar(img,img_corte, l):
    img[l[0][1]:l[1][1],l[0][0]:l[1][0]] = img_corte

    #cv2.imshow("IRM segmentada",img)
    #cv2.waitKey(0)

    return img

def corte2(l, nombre):
    img = cv2.imread(nombre)
    crop_img = img[l[0][1]:l[1][1],l[0][0]:l[1][0]]

    return crop_img
