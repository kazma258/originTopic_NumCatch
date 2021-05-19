#3辨識圖片的數字
import cv2
from numpy import imag
import pytesseract
import os
import getphoto

def numget(img):
    pytesseract.pytesseract.tesseract_cmd = r"D:/pytesseract/tesseract.exe"
    #img.show()
    result = ""
    output = pytesseract.image_to_string(img, lang="eng", config="--psm 8")
    for i in range(len(output)):
        if output[i].isdigit():
            result += output[i]
    return result

def mask(imgpath):
    img = cv2.imread(imgpath)
    # img = getphoto.greenmask(img)
    return img

def write_numfile():
    folder = r"./Numdata/"
    filelist = os.listdir(folder)
    f = open(r'./result.txt', 'w')
    for file in filelist:
        img = getphoto.imgq(mask(folder+file))
        # cv2.imshow(file, img)
        num = numget(img)
        # print('{} \nThe result is: {}'.format(folder+file, num))
        if('.jpg' in file):
            file = file[:-4]
            file = file.replace(',', ' ')
        # print(file)
        f.write('{} {}\n'.format(file, num))
    f.close()

    cv2.waitKey()
    cv2.destroyAllWindows()

def lenl(var):
    return{
        0 : map[i].x,
        1 : map[i].y,
        2 : map[i].num
    }.get(var, 'error')

class num_Map:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

if __name__ == "__main__":
    write_numfile()
    f = open(r'./result.txt')
    data = f.read().splitlines()
    for i in range(len(data)):
        data[i] = data[i].split(' ')

    map = [num_Map(0,0,0)] * 11
    for i in range(len(data)):
        for n in range(len(data[i])):
            lenl[n] = data[i][n]
            # if(n is 0):
            #     map[i].x = data[i][n]
            # elif(n is 1): map[i].y = data[i][n]
        print('{} {} {}'.format(map[i].x, map[i].y, map[i].num))
    
    os.system('pause')
