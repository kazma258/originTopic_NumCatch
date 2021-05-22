import os
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"D:/pytesseract/tesseract.exe"
os.system(r"python ./getphoto.py")
os.system(r"python ./cutimg.py")
os.system(r"python ./getnum.py")