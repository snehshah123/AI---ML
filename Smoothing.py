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

#Averaging
average = cv.blur(resized_image1,(3,3))
cv.imshow('Average',average)

#Gaussian Blur
gauss = cv.GaussianBlur(resized_image1,(3,3),0)
cv.imshow('Gaussian Blur',gauss)

#Median Blur
median = cv.medianBlur(resized_image1,3)
cv.imshow('Median',median)

#Bilateral #Most Effective
bilateral = cv.bilateralFilter(resized_image1,5,35,25)
cv.imshow('Bilateral',bilateral)

cv.waitKey(0)