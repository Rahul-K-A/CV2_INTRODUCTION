import cv2
import numpy as np
from numpy.lib.type_check import _imag_dispatcher

#Warping: Transorming perspective within an image
#Need two sets of points for warping
#Points 1: Set of coordinates of vertices of object that needs to be warped into new position
#Points 2: Set of vertices which represent the new coordinates of vertices
#Step 1 : Get relative transform between the two perspectives using cv2.getPersspectiveTransform()
#Step 2: Warp the original image using cv2.warpPerspective()
#For now vertices are hard coded. Edge detection will be implemented later

path="Resources/Cards.jpg"

img=cv2.imread(path)
width,height=250,350
#The vertices were found by hand. MS Paint shows the coordinates of where cursor is on top of image so i recommend that.
pts1=np.float32([[955,516],[1358,562],[711,936],[1146,1031]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
#Gets the relative perspective between the two sets of points
matrix=cv2.getPerspectiveTransform(pts1,pts2)
print(matrix)
img_output=cv2.warpPerspective(img,matrix,(width,height),)
print(img_output)
for x in range(0,4):
    cv2.circle(img,(pts1[x][0],pts1[x][1]),20,(0,0,255),cv2.FILLED)


img=cv2.resize(img,(512,288))
cv2.imshow('OG image',img)
cv2.imshow('Output',img_output)
cv2.waitKey(0)