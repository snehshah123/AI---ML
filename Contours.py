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

blank = np.zeros(resized_image1.shape,dtype ='uint8')
cv.imshow('Blank',blank)

#Convert to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
resized_image2 = rescaleImg(gray)
cv.imshow('Gray',resized_image2)

#Edge Cascade
canny = cv.Canny(img,125,175)
resized_image3= rescaleImg(canny)
cv.imshow('Canny',resized_image3)

#Contours

ret,thresh = cv.threshold(gray,125,225,cv.THRESH_BINARY)
resized_image4= rescaleImg(thresh)
cv.imshow('Thresh',resized_image4)

contours,hierarchies = cv.findContours(resized_image3,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found !')

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours Drawn',blank)

cv.waitKey(0)