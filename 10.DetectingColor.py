
import numpy as np
import cv2
#detecting colors can be done by setting the minimum and maximmum values for the pixel values
#instad of using bgr or rgb, hsv is used because its more intuitive
#   H:0-179(0-359 usually) , S:0-255 , V:0-255
#empty function just to satisy the cv2.resizeWindow() params
def empty(a):
    pass

frameWidth=320
frameHeight=240
vidCap=cv2.VideoCapture(0)
#sets frame (window) width and height 
vidCap.set(cv2.CAP_PROP_FRAME_WIDTH,frameWidth)
vidCap.set(cv2.CAP_PROP_FRAME_HEIGHT,frameHeight)
#instad of hardcoding values, its more easier to use sliders to dyunamically adjust values
#New window is created
cv2.namedWindow("HSV")
#Trackbars are created and attached to the new window
#cv2::createTrackbar(NameOfTrackbar,WindowName,StartingPositionOfSlider(Doesnt affect slider values.Slider values will always be between 0-MaxValueOfSlider.It simply affects starting value of slider),MaxValueOfSlider,FunctionCalledWhenTrackbar)
#For now no function needs to be called while TrackbarValue changes so we can pass empty
cv2.createTrackbar("HUE min","HSV",0,179,empty)
cv2.createTrackbar("HUE max","HSV",0,179,empty)
cv2.createTrackbar("SAT min","HSV",0,255,empty)
cv2.createTrackbar("SAT max","HSV",0,255,empty)
cv2.createTrackbar("VAL min","HSV",0,255,empty)
cv2.createTrackbar("VAL max","HSV",0,255,empty)


#while loop to display video feed
while True:
    success,img=vidCap.read()
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    #gets position of trackbar and converts it to usable value
    HueMinimum=cv2.getTrackbarPos("HUE min","HSV")
    HueMaximum=cv2.getTrackbarPos("HUE max","HSV")
    SaturationMinimum=cv2.getTrackbarPos("SAT min","HSV")
    SaturationMaximum=cv2.getTrackbarPos("SAT max","HSV")
    ValueMinimum=cv2.getTrackbarPos("VAL min","HSV")
    ValueMaximum=cv2.getTrackbarPos("VAL max","HSV")
    #two arrays are created which denote minimum and maximum acceptale range of values
    LowRange=np.array([HueMinimum,SaturationMinimum,ValueMinimum])
    HighRange=np.array([HueMaximum,SaturationMaximum,ValueMaximum])
    #mask is an array of booleans which has value 1 if Lowrange<=pixel<=Highrange and otherwise has 0 
    Mask=cv2.inRange(imgHSV,LowRange,HighRange)
    #we want to black out just the pixels which do not have the required values so we AND the img with itself and then use mask to black out the unwanted values
    Result=cv2.bitwise_and(img,img,mask = Mask)

   
    #Converts to BGR so that its possible to hStack
    Mask=cv2.cvtColor(Mask,cv2.COLOR_GRAY2BGR)
    final=np.hstack([img,Mask,Result])
    cv2.imshow("Output",final)

    key=cv2.waitKey(40)
    if key & 0xFF==ord('q'):                      #0xFF is a bit mask to reduce key to 8 bits
        print('done')
        break
