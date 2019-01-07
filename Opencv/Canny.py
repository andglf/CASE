import cv2 as cv 
import numpy as np 
import os

os.chdir("../image")


if __name__ == '__main__':
	img = cv.imread('hear.jpg', 0)

	img = cv.GaussianBlur(img, (3, 3), 0)

	canny = cv.Canny(img, 50, 150)

	cv.namedWindow('图片'.encode('gbk').decode(errors='ignore'), cv.WINDOW_NORMAL)
	cv.imshow('图片'.encode('gbk').decode(errors='ignore'), canny)

	if cv.waitKey(0) == ord('q'):
		cv.destroyAllWindows() 


