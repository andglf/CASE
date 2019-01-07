import cv2 as cv
import numpy as np 
import os

os.chdir('../video')
if __name__ == '__main__':
	cap = cv.VideoCapture('output.avi')

	cv.namedWindow('video', cv.WINDOW_NORMAL)

	while cap.isOpened():
		ret, frame = cap.read()

		if ret:
			cv.imshow('video', frame)

			if cv.waitKey(1) == 27:
				break
		else:
			if cv.waitKey(1) == 27:
				cap.release()
	cv.destroyAllWindows()