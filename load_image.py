import numpy as np
import pyopencv as cv2

# Load an color image in grayscale
img = cv2.imread('IMG.jpeg',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('1.png', img)