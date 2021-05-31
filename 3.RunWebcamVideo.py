import cv2
import numpy
#using cv2.VideoCapture(0) lets you capture footage from your webcam.
video1=cv2.VideoCapture(0)
frameWidth=480
frameHeight=360
#sets width of window
#video1.set(3,frameWidth)
#sets height of window
#video1.set(4,frameHeight)
#these functions only resize to conventional resolutions so it's more convenient to use cv2.resize

while True:
    success,img=video1.read()
    #this version of resize lets you resize to anything
    img= cv2.resize(img,(frameWidth,frameHeight))
    cv2.imshow('TestVideo',img)
    key=cv2.waitKey(40)
    if key & 0xFF==ord('q'):                      #
        print('done')
        break
