import getnum
import cutimg
import getphoto
from os import system

getphoto.img2photo()
cutimg.crop(cutimg.pos())
getnum.write_numfile()
getnum.final_result()
system('Pause')