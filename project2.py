#screenshot in Python
import pyscreenshot as ImageGrab
#import for video
import numpy as np
import cv2
#fullscreen
#im=imageGrab.grab()
im.show()
#part of the screen
xone=raw_input("Enter X1:")
xtwo=raw_input("Enter X2:")
yone=raw_input("Enter Y1:")
ytwo=raw_input("Enter Y2:")
while(True)
    im=imageGrab.grab(bbox=(%xone,%yone,%xtwo,%ytwo))
#to file
#ImageGrab.grab_to_file('im.png')
#capture frames from the screen
#cv2.VideoWriter.open(filename, fourcc, fps, frameSize[, isColor])
#fourcc: http://www.fourcc.org/codecs.php
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imshow("test", frame)
    cv2.waitKey(0)
cv2.destroyAllWindows()
#http://docs.opencv.org/3.0-beta/modules/videoio/doc/reading_and_writing_video.html
#https://docs.python.org/3.0/library/time.html
#http://stackoverflow.com/questions/24374620/python-loop-to-run-for-certain-amount-of-seconds
from PIL import ImageGrab
import time
time.sleep(5)
ImageGrab.grab().save("screen_capture.jpg", "JPEG")
#time loop: until the time is passed, do stuff
import time

t_end = time.time() + 60 * 15
while time.time() < t_end:
    #do stuff

