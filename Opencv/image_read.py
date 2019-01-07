import cv2 as cv 
import numpy as np 
import os
os.chdir("../image")

if __name__ == '__main__':

	# 读取图片
	img = cv.imread('hear.jpg')
	cv.namedWindow('图片'.encode("gbk").decode(errors="ignore"))
	cv.imshow('图片'.encode("gbk").decode(errors="ignore"), img)
	cv.waitKey(0)
	cv.destroyAllWindows()