import cv2 as cv
import numpy as np
import os

os.chdir('../image') 

if __name__ == '__main__':
	img = cv.imread('body.jpg')
	print(img.shape)
	print(cv.split(img))
	px = img[100, 100]
	print(px)
	px1 = img[100, 100, 0]
	print(px1)