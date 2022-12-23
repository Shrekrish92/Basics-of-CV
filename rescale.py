import cv2 as cv

def rescaleframe(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width,height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat',img)
#cv.waitKey(0)

img_resized = rescaleframe(img)
cv.imshow('resized img', img_resized)

capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleframe(frame)
    cv.imshow('Dog',frame)
    cv.imshow('resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

