import pyautogui as gui
import time

number = input("How many cycles, daddy? ")
time.sleep(5)

count = 375

for i in range(int(number)):
    
    time.sleep(1)
    gui.hotkey('ctrl', 'f')
    time.sleep(1)
    gui.typewrite("%")
    
    time.sleep(1)
    gui.hotkey('ctrl', 'f')
    time.sleep(1)
    gui.typewrite("download")
    time.sleep(1)
    gui.hotkey('ctrl', 'Enter')
    time.sleep(1)
    gui.hotkey('ctrl', 'f')
    time.sleep(1)
    gui.typewrite("download")
    time.sleep(1)
    gui.hotkey('ctrl', 'Enter')
    time.sleep(10)
    gui.typewrite(str(count))
    time.sleep(2)
    gui.press('Enter')
    time.sleep(1)
    count += 1
    
    time.sleep(3)
    gui.hotkey('ctrl', 'f')
    time.sleep(1)
    gui.typewrite("Complete and Continue")
    time.sleep(1)
    gui.hotkey('ctrl', 'Enter')
    time.sleep(3)
