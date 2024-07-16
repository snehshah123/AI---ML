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

#BGR to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
resized_image2 = rescaleImg(gray)
cv.imshow('Gray',resized_image2)

#BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
resized_image3 = rescaleImg(hsv)
cv.imshow('HSV',resized_image3)

#BGR to L*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
resized_image4 = rescaleImg(lab)
cv.imshow('LAB',resized_image4)

#BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
resized_image5 = rescaleImg(rgb)
cv.imshow('RGB',resized_image5)

cv.waitKey(0)