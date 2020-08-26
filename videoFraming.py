# coding=utf-8

import cv2
import os

video_formats = [".mp4", ".avi"]
# video_path = r'E:\videos\bingxing/'
video_path = os.getcwd() + "\\"
names = ["others", "dali", "gali", "haitang", "meijia", "xiaohei", "yifei", "zhangwei", "ziqiao", "zengxiaoxian", "more than two people"]

def filter_format(x, all_formats):
    if x[-4:] in all_formats:
        return True
    else:
        return False

def videoFrame():

    videos = os.listdir(video_path)
    videos = filter(lambda x: filter_format(x, video_formats), videos)

    for video_name in videos:  # 每个视频文件建立对应的文件夹
        file_name = video_name.split('.')[0]
        folder_name = video_path + file_name
        result_folder_name = video_path + file_name + '_result'

        try:
            os.makedirs(folder_name, exist_ok=False)
        except OSError:
            print('folder '+ file_name +' already exists')

        try:
            os.makedirs(result_folder_name, exist_ok=False)
        except OSError:
            print('folder ' + file_name + '_result already exists')
            continue
        vc = cv2.VideoCapture(video_path + video_name)
        # classfier = cv2.CascadeClassifier(r'C:\Users\admin\AppData\Local\Programs\Python\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
        frame_count = 0
        rval = vc.isOpened()

        while rval:
            rval, frame = vc.read()  # rval,frame是获vc.read()方法的两个返回值。其中rval是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾，它的返回值就为False。frame就是每一帧的图像，是个三维矩阵。
            vc.set(cv2.CAP_PROP_POS_MSEC, 1000 * frame_count)
            pic_path = folder_name + '/'
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # faceRects = classfier.detectMultiScale(frame, scaleFactor=1.2, minSize=(32, 32), minNeighbors=3)
            # if len(faceRects) > 0:
                # for faceRect in faceRects:
                #     x, y, w, h = faceRect
                #     cv2.rectangle(frame, (x - 1, y - 1), (x + w + 1, y + h + 1), (0, 255, 0), 2)
                    # if rval == True:
                # cv2.imwrite(pic_path + str(frame_count) + '.jpg', frame)
                    # cv2.imwrite(pic_path + str(frame_count) + '.jpg', frame[y:y+h, x:x+w])
                    # else:
                    #     break
                    # print('picture name'+file_name+'_'+str(frame_count)+'---'+'x axis: '+str(x)+' y axis: '+str(y)+' weight: '+str(w)+' height: '+str(h))
            if rval == True:
                frame_count = frame_count + 1
                cv2.imwrite(pic_path + file_name + '_' + str(frame_count) + '.jpg', frame)
            else:
                continue
        vc.release()
        print('save_success')
        print(folder_name + ' video frame_count:' + str(frame_count))
    for name in names:
        folder_names = result_folder_name + "\\" + name
        try:
            os.makedirs(folder_names, exist_ok= False)
        except OSError:
            continue
            # print("folder " + name +" already exist")

# videoFrame()
