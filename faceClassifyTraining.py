
import os
import cv2
import numpy as np

dir_path = r"E:\videos\bingxing\person_src\facedata"
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier('./traincascade.xml')
names = ["others", "dali", "gali", "haitang", "meijia", "yifei", "zhangwei", "ziqiao", "zengxiaoxian", "xiaohei", "more than two people"]

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(img, scaleFactor=1.2 , minSize=(32, 32), minNeighbors=3);
    if (len(faces) == 0):
        return None, None
    (x, y, w, h) = faces[0]
    return gray[y:y + w, x:x + h], faces[0]

def prepare_training_data(data_folder_path):
    dirs = os.listdir(data_folder_path)
    faces = []
    labels = []
    for dirName in dirs:
        subject_dir_path = data_folder_path + "/" + dirName
        subject_images_names = os.listdir(subject_dir_path)
        label = int(dirName)
        for image_name in subject_images_names:
            image_path = subject_dir_path + "/" + image_name
            image = cv2.imread(image_path)
            face, rect = detect_face(image)
            if face is not None:
                faces.append(face)
                labels.append(label)
    cv2.destroyAllWindows()
    return faces,labels

print("Preparing data...")
faces, labels = prepare_training_data(dir_path)
print("Data prepared")

print("Total faces: ", len(faces))
print("Total labels: ", len(labels))

recognizer.train(faces, np.array(labels))

recognizer.write(r"E:\videos\bingxing\person_src\facedata\trainer.yml")
print("ok")