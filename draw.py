import cv2 as cv
import numpy as np

# img = cv.imread('Photos/Cat.jpg')
# cv.imshow('Cat',img)
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank', blank)
blank[200:300, 300:400] = 255,0,0
cv.imshow('green', blank)

#making a rectangle
cv.rectangle(blank,(0,0),(300,300),(255,0,250), thickness=2)

#draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),60,(100,20,90), thickness=-1)

#draw a line
cv.line(blank,(0,0),(500,500),(0,255,0), thickness=4)

#write text
cv.putText(blank,'Hello!!!!!', (200,280), cv.FONT_HERSHEY_TRIPLEX, 1,(255,255,255), thickness=3)

cv.imshow('rect', blank)
cv.waitKey(0)