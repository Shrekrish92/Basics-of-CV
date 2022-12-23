import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('org',img)

plt.imshow(img)
plt.show()

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gry',gray)

# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('hsv',hsv)

# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('lab', lab)

cv.waitKey(0)