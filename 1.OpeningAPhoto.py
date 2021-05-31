import cv2
import numpy
#reads image
#cv2.IMREAD_UNCHANGED tells system to read transparent pixels as they are
#this prevents artefacts from occuring in the output
img=cv2.imread('Resources\Lena.jpg',cv2.IMREAD_UNCHANGED)
#shows image in new window (window name,image)
cv2.imshow("TEST IMAGE",img)
#tells how long to show the window in ms. 0 indicates infinity( till window is closed)
cv2.waitKey(0)


