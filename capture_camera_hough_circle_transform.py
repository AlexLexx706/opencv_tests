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
        help(cv2.HoughCircles)
        # Convert BGR to HSV
        circles = cv2.HoughCircles(frame[:, :, 0], 1, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
        circles = np.uint16(np.around(circles))

        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)

            # draw the center of the circle
            cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)

        cv2.imshow('image',frame)
        #cv2.imshow('mask',mask)
        #cv2.imshow('res', res)
        #cv2.imshow('mask', mask)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

cv2.destroyAllWindows()