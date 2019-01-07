# Author Copyright LAPLA.Inc Time: 2018/8/11
import cv2 as cv
import os
os.chdir('../video')
 
if __name__ == '__main__':

	# 用VideoCapture()创建一个对象，其参数是摄像机的编号或者是一个视频的文件名
	cap = cv.VideoCapture(0)  

	# 指定视频视频编解码器格式
	fourcc = cv.VideoWriter_fourcc(*'XVID')  
	# 用VideoWriter创建一个对象，其参数有：输出视频的格式、编码格式、帧数（图片数/s,帧数少，视频不流畅，反之流畅，一般在25帧左右）、画面的大小
	out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
	 
	while (True):

		# 返回一个布尔值和一个图像矩阵
	    ret,frame = cap.read()
	    gray = cv.cvtColor(frame, 1)

	    # 一个标志，指定如何翻转数组; 0表示绕x轴翻转，正值（例如1）表示绕y轴翻转。负值（例如，-1）表示在两个轴周围翻转
	    flip = cv.flip(gray, 1)
	    out.write(frame)
	    cv.imshow("frame", flip)
	    k = cv.waitKey(1)
	    if k == ord('q'):
	        break
	 
	#完成后，要释放摄像机（或文件）
	cap.release()
	cv.destroyAllWindows()

