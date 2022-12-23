import cv2 as cv
import numpy as np
img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray cats', gray)

threshold, thresh = cv.threshold(gray, 50, 255, cv.THRESH_BINARY)
cv.imshow('simple threshold', thresh)

threshold, thresh_i = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('inverse threshold', thresh_i)


cv.waitKey(0)