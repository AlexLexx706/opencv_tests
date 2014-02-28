import cv2
import numpy as np


def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('image')
cv2.createTrackbar('pos', 'image', 0, 255, nothing)
cv2.createTrackbar('wnd', 'image', 0, 50, nothing)

while(1):

    # Take each frame
    res, frame = cap.read()
    if res:
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #hsv = frame[:, :, 0]

        # define range of blue color in HSV
        pos = cv2.getTrackbarPos('pos','image')
        wnd = cv2.getTrackbarPos('wnd','image')

        lower_blue = np.array([pos, 100, 100])
        upper_blue = np.array([pos + wnd, 255, 255])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        #ret, mask = cv2.threshold(hsv, pos, 255,cv2.THRESH_BINARY)
        cv2.imshow('image', mask)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

        # Bitwise-AND mask and original image
        #res = cv2.bitwise_and(frame, frame, mask= mask)

        #cv2.imshow('frame',frame)
        #cv2.imshow('mask',mask)
        #cv2.imshow('res', res)
        #cv2.imshow('mask', mask)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

cv2.destroyAllWindows()