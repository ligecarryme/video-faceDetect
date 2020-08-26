# coding = utf-8

import os
import cv2
import shutil
from faceClassify import Classify, draw_text, getImageVar
from videoFraming import videoFrame


def detectAndclassify(dirPath, dirResultPath):
    count = -1
    classfier = cv2.CascadeClassifier('./traincascade.xml')
    # classfier = cv2.CascadeClassifier(r'D:\Program Files\opencv\opencv4.1.2\build\etc\lbpcascades\lbpcascade_frontalface_improved.xml')
    # classfier = cv2.CascadeClassifier(r'E:\training\TrainCascadeClassification\cascade.xml')
    for pic in os.listdir(dirPath):
        img = cv2.imread(dirPath + pic)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = classfier.detectMultiScale(gray, scaleFactor=1.2, minSize=(32, 32), minNeighbors=3)
        # imageVar = getImageVar(gray) #选择清晰的图片
        # print("imagevar value: " + str(imageVar))
        if len(faces) > 0 :
            # draw_text(img, str(imageVar), 10, 30)
            for face in faces:
                x, y, w, h = face
                cv2.rectangle(img, (x - 1, y - 1), (x + w + 1, y + h + 1), (0, 255, 0), 2)
                name, confidence = Classify(gray, face)
                draw_text(img, name, x + 5, y - 5)
                print(" name : "+name)
                draw_text(img, str(confidence), x + 5, y + h - 5)
            # print('lastX: ' + str(lastX) + ' lastY: ' + str(lastY), end='  ')
            if len(faces) == 1 :  #
                cv2.imwrite(dirResultPath + name + "\\" + name + str(count + 1).rjust(4, '0') + '.jpg', img)
            else:
                cv2.imwrite(dirResultPath + "more than two people\\" + "many_people" + str(count + 1).rjust(4, '0') + '.jpg', img)
            # cv2.imwrite("E:/videos/bingxing/facedata/User." + "zhangwei" + '.' + str(count) + '.jpg', gray[y: y + h, x: x + w])
        else:
            try:
                # shutil.move(dirPath + pic, dirResultPath + "others\\" + pic)
                os.remove(dirPath + pic)
                # print('have deleted  '+pic)
            except IOError:
                print("IOError")
                continue
        count = count + 1
        print(count, end="  ")
    print('total pictures: ' + str(count))

if __name__ == '__main__':
    # dirPath = os.getcwd() + '\\AqingGyu5_30-2(1)/'
    # dirResultPath = os.getcwd() + '\\AqingGyu5_30-2(1)_result/'

    path = os.getcwd()
    videoFrame()
    videoName = ""
    for dir in os.listdir(path):
        if os.path.splitext(dir)[1] == '.mp4':
            videoName = os.path.splitext(dir)[0]
        else:
            continue
    if videoName != "":
        dirPath = os.path.join(path, videoName) + '/'
        dirResultPath = os.path.join(path, videoName) + '_result' + '/'
    else:
        print("no videos")

    detectAndclassify(dirPath, dirResultPath)
    for resultDir in os.listdir(dirResultPath):
        everyoneDir = os.path.join(dirResultPath, resultDir)
        imgVarMax = 0
        picVarMax = ""
        for pic in os.listdir(everyoneDir):
            picPath = everyoneDir + '\\' +pic
            imgVar = getImageVar(picPath)
            if imgVarMax < imgVar :
                imgVarMax = imgVar
                picVarMax = pic

        if picVarMax != "":
            shutil.copy(everyoneDir + "\\" + picVarMax, dirResultPath)