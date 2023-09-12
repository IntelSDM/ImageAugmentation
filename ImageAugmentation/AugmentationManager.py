import random
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def MutateFile(file, amount, index):
    if amount == index:
        return
    image = Image.open("input/" + file).convert("RGBA")  # Convert the image to RGBA mode
    width, height = image.size
    widthmod = random.randint(1, 8)
    heightmod = random.randint(1, 8)
    rects = random.randint(1, 6)
    
    augmentedimage = image.copy()
    
    for rectangles in range(rects):
        x0 = random.randint(0, int(width/1.5))
        y0 = random.randint(0, int(height/1.5))
        x1 = random.randint(x0, width)
        y1 = random.randint(y0, height)
        opacity = random.randint(30, 145)

        # Create a new transparent RGBA image
        rect = Image.new("RGBA", image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(rect)
        colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), opacity) 

        draw.rectangle([x0, y0, x1, y1], fill=colour)

        # Composite each rectangle onto augmentedimage
        augmentedimage = Image.alpha_composite(augmentedimage, rect)

    augmentedimage.save("output/" + "(" + str(index) + ")" + file.split('.')[0] + ".png")
    index += 1
    MutateFile(file, amount, index)


def MutateImages(files):
    amount = int(input("Amount Of Images You Want To Augment: "))
    for file in files:
        MutateFile(file,amount,0)