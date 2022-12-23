import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray_scale', gray)

blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)
cv.imshow('edges', canny)

contours,heirarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} countour(s) found!')

cv.waitKey(0)