'''
Show images one by one in a folder
'''
from PIL import Image
import os
import psutil

def close_image_window():
    for proc in psutil.process_iter():
        if proc.name() == "display":
            proc.kill()

os.chdir('/home/zluo/food')
files = os.listdir('.')
for f in files:

    image = Image.open(f)
    image.show()
    value = raw_input("Is this a correct image?: ")
    close_image_window()


