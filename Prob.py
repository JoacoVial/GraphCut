import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2gray, rgb2hsv
from skimage.filters import threshold_otsu
from math import log

def otsu(imgName):
	img = imread(imgName)
	img_gray = rgb2gray(img)	
	thresh = threshold_otsu(img_gray)
	img_otsu  = img_gray < thresh
	return(img_otsu)

def prob(imgName, l ):
	img = imread(imgName)
	pObj = rgb2gray(img)
	pBkg = rgb2gray(img)
	img_hsv = rgb2hsv(img)
	ac=0
	bc=0
	for a in img_hsv[:,:,2]:
		for b in a:
			if(b > 0.71 and b <= 1): #10%
				pObj[ac][bc]= -log(0.1) * l
				pBkg[ac][bc]= -log(0.9)	* l
			if(b > 0.400 and b <= 0.7): #30%
				pObj[ac][bc]= -log(0.3) * l
				pBkg[ac][bc]= -log(0.7)* l
			if(b > 0.180 and b <= 0.400): #100%
				pObj[ac][bc]= -log(1)* l
				pBkg[ac][bc]= -log(0.0001)* l
			if(b > 0.050 and b <= 0.180): #50%
				pObj[ac][bc]= -log(0.5)* l
				pBkg[ac][bc]= -log(0.5)* l
			if(b <=0.050):#0%
				pObj[ac][bc]= -log(0.0001)* l
				pBkg[ac][bc]= -log(1)* l
			bc=bc+1
		ac=ac+1
		bc=0
	return(pObj,pBkg)

