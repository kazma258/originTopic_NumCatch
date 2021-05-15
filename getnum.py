import cv2
from numpy import imag
import pytesseract
from PIL import Image
import os
import getphoto

def numget(img):
    pytesseract.pytesseract.tesseract_cmd = r"D:/pytesseract/tesseract.exe"
    #img.show()
    result = ""
    output = pytesseract.image_to_string(img, lang="eng", config="--psm 8")
    for i in range(len(output)):
        # if output[i].isdigit():
        #     result += output[i]
        return output

def mask(imgpath):
    img = cv2.imread(imgpath)
    # img = getphoto.greenmask(img)
    return img

if __name__ == "__main__":
    folder = r"./Numdata/"
    filelist = os.listdir(folder)
    for file in filelist:
        img = getphoto.imgq(mask(folder+file))
        cv2.imshow(file, img)
        num = numget(img)
        print('{} \nThe result is: {}'.format(folder+file, num))
    
    cv2.waitKey()
    cv2.destroyAllWindows()