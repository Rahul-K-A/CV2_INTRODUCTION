import cv2
import numpy as np
import copy
#while using np np.zeroes/np.ones order is (width,height)
#OpenCV can read arrays as images, if arr[x]=0, blacl pixel. If arr[x]=255, white pixel.Anything in between is a shade of gray
BlackAndWhiteImage=np.zeros((480,640),np.uint8)
print(BlackAndWhiteImage)

#OpenCV can read arrays as images, if arr[x]=0, blacl pixel. If arr[x]=255, white pixel.Anything in between is a shafe of gray
BlackAndWhiteImageWithEdit=copy.deepcopy(BlackAndWhiteImage)
BlackAndWhiteImageWithEdit[240:250,320:330]=255
print(BlackAndWhiteImageWithEdit)
#To add colour functionality youve to make array 3d. now brg channel is enabled 
ColorImage=np.zeros((480,640,3),np.float32)
print(ColorImage)
ColorImageEdit=copy.deepcopy(ColorImage)
#if 255,0,0 blue. if 0,255,0 green. if 0,0,255, red. 0,0,0 black. 255,255,255 white
ColorImageEdit[240:250,320:330]=(255,0,0)
print(ColorImageEdit)
#cv2.line draws a line in the image
cv2.line(ColorImageEdit,(0,0),(ColorImage.shape[1],ColorImage.shape[0]),(0,255,0),1)
#cv2.rectangle draws a rectangle in the image when the two furthest vertices are defined
cv2.rectangle(ColorImageEdit,(0,0),(320,240),(255,255,255),2)
#cv2.circle draws circle when origin, radius are defined
cv2.circle(ColorImageEdit,(320,240),10,(0,0,255))
#cv2.putText displays text when bottom left starting point,Text, and font are defined
cv2.putText(ColorImageEdit,"This is a test",(330,240),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1,)
cv2.imshow("Black",BlackAndWhiteImage)
cv2.imshow("Black and White",BlackAndWhiteImageWithEdit)
cv2.imshow("Blank color image",ColorImage)
cv2.imshow("color image",ColorImageEdit)

cv2.waitKey(0)