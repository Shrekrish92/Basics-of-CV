import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype = 'uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

bit_and = cv.bitwise_and(rectangle,circle)
cv.imshow('AND', bit_and)

bit_or = cv.bitwise_or(rectangle,circle)
cv.imshow('OR', bit_or)

bit_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('XOR', bit_xor)

bit_not1 = cv.bitwise_not(rectangle)
cv.imshow('NOT1', bit_not1)

bit_not2 = cv.bitwise_not(circle)
cv.imshow('NOT2', bit_not2)

cv.waitKey(0)