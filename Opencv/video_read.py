import cv2 as cv
import os

os.chdir('video')

if __name__ == '__main__':
    # 用VideoCapture()创建一个对象，其参数是摄像机的编号或者是一个视频的文件名
    cap = cv.VideoCapture(0)

    # 指定视频视频编解码器格式
    fourcc = cv.VideoWriter_fourcc('M', 'J', 'P', 'G')
    # 用VideoWriter创建一个对象，
    # 其参数有：输出视频的格式、编码格式、帧数（图片数 / s, 帧数少，
    # 视频不流畅，反之流畅，一般在25帧左右）、画面的大小
    out = cv.VideoWriter('out.avi', fourcc, 20, (640, 480))
    cv.namedWindow('窗口'.encode('gbk').decode(errors='ignore'), cv.WINDOW_NORMAL)

    while cap.isOpened():
        # 返回一个布尔值和一个图像矩阵
        ret, frame = cap.read()
        if ret:
            gray = cv.cvtColor(frame, 1)

            # 一个标志，指定如何翻转数组;
            # 0表示绕x轴翻转，正值（例如1）表示绕y轴翻转。负值（例如，-1）表示在两个轴周围翻转
            flip = cv.flip(gray, 1)
            out.write(frame)
            cv.imshow('窗口'.encode('gbk').decode(errors='ignore'), flip)
            if cv.waitKey(1) == 27:
                break
        else:
            break
            
    # 完成后，要释放摄像机（或文件）
    cap.release()
    out.release()
    cv.destroyAllWindows()


