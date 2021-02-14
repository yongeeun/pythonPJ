import cv2 as cv

# img = cv.imread('Photos/sample.png')
# cv.imshow('sample', img)
# cv.waitKey(0)

capture = cv.VideoCapture('Video/IMG_5831.MOV')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()