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

blank = np.zeros(resized_image1.shape[:2],dtype ='uint8')
cv.imshow('Blank',blank)

#Mask
mask = cv.circle(blank,(resized_image1.shape[1]//2,resized_image1.shape[0]//2),100,255,-1)
cv.imshow('Mask',mask)

masked = cv.bitwise_and(resized_image1,resized_image1,mask=mask)
cv.imshow('Masked',masked)

cv.waitKey(0)