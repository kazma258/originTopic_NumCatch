#3辨識圖片的數字
import cv2
import numpy as np
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

def final_result():
    f = open(r'./result.txt')
    data = f.read().splitlines()
    f.close()
    for i in range(len(data)):
        data[i] = data[i].split(' ')
    for i in range(len(data)):
        for n in range(len(data[i])):
            data[i][n] = int(data[i][n])

    count = 0
    for i in range(len(data)):
        if(i == len(data)-1):
            data[i][0] = count
        elif(abs(data[i][0] - data[i+1][0]) <= 50):
            data[i][0] = count
        else: 
            data[i][0] = count
            count+=1
        # print(data[i])

    dx_point = 0
    i = [0]*2
    final_out = []
    while (i[1] <= len(data)):
        try:
            if(data[i[1]][0] == dx_point):
                i[1]+=1
            elif(data[i[1]][0] != dx_point):
                temp = data[i[0] : i[1]]
                temp.sort(key=lambda x:x[1])
                for temp_c in range(len(temp)):
                    temp[temp_c][1] = temp_c
                final_out.append(temp)
                # print('{} {} {}'.format(dx_point, i, temp))
                i[0]=i[1]
                i[1]+=1
                dx_point+=1
        except:
            temp = data[i[0] : i[1]]
            temp.sort(key=lambda x:x[1])
            for temp_c in range(len(temp)):
                temp[temp_c][1] = temp_c
            final_out.append(temp)
            # print('{} {} {}'.format(dx_point, i, temp))
            i[1]+=1

    # for i in range(len(final_out)):
    #     print(final_out[i], '\n')
    f = open(r'./finalfile.txt', 'w')
    transpose_final_out = [[0]*3 for i in range(4)]
    for i in range(len(final_out)):
        for m in range(len(final_out[i])):
            transpose_final_out[i][m] = final_out[i][m][2]

    # print(transpose(transpose_final_out))
    transpose_final_out = transpose(transpose_final_out)
    # print(transpose_final_out)
    for i in range(len(transpose_final_out)):
        for m in range(len(transpose_final_out[i])):
            f.write('{:>3d}'.format((transpose_final_out[i][m])))
        f.write('\n')

def transpose(matrix): 
    return [[i[j] for i in matrix] for j in range(0, len(matrix[0]))]

if __name__ == "__main__":
    write_numfile()
    final_result()