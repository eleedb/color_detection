import os
import cv2
import numpy as np
from PIL import Image

def get_limits(color):
    c = np.uint8([[color]])# we are only going to use 8 bits instead of 32 (with 8 bits we achieve 255(white)
                           #instead of writing a code that looks if it is above 255 we limit the capacity to 255 and we discard the carry
    hsvc = cv2.cvtColor(c,cv2.COLOR_BGR2HSV)#change values rgb to hsv

    lower_limit = hsvc[0][0][0] - 10, 100, 100
    upper_limit = hsvc[0][0][0] + 10, 255, 255 #creates the range of colors that we are going to detect

    lower_limit = np.array(lower_limit, dtype=np.uint8)
    upper_limit = np.array(upper_limit, dtype=np.uint8) #this transforms it into a numpy array (opencv works with arrays)
                                                        
    return lower_limit, upper_limit

def main():
    capt = cv2.VideoCapture(0) #creates an array with the rgb scale of each pixel that the camera captures
    while True: #loop that updates what is seen on camera and makes it look like a video
        ret, frame = capt.read()
        
        #yellow = [0,255, 255]
        yellow = [87 ,213, 222]
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_limit, upper_limit = get_limits(color=yellow)
        mask = cv2.inRange(hsv_image, lower_limit, upper_limit)#mask is what make it show only the pixels with the specific color

        cv2.imshow("frame", mask) #this shows the image, if you want to see video instead change "mask" for "frame
        
        if cv2.waitKey(1) & 0xFF == ord("l"): #this is for closing the video clicking "l"
            break
    capt.release()
    cv2.destroyAllWindows

if __name__ == "__main__":
    main()
