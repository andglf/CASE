import cv2 as cv 
import numpy as np 
import os

os.chdir('../image')


if __name__ == '__main__':
	
	img = cv.imread("hear.jpg")

	#下面的None本应该是输出图像的尺寸，但是因为后边我们设置了缩放因子
	#因此这里为None 

	res = cv.resize(img, None, fx=0.2, fy=0.2, interpolation=cv.INTER_CUBIC)

	#这里呢，我们直接设置输出图像的尺寸，所以不用设置缩放因子 
	height,width=img.shape[:2] 
	re1=cv.resize(img,(2*width,2*height),interpolation=cv.INTER_CUBIC)

	# 创建新窗口
	cv.namedWindow('res', cv.WINDOW_NORMAL)
	cv.namedWindow('img', cv.WINDOW_NORMAL)
	cv.namedWindow('res1', cv.WINDOW_NORMAL)
	while True:
		cv.imshow('res', res)
		cv.imshow('img', img)
		cv.imshow('res1', re1)
		if cv.waitKey(0) == 27:
			break

	cv.destroyAllWindows()