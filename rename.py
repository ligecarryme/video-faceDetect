import os

dirPath = r"E:\videos\bingxing\person_src\facedata\9/"

def rename(path):
    filelist = os.listdir(path)
    # print(filelist)
    count = 0
    for item in filelist:
        src = os.path.join(os.path.abspath(path), item)
        dst = os.path.join(os.path.abspath(path), '%s.jpg' % str(count).rjust(4, '0'))
        try:
            os.rename(src, dst)
            count += 1
        except:
            continue
    return count

print(rename(dirPath))
