import cv2
import os

w = 48
h = 48

def getimage(file_dir):
    images = {}
    for root, dirs, files in os.walk(file_dir):
        for name in files:
            images[name] = os.path.join(root, name)
    return images


if __name__ == '__main__':
    n = -1
    dirpath_dst = r'E:\videos\bingxing\train\all/'
    # dirpath2 = r'E:\videos\bingxing\zhang_size'
    dir_path = r"E:\videos\bingxing\person_src\11111/"
    dirs = os.listdir(dir_path)
    print(dirs)
    # dir = os.getcwd()
    # dirpath = os.path.join(dir, 'pos')
    for dir in dirs:
        imagedic = getimage(dir_path + dir)
        # print(imagedic)
        try:
            for key, value in imagedic.items():
                img = cv2.imread(value)
                img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img2 = cv2.resize(img1, (w, h))
                cv2.imwrite(dirpath_dst + str(n + 1).rjust(4, '0') + '.jpg', img2)
                n += 1
        except KeyboardInterrupt:
            print('暂停一下')