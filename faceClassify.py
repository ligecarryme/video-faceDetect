
import cv2
from PIL import Image


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("./trainer.yml")
font = cv2.FONT_HERSHEY_SIMPLEX

idnum = 0
# names = ["others", "dali", "gali", "haitang", "meijia", "xiaohei", "yifei", "zhangwei"]
names = ["others", "dali", "gali", "haitang", "meijia", "yifei", "zhangwei", "ziqiao", "zengxiaoxian", "xiaohei", "more than two people"]

def Classify(grayImg, rect):
    x, y, w, h = rect
    idnum, confidence = recognizer.predict(grayImg[y:y+h, x:x+w])

    if confidence < 100:
        id = names[idnum]
        confidence = "{0}%".format(round(100 - confidence))
    else:
        id = names[0]
        confidence = "{0}%".format(round(100 - confidence))

    # cv2.putText(grayImg, id, (x+5, y-5), font, 1, (0, 0, 255), 1)
    # cv2.putText(grayImg, str(confidence), (x + 5, y + h - 5), font, 1, (0, 0, 0), 1)
    return id, confidence

def draw_rectangle(img, rect):
    (x,y,w,h) = rect
    cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0), 2)

def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), font, 1, (0, 255, 0), 1)

def getImageVar(img):
    pic = cv2.imread(img)
    gray =cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
    imageVar = cv2.Laplacian(gray, cv2.CV_64F).var()
    return imageVar

# if __name__ == '__main__':
    # getImageVar(r"D:\PycharmProjects\parallelTech\AqingGyu5_30-2(1)_result\zhangwei\zhangwei0359.jpg")