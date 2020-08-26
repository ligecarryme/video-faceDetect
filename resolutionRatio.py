import cv2
import os
from faceClassify import getImageVar

dirPath = r"E:\videos\bingxing\train\9/"


def resolution():
    for pic in os.listdir(dirPath):
        img = cv2.imread(dirPath + pic)
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgvar = getImageVar(img)
        # print(pic + "  " + str(imgvar))
        if imgvar < 100:
            try:
                os.remove(dirPath + pic)
                print("deleted image var: " + pic + "  " + str(imgvar))
            except OSError:
                print(OSError)
            # print("image var: " + pic + "  " + str(imgvar))


if __name__ == '__main__':
    resolution()
