import cv2
import numpy as np

def on_change(v):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('image')
cv2.createTrackbar('sv_min', 'image', 200, 255, on_change)
cv2.createTrackbar('h_pos', 'image', 0, 255, on_change)
cv2.createTrackbar('h_wnd', 'image', 30, 255, on_change)

while(1):

    # Take each frame
    res, frame = cap.read()
    kernel = np.ones((5,5),np.uint8)

    if res:
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #hsv = frame[:, :, 0]

        # define range of blue color in HSV
        sv_min = cv2.getTrackbarPos('sv_min','image')
        h_pos = cv2.getTrackbarPos('h_pos','image')
        h_wnd = cv2.getTrackbarPos('h_wnd','image')

        lower_blue = np.array([h_pos, sv_min, sv_min])
        upper_blue = np.array([h_pos + h_wnd, 255, 255])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        #mask = cv2.GaussianBlur(mask,(5,5),0)
        #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #ret, mask = cv2.threshold(hsv, h_pos, 255, cv2.THRESH_BINARY)
        #cv2.imshow('image', mask)

        #contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

        #Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame, frame, mask= mask)

        cv2.imshow('mask',mask)
        cv2.imshow('res', res)
        #cv2.imshow('mask', mask)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
 
cv2.destroyAllWindows()