import cv2
import Photo2Numdata

# 原影象路徑
origin_pic = cv2.imread('./Testdata/testmodle3.jpg')
# 文件路徑，用於記錄輪廓框座標
txt_file = open('./contours.txt', 'w')

origin_pic = Photo2Numdata.greenmask(origin_pic)
# 要先轉換成單通道灰度影象才能進行後續的影象處理
pic = cv2.cvtColor(origin_pic, cv2.COLOR_BGR2GRAY)
# 閾值處理，將前景全填充為白色，背景全填充為黑色
_, pic = cv2.threshold(src=pic, thresh=200, maxval=255, type=1)
# 中值濾波，去除椒鹽噪聲
pic = cv2.medianBlur(pic, 5)
# 邊緣檢測，得到的輪廓列表
contours, _2 = cv2.findContours(
    pic, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
# 根據輪廓列表，迴圈在原始影象上繪製矩形邊界
for i in range(len(contours)):
    cnt = contours[i]
    x, y, w, h = cv2.boundingRect(cnt)
    origin_pic = cv2.rectangle(origin_pic, (x, y), (x+w, y+h), (255, 0, 0), 2)
    txt_file.write('{}: [{},{}  {},{}  {},{}  {},{}]\n'.format(
        i+1, x, y, x, y+h, x+w, y, x+w, y+h))

cv2.imwrite('./rectangle.jpg', origin_pic)
txt_file.close()

cv2.imshow('', origin_pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
