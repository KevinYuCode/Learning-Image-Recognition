from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

while 1:
    if pyautogui.locateOnScreen('./Assets/Stickman.png', region=(40, 0, 500, 1000), grayscale=True, confidence=0.8) != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("i am unable to see it")
    time.sleep(0.5)
