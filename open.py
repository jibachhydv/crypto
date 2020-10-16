from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt


vigenerKey = input("Enter the key to encrypt image: ")

# Open love.jpg
im = Image.open('check.jpeg')
img = cv2.imread('checkEncrypted.jpeg')
color = ('b','g','r')

for i,col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(histr, color = col)
    plt.xlim([0,256])
    
plt.show()
im.show()

import sys
sys.exit()
# Image Dimension

w,h = im.size
# print(w,h)

# Create New Image
newimage = Image.new(mode="RGB", size=(int(w),int(h)))
pixels = newimage.load()

caesarKey = ord(vigenerKey[0])



# Iterate Over the Image pixel by pixel
for i in range(int(w)):
    for j in range(int(h)):

        print(f"Sum of Pixels value {i}, {j} are {i+j}")
        key = ord(vigenerKey[(i+j) % len(vigenerKey)])
        print(f"Key is {vigenerKey} whose position is {vigenerKey[(i+j) % len(vigenerKey)]}")
        print(f"Ascii Value of Key is {key}")

        key = key * (i+1) *(j+1)
        print(f"Manipulated value of Key is {key}")
        print(key)
        # import sys
        # sys.exit()
        # Get pixel of first image

        pixel = im.getpixel((i,j))
        print(f"Real Pixel is: {pixel}")
        red = pixel[0] 
        green = pixel[1]
        blue = pixel[2]
        print(f"Red Value is {red}")
        print(f"Green Value is {green}")
        print(f"Blue Value is {blue}")

        # Transform the pixel
        eRed = (red + key) % 256
        eGreen = (green + key) % 256
        eBlue = (blue + key) % 256
        
        print(f"Manipulated Red Value is {eRed}")
        print(f"Manipulated Green Value is {eGreen}")
        print(f"Manipulated Blue Value is {eBlue}")
        
        # Set Pixel in new Image
        pixels[i,j] = (int(eRed), int(eGreen), int(eBlue))
        # print(pixels[i,j])
    # print(i)
newimage.show()




# Deencryption Of Image
deencrptedImage = Image.new(mode="RGB", size=(int(w), int(h)))
dPixels = deencrptedImage.load()


# Iterate Over the Image pixel by pixel
for i in range(int(w)):
    for j in range(int(h)):

        # print(f"Sum of Pixels value {i}, {j} are {i+j}")
        key = ord(vigenerKey[(i+j) % len(vigenerKey)])
        print(f"Key is {vigenerKey} whose position is {vigenerKey[(i+j) % len(vigenerKey)]}")
        print(f"Ascii Value of Key is {key}")

        key = key * (i+1) *(j+1)
        print(f"Manipulated value of Key is {key}")
        print(key)
        # import sys
        # sys.exit()
        # Get pixel of first image

        pixel = newimage.getpixel((i,j))
        print(f"Real Pixel is: {pixel}")
        red = pixel[0] 
        green = pixel[1]
        blue = pixel[2]
        print(f"Red Value is {red}")
        print(f"Green Value is {green}")
        print(f"Blue Value is {blue}")

        # Transform the pixel
        eRed = (red - key) % 256
        eGreen = (green - key) % 256
        eBlue = (blue - key) % 256
        
        print(f"Manipulated Red Value is {eRed}")
        print(f"Manipulated Green Value is {eGreen}")
        print(f"Manipulated Blue Value is {eBlue}")
        
        # Set Pixel in new Image
        dPixels[i,j] = (int(eRed), int(eGreen), int(eBlue))
        print(pixels[i,j])
    # print(i)
deencrptedImage.show()
newimage.save('checkEncrypted.jpeg')
