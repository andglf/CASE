import cv2 as cv 
import numpy as np 

if __name__ == '__main__':

	img1 = cv.imread('hear.jpg')
	
	e = cv.getTickCount()
	print("======", e)
	for i in range(5,49,2): 
		img1 = cv.medianBlur(img1,i) 
	t = cv.getTickCount()
	print("-------", t)

	time = (e - t)/cv.getTickFrequency()
	print(time)