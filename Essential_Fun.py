import cv2 as cv

img = cv.imread(r"D:\Space\Space\WhatsApp Image 2022-05-25 at 11.52.29 AM.jpeg")
#rescaling and resizing
def rescaleImg(img,scale = 0.5):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(img,dimensions,interpolation=cv.INTER_AREA)

resized_image1 = rescaleImg(img)
cv.imshow('Image',resized_image1)

#Convert to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

resized_image2 = rescaleImg(gray)
cv.imshow('Gray',resized_image2)

#BLUR
blur =cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
resized_image3 = rescaleImg(blur)
cv.imshow('Blurred',resized_image3)

#Edge Cascade
canny = cv.Canny(img,125,175)
resized_image4= rescaleImg(canny)
cv.imshow('Canny',resized_image4)

#Dilating
dilated = cv.dilate(canny,(7,7),iterations=1)
resized_image5= rescaleImg(dilated)
cv.imshow('Dilated',resized_image5)

#Eroding
eroded = cv.erode(dilated,(3,3),iterations=3)
resized_image6= rescaleImg(dilated)
cv.imshow('Eroded',resized_image6)

#Resize
resized=cv.resize(resized_image1,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#Cropping
cropped = resized_image1[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0) 