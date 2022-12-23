import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('cats', img)

blur= cv.blur(img,(7,7))
cv.imshow('blured',blur)
cv.waitKey(0)