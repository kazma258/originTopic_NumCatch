import cv2
from numpy import imag
import pytesseract
import os
import getphoto
import tesserocr
from PIL import Image

def numget(img):
    pytesseract.pytesseract.tesseract_cmd = r"D:/pytesseract/tesseract.exe"
    #img.show()
    result = ""
    output = pytesseract.image_to_string(img, lang="eng", config="--psm 10")
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
    # for file in filelist:
    #     img = getphoto.imgq(mask(folder+file))
    #     cv2.imshow(file, img)
    #     num = numget(img)
    #     print('{} \nThe result is: {}'.format(folder+file, num))

    for file in filelist:
        image = Image.open(folder+file)
        print(file)
        print(tesserocr.image_to_text(image)+'\n')
    
    # cv2.waitKey()
    # cv2.destroyAllWindows()