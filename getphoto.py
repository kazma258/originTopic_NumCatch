#1圖片轉尋找框
import cv2
import numpy as np


def show_photo(win_name, img):
    cv2.namedWindow(win_name, 0)
    cv2.resizeWindow(win_name, 554, 739)
    cv2.imshow(win_name, img)

def imgq(img):
    # 轉灰度圖
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 侵蝕膨脹
    kernel = np.ones((5,5), np.uint8)
    img = cv2.erode(img, kernel)
    img = cv2.dilate(img, kernel)
    # 高斯濾波
    img = cv2.GaussianBlur(img, (3,3), 0)
    # 二值化
    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    return img

def imgtreat(img):
    img = imgq(img)
    # canny邊緣檢測
    img = cv2.Canny(img, 100, 300)
    # 尋找輪廓
    (cnts, _) = cv2.findContours(img.copy(),
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print(len(cnts))
    return cnts

def img2photo():
    print("輸入讀取的圖片路徑")
    img = cv2.imread(input())
    # show_photo('mask', img)
    cnts = imgtreat(img)
    txt_file = open('./contours.txt', 'w')
    for i in range(len(cnts)):
        cnt = cnts[i]
        x, y, w, h = cv2.boundingRect(cnt)
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        txt_file.write('{:0>2d}: [{},{}  {},{}  {},{}  {},{}]\n'.format(
            i+1, x, y, x, y+h, x+w, y, x+w, y+h))

    cv2.imwrite('./rectangle.jpg', img)
    txt_file.close()

    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    img2photo()
