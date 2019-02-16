import sys
import os
from PIL import Image
from resizeimage import resizeimage

for folder in os.listdir("./pictures/"):
    for file in os.listdir("./pictures/" + folder + "/"):
        try:
            with open("./pictures/" + folder + "/" + file, 'r+b') as f:
                with Image.open(f) as image:
                    resized_image = resizeimage.resize_cover(image, [256, 144])
                    resized_image.save("./pictures/" + folder + "/" + file, image.format)
        except:
            os.remove("./pictures/" + folder + "/" + file)
