import random
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def MutateFile(file, amount,index):
    if amount == index:
        return
    image = Image.open("input/" + file)
    draw = ImageDraw.Draw(image)
    image.save("output/" +"(" + str(index) + ")" +  file)
    index += 1
    MutateFile(file,amount,index)



def MutateImages(files):
    amount = int(input("Amount Of Images You Want To Augment: "))
    for file in files:
        MutateFile(file,amount,0)