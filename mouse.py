import pyautogui as gui
import time
import os
#import keyboard
#import subprocess

time.sleep(1)
# gui.moveTo(0,0,3)

a = gui.position()
print(gui.position())
while(True):
    #safeguard = 0
    #if keyboard.is_pressed('alt'):
    #    safeguard = 1
    time.sleep(0.5)
    b = gui.position()
    time.sleep(0.5)
    if a != b: #or safeguard==1:
        os.system('xdg-open /home/euller/Pictures/fswebcam/freddy1.gif')
        os.system('fswebcam -r 640x480 --jpeg 85 -D 1 /home/euller/Pictures/fswebcam/web-cam-shot.jpg')	
        gui.typewrite('h')        
        time.sleep(1)
        os.system('xdg-open /home/euller/Pictures/fswebcam/web-cam-shot.jpg') 
        time.sleep(0.5) 
        gui.typewrite('h') 
        time.sleep(1.5)
        os.system('xdg-open /home/euller/Pictures/fswebcam/joker.gif') 
        time.sleep(0.5)
        gui.typewrite('h') 
        time.sleep(2.5)
        gui.typewrite('w') 
        break
time.sleep(2.5)
os.system('systemctl suspend')
