import numpy as np
import cv2
from numpy.core.fromnumeric import resize

# refer http://amroamroamro.github.io/mexopencv/opencv/contours_hierarchy_demo.html (Old documentation but easy to understand)
# New documentation:
# https://docs.opencv.org/master/d9/d8b/tutorial_py_contours_hierarchy.html
# https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html
# https://docs.opencv.org/master/d3/dc0/group__imgproc__shape.html#ga8d26483c636be6b35c3ec6335798a47c
# https://stackoverflow.com/questions/65200011/what-does-cv2-approxpolydp-return


def empty(a):
    pass

def GetContours(img,imgContour,PresetArea=1000):
    # returns all contours and heirarchy of contours
    # some shapes are inside other shapes like nested figures.We call outer one as parent and inner one as child. 
    # This way, contours in an image has some relationship to each other
    #cv2.RETR_EXTERNAL means that only overall shape will be considered and shapes within shapes will not be considered
    #cv2.CHAIN_APPROX_NONE means that every point in the contour is stored and there is no compression
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    #We only need contours which form bigger shapes, so we iterate through all contours and disregard shapes which have small areas
    for cnt in contours:
        #finds the area within a given contour
        area=cv2.contourArea(cnt)

        if area>PresetArea:
            #draws the contour
            #third argument is index of contours (useful when drawing individual contour. To draw all contours, pass -1
            cv2.drawContours(imgContour,cnt,-1,(255,0,255),3)

            #Finds arc length/perimeter of contour. True/False is given depending on whether the curve is closed or not
            perimeter=cv2.arcLength(cnt,True)

            #Approximates a polygonal curve(s) with the specified precision.
            #The function cv::approxPolyDP approximates a curve or a polygon with another curve/polygon with less vertices so that 
            # the distance between them is less or equal to the specified precision
            #cv2.approxPolyDP returns a resampled contour, so this will still return a set of (x, y)
            approx=cv2.approxPolyDP(cnt,0.02*perimeter,True)
            
            
            #The cv2.boundingRect() function of OpenCV is used to define an approximate rectangle around the binary image. 
            # This function is used mainly to highlight the region of interest after obtaining contours from an image.
            #The function cv2. boundingRect() returns the 4 points of the bounding box.
            x_,y_,w,h=cv2.boundingRect(approx)
            
            #Draw the rectangle defined by cv2.boundingRect()
            cv2.rectangle(imgContour,(int(x_),int(y_)),(int(x_+w),int(y_+h)),(0,255,0),int(5))

    

kernel=np.ones((5,5),np.uint8)
frameWidth=480
frameHeight=360

#New window is created
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",480,360)
#Trackbars are created and attached to the new window
cv2.createTrackbar("Threshold1","Parameters",0,150,empty)
cv2.createTrackbar("Threshold2","Parameters",255,255,empty)
cv2.createTrackbar("Area","Parameters",0,10000,empty)

#video is captured and resized
video1=cv2.VideoCapture(0)
#When you try to set random resolutionusing video.set(3,framWidth) and video.set(4,frameHeight) opencv sets nearest resolution if that resolution is not available.

while True:
    success,img=video1.read()
    #instead of resizing video feed i resized the image
    img=cv2.resize(img,(frameWidth,frameHeight))

    #decalring and initializing imgContour variable for future use
    imgContour=img.copy()

    #Blurring image to make it easier to find contours
    imgBlur=cv2.GaussianBlur(img,(7,7),1)

    #Converting blurred image to grayscale
    imgGray=cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)

    #Getting values from trackbar
    threshold1=cv2.getTrackbarPos("Threshold1","Parameters")
    threshold2=cv2.getTrackbarPos("Threshold2","Parameters")
    MinimumArea=cv2.getTrackbarPos("Area","Parameters")

    #Use canny algorithm on the image to find outlines of shapes
    imgCanny=cv2.Canny(imgGray,threshold1,threshold2)

    #Dilate the image to remove noise
    imgDil=cv2.dilate(imgCanny,np.ones((7,7),np.uint8),iterations=1)

    #Get contours
    GetContours(imgDil,imgContour,MinimumArea)
    imgCanny=cv2.cvtColor(imgCanny,cv2.COLOR_GRAY2BGR)
    imgDil=cv2.dilate(imgCanny,np.ones((7,7),np.uint8),iterations=1)
    imgGray= cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR)

    #Stack video feeds
    result1=np.hstack([img,imgGray,imgDil])
    result2=np.hstack([imgCanny,imgContour,imgContour])
    result=np.vstack([result1,result2])

    #Show feed
    cv2.imshow('TestVideo',result)
    key=cv2.waitKey(1)
    if key & 0xFF==ord('q'):                      
        break
