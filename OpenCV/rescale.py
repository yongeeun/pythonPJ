import cv2 as cv

img = cv.imread('Photos/sample.png')
cv.imshow('sample', img)

def rescaleFrame(cv2(frame), scale=0.75):
    width = int(frame.shape[1] *scale)
    height = int(frame.shape[0] *scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# cv.waitKey(0)

def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)


resized_image = rescaleFrame(img)


capture = cv.VideoCapture('Video/IMG_5831.MOV')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, .2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()