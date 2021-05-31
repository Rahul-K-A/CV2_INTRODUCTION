from typing import Counter
import cv2
import numpy as np
from numpy.lib.type_check import _imag_dispatcher

#Warping: Transorming perspective within an image
#Need two sets of points for warping
#Points 1: Set of coordinates of vertices of object that needs to be warped into new position
#Points 2: Set of vertices which represent the new coordinates of vertices
#Step 1 : Get relative transform between the two perspectives using cv2.getPersspectiveTransform()
#Step 2: Warp the original image using cv2.warpPerspective()
#Vertices will be selected by clicking on them
#Order of selection shouold be top left, top roght, bottom left, bottom right

#create empty matrix
circles=np.zeros((4,2),np.int16)
#keep counter to keep track of mouse clicks
counter=0
#function to set vertices.It takes 5 outputs from cv2.setmousecallback() as input
def MousePoints(event,x,y,flag,params):
     global counter
     if event==cv2.EVENT_LBUTTONDOWN: 
        print(x,y)
        if counter<=3:
            #Adding elements to matrix  
            circles[counter]=[x,y]
            cv2.circle(img,(circles[counter][0],circles[counter][1]),5,(0,0,255),cv2.FILLED)
        counter=counter+1

path="Resources/Cards.jpg"
img=cv2.imread(path)
width,height=250,350
img=cv2.resize(img,(640,480))
while True:
    
    if counter>3:
        pts1=np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix=cv2.getPerspectiveTransform(pts1,pts2)
        img_output=cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow('Output',img_output)
        cv2.waitKey(0)
    cv2.imshow('OG image',img)
    cv2.setMouseCallback('OG image',MousePoints)
    cv2.waitKey(1)