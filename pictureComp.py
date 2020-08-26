#coding=utf-8
#author='Shichao-Dong'

from PIL import Image
import math
import operator
import os
from functools import reduce
from rename import rename

dirPath_src = r"E:\videos\bingxing\person_src\facedata\6/"
dirPath_dst = ""

def compare(pic1,pic2):
    '''
    :param pic1: 图片1路径
    :param pic2: 图片2路径
    :return: 返回对比的结果
    '''
    image1 = Image.open(pic1)
    image2 = Image.open(pic2)

    histogram1 = image1.histogram()
    histogram2 = image2.histogram()

    differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2,histogram1, histogram2)))/len(histogram1))

    # print(differ)
    return differ

if __name__ == '__main__':

    # print(compare(r'E:\videos\bingxing\person_src\facedata\1\0670.jpg',r'E:\videos\bingxing\person_src\facedata\1\0671.jpg'))
    total = len(os.listdir(dirPath_src))
    for pic in os.listdir(dirPath_src):
        i = int(pic.split('.')[0]) + 1
        print(pic, end=' ')
        while i < total:
            pic2 = str(i).rjust(4, '0') + ".jpg"
            diff = compare(dirPath_src + pic , dirPath_src + pic2)
            # print(diff)
            if diff < 33.0:
                # total = rename(dirPath_src)
                try:
                    os.remove(dirPath_src + pic2)
                except OSError:
                    print("deleted fail")
                print("different = " + str(diff) + "  src pic :" + pic + "  need delete pic" + str(i))
            i = i + 1

        total = rename(dirPath_src)