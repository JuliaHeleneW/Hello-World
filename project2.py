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
