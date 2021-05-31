import cv2
import numpy as np


#detecting mouse using setmousecallback


#Function to log mouse clicks
def MousePoints(event,x,y,flag,params):
 if event==cv2.EVENT_LBUTTONDOWN:
        print(x,y)
    

path='Resources\Cards.jpg'
img=cv2.imread(path)
img=cv2.resize(img,(640,480))
cv2.imshow('Image1',img)
#set mouse callback params are 1)Name of window to track 2)Fuction to call if click is detected
cv2.setMouseCallback('Image1',MousePoints)
cv2.waitKey(0)


