import cv2
import numpy as np
from numpy.core.fromnumeric import compress
import Comparison


def greenmask(image):
    # Green濾鏡
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_green = np.array([30, 43, 46])
    upper_green = np.array([50, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    green = cv2.bitwise_and(image, image, mask=mask)
    # green = cv2.Canny(green, 50, 150) #邊緣偵測
    return green


def img_treat(img, return_code):
    # 轉灰度圖
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 高斯濾波
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    # canny邊緣檢測
    gray = cv2.Canny(gray, 100, 300)
    # 閥值分割
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    # cv2.imshow('exe',binary)

    # 獲取輪廓
    contours, hierarchy = cv2.findContours(
        binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.imshow('image',img)
    # cv2.imshow('imgTogray',binary)

    print("contours 數量：", len(contours))
    # 繪製外框
    cntimg = cv2.drawContours(img.copy(), contours, -1, (0, 255, 0), 3)

    count = 0
    for c in contours:
        # CV2.moments會傳回一系列的moments值，我們只要知道中點X, Y的取得方式是如下進行即可。
        M = cv2.moments(c)
        c_x = int(M['m10'] / M['m00'])
        c_y = int(M['m01'] / M['m00'])
        # 在中心點畫上黃色實心圓
        cv2.circle(cntimg, (c_x, c_y), 5, (1, 227, 254), -1)
        area = int(cv2.contourArea(c))  # 計算面積v
        if area < 100:
            count += 1
            continue
        print('第', count, '個輪廓的面積為: ', area, '座標: ', c_x, c_y)
        count += 1

    # show_photo('DrawCnt', cntimg)
    if return_code == 1:  # 回傳IMG
        return cntimg
    elif return_code == 2:  # 回傳LIST
        return img_info
    else:
        print('Error value!!!')
        return -1


def show_photo(win_name, img):
    cv2.namedWindow(win_name, 0)
    cv2.resizeWindow(win_name, 554, 739)
    cv2.imshow(win_name, img)

if __name__ == '__main__':
    img = cv2.imread(r"./Testdata/testmodle1.png")
    img = greenmask(img)
    # 轉灰度圖
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 高斯濾波
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    # canny邊緣檢測
    gray = cv2.Canny(gray, 100, 300)
    # 閥值分割
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    (cnts, _) = cv2.findContours(binary.copy(),
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print(len(cnts))

    # c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
    # rect = cv2.minAreaRect(c)
    # box = np.int0(cv2.boxPoints(rect))
    # count = 0
    # img = cv2.drawContours(img, cnts, -1, (0, 255, 0), 3)

    # cutPicture = [0]*11
    # for c in cnts:
    #     # CV2.moments會傳回一系列的moments值，我們只要知道中點X, Y的取得方式是如下進行即可。
    #     M = cv2.moments(c)
    #     c_x = int(M['m10'] / M['m00'])
    #     c_y = int(M['m01'] / M['m00'])
    #     # 在中心點畫上黃色實心圓
    #     cv2.circle(img, (c_x, c_y), 5, (1, 227, 254), -1)
    #     area = int(cv2.contourArea(c))  # 計算面積v
    #     if area < 100:
    #         count += 1
    #         continue
    #     print('第', count, '個輪廓的面積為: ', area, '座標: ', c_x, c_y)
        
    #     count += 1

    # draw a bounding box arounded the detected barcode and display the image
    # cv2.imshow("Image", img)
    # cv2.imwrite("contoursImage2.jpg", img)

    txt_file = open('./contours.txt', 'w')
    for i in range(len(cnts)):
        cnt = cnts[i]
        x, y, w, h = cv2.boundingRect(cnt)
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        txt_file.write('{}: [{},{}  {},{}  {},{}  {},{}]\n'.format(
            i+1, x, y, x, y+h, x+w, y, x+w, y+h))

    cv2.imwrite('./rectangle.jpg', img)
    txt_file.close()

    cv2.waitKey()
    cv2.destroyAllWindows()
