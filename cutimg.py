#2裁切框為小圖片
import cv2
import os
from re import split

def pos():
    txt_file = open(r'./contours.txt', 'r')
    read = txt_file.readlines() #讀取內容
    count = len(read) #讀取行數
    # print(read, count)
    pos = [[0]*8 for i in range(count)]
    for i in range(count):
        line = read[i]
        line= line[5:-2]
        pos[i] = split(r'[,\s]\s*', line) #切割值
        # print(pos[i])
    txt_file.close()
    return pos

def crop(pos):
    img = cv2.imread(r"./rectangle.jpg")
    dir = r'./Numdata/'
    if os.path.isdir(dir):
        filelist = os.listdir(dir)
        for file in filelist:
            os.remove(dir+file)
    else:
        os.mkdir(dir)
    for i in range(len(pos)):
        x = int(pos[i][0])+15
        y = int(pos[i][1])+15
        w = int(pos[i][6])-15
        h = int(pos[i][7])-15
        # print('{} {} {} {}'.format(x, y, w, h))
        crop_img = img[y:h, x:w]
        write_name = dir + str(x)+','+str(y)+'.jpg'
        cv2.imwrite(write_name,  crop_img)

if __name__ == "__main__":
    crop(pos())
