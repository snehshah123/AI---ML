import cv2 as cv
import numpy as np

img = cv.imread(r"D:\Space\Space\WhatsApp Image 2022-05-25 at 11.52.29 AM.jpeg")

#rescaling and resizing
def rescaleImg(img,scale = 0.5):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(img,dimensions,interpolation=cv.INTER_AREA)

resized_image1 = rescaleImg(img)
cv.imshow('My Photos',resized_image1)

b,g,r = cv.split(resized_image1)

cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)

print(img.shape)
print(resized_image1.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image',merged) 

blank = np.zeros(resized_image1.shape[:2],dtype ='uint8')
cv.imshow('Blank',blank)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("Blue2",blue)
cv.imshow("Green2",green)
cv.imshow("Red",red)

cv.waitKey(0)