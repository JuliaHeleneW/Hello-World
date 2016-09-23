#screenshot in Python
import pyscreenshot as ImageGrab
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
