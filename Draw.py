import cv2 as cv
import numpy as np

'''
img = cv.imread(r"D:\Space\IMG_0006.JPG")

#rescaling and resizing
def rescaleImg(img,scale = 0.1):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(img,dimensions,interpolation=cv.INTER_AREA)

resized_image = rescaleImg(img)
cv.imshow('Image',resized_image)
'''

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#blank[200:300,300:400] = 0,255,0
#cv.imshow('Green',blank)
 
#Rectangle
rectangle = cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,0,255),thickness=-1)
cv.imshow('Rectangle',rectangle)

#circle
Circle=cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(255,0,0),thickness=-1)
cv.imshow('Circle',Circle)          

#Line
Line = cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)
cv.imshow('Line',Line)

#Text
text= cv.putText(blank,'Hi Sneh',(255,255),cv.FONT_HERSHEY_COMPLEX,1.0,(255,255,0),2)
cv.imshow('Text',text)

cv.waitKey(0)

