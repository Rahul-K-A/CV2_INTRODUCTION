import cv2
import numpy as np

#path1 and 2 are paths to two dIfferent images

#you can combine various images/videos using numpys hstack and vstack functions
#COMBINATION CAN ONLY BE DONE WHEN NUMBER OF COLOR CHANNELS ARE SAME. FOR EXAMPLE GREYSCALE(1 channel ) AND BGR(3 channels) 
#CAN'T BE USED TOGETHER BUT RGB(3 channel) AND BGR(3 channel) CAN BE USED TOGETGHER

#BOTH IMAGES NEED TO BE OF THE SAME SIZE TO BE STACKED SO BE SURE TO RESIZE BOTH IMAGES TO SAME WIDTH AND HEIGHT

path1="Resources\Firewatch.jpg"
path2="Resources\Lena.jpg"

width=480
height=360

img1=cv2.imread(path1)
img2=cv2.imread(path2)
#img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img1=cv2.resize(img1,(width,height))
img2=cv2.resize(img2,(width,height))

ver=np.vstack((img1,img2))
hor=np.hstack((img1,img2))
cv2.imshow('Vertical stack',ver)
cv2.imshow('Horizontal stack',hor)
cv2.waitKey(0)
