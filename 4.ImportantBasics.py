import cv2
import numpy as np

#n.ones() creates array full of 1s of specified size and type
kernel=np.ones((5,5),np.uint8)

print(kernel)
path="Resources/Lena.jpg"
#adding 0 to params in imread dierctly converts it into greyscale
Img=cv2.imread(path)
#cv2 uses BGR colorspace
#cvtcolor converts from one colorspace to another.Here converts to BGR to Greyscale
ImgGray=cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)
#gaussianBlur blurs objects (src,Kernal size[this param defines blurrinesss{higher thr better} ],Sigma)
ImgBlur=cv2.GaussianBlur(ImgGray,(7,7),0)
#Canny provides photo with just the edges.Basically edge detection func.Threshold values define number of edges. Lower=more edges
ImgCanny=cv2.Canny(ImgBlur,100,200)
#Dilation: Kernal array goes through the image, if white pixel found,it turns the area defined by kernal white
ImgDilate=cv2.dilate(ImgCanny,kernel,iterations=1)
#Erosion: Kernal array goes through the image, if black pixel found,it turns the area defined by the kernel black 
ImgErode=cv2.erode(ImgDilate,kernel,iterations=1)

#Image display section
success=cv2.imshow('Lena',Img)
success=cv2.imshow('Greyscaled Lena',ImgGray)
success=cv2.imshow('Blurred Lena',ImgBlur)
success=cv2.imshow('Edge Detected Lena',ImgCanny)
success=cv2.imshow('Dilated Lena',ImgDilate)
success=cv2.imshow('Eroded Lena',ImgErode)
cv2.waitKey(0)