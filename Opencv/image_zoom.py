import cv2 as cv 
import numpy as np 
import os

os.chdir("../image")

if __name__ == '__main__':
	img = cv.imread('hear.jpg', 1)
	# 图像缩放
	imgnew = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_LINEAR)

	# 创建新窗口
	cv.namedWindow('image', cv.WINDOW_NORMAL)
	cv.imshow('image', imgnew)

	if cv.waitKey(0) == ord('q'):
		cv.destroyAllWindows()