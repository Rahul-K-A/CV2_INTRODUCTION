import cv2
path='Resources\Firewatch.jpg'

Img=cv2.imread(path)
#width and height of resized image
width,height=640,480
#IMPORTANT: (0,0) of image is in top left corner, +ve y axis is downwards from (0,0) and +ve x is rightwards of (0,0)
cv2.imshow('Firewatch',Img)
#Image.shape has 3 elements inside it:(height, width, channels).Using img.shape[0] will give you height and usign img.shape[1] will give you width
print(Img.shape)
#cv2.resize resizes image to given params. doesnt necessarily retain quality. Both minimises and increases window size
ImgResize=cv2.resize(Img,(width,height))
cv2.imshow('Resized',ImgResize)
#since images are basically arrays of pixels, you can crop images by slicing array
ImgCropped=Img[0:400,300:]
#cropped images can also be resized
#Img.shape retuens the number of columns and rows in the matrix which contains the image
ImgCroppedResized=cv2.resize(ImgCropped,(Img.shape[1],Img.shape[0]))
cv2.imshow('Cropped',ImgCropped)
cv2.imshow('Cropped Resized',ImgCroppedResized)
cv2.waitKey(0)
