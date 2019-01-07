import cv2 as cv
import numpy as np


def nothing(x):
    pass


if __name__ == '__main__':
    # 创建一副黑色图像
    img = np.zeros((300, 512, 3), np.uint8)

    # 创建新窗口
    cv.namedWindow('窗口'.encode("gbk").decode(errors='ignore'), cv.WINDOW_NORMAL)

    cv.createTrackbar('R',
                      '窗口'.encode("gbk").decode(errors='ignore'),
                      0, 225, nothing)
    cv.createTrackbar('G',
                      '窗口'.encode("gbk").decode(errors='ignore'),
                      0, 225, nothing)
    cv.createTrackbar('B',
                      '窗口'.encode("gbk").decode(errors='ignore'),
                      0, 225, nothing)

    switch = '0:OFF\n1:ON'
    cv.createTrackbar(switch,
                      '窗口'.encode("gbk").decode(errors='ignore'),
                      0, 1, nothing)

    while True:
        cv.imshow('窗口'.encode("gbk").decode(errors='ignore'), img)

        if cv.waitKey(1) == 27:
            break
        else:
            r = cv.getTrackbarPos('R', '窗口'.encode("gbk").decode(errors='ignore'))
            g = cv.getTrackbarPos('G', '窗口'.encode("gbk").decode(errors='ignore'))
            b = cv.getTrackbarPos('B', '窗口'.encode("gbk").decode(errors='ignore'))
            s = cv.getTrackbarPos(switch, '窗口'.encode("gbk").decode(errors='ignore'))

            if s == 0:
                img[:] = 0
            else:
                img[:] = [r, g, b]

    cv.destroyAllWindows()