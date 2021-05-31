import cv2

video1=cv2.VideoCapture('Resources\VoxelBuilding.mp4')


while True:
     #video.read() returns a boolean and an image. the boolean value tells us whether the video was successfully read
    success,image=video1.read()
    #You can check the video has successfully been read for additional safety but it's not needed for now
    #if success==True:
    cv2.imshow('TestVideo',image)
    #cv2.waitkey(Time) shows the image and waits for Time milliseconds for an input from the user. Set Time=1/[Framrate of video] for best results 
    key=cv2.waitKey(16)
    #If a key is pressed during cv2.waitkey it is stored as an integer in key variable
    #We want to quit the video if we press 'q'
    #We use bitwise AND to check if we have pressed the right key
    #ord(letter) returns the unicode integer of the character passed through it. For q unicode value is 71
    #To reduce errors we use 0xFF which is a bit mask to reduce key variable to it's 8 smallest bits.
    if key & 0xFF==ord('q'):                      
        break
#Closes video file or capturing device.
video1.release()
#Destroys all windows
cv2.destroyAllWindows()
print('done')
