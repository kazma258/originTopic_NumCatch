import cv2
import os

if __name__ == "__main__":
    txt_file = open('./contours.txt', 'r')
    count = len(txt_file.readlines())
    pos = [[0]*4 for i in range(count)]
    