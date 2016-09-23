#screenshot in Python
import pyscreenshot as ImageGrab
#import for video
import numpy as np
import cv2
#fullscreen
im=imageGrab.grab()
im.show()
#part of the screen
xone=raw_input("Enter X1:")
xtwo=raw_input("Enter X2:")
yone=raw_input("Enter Y1:")
ytwo=raw_input("Enter Y2:")
im=imageGrab.grab(bbox=(%xone,%yone,%xtwo,%ytwo))
#to file
ImageGrab.grab_to_file('im.png')
#capture frames from the screen
cv2.VideoWriter.open(filename, fourcc, fps, frameSize[, isColor])
#fourcc: http://www.fourcc.org/codecs.php
