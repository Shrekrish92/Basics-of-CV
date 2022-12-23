import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('PArk',img)

#converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('bnw',gray)

#blurring
blur = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)
cv.imshow('blured',blur)

#edge detection
can = cv.Canny(img,125,175)
cv.imshow('edges', can)

#dilating the image using the edge detected image.
dil = cv.dilate(blur,(3,3),iterations=1)
cv.imshow('dilated',dil)

cv.waitKey(0)