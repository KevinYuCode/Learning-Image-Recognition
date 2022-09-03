from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)

while keyboard.is_pressed('q') == False:
    #Each index represents an rgb value respectively: r -> [0] g -> [0] b->[0]
    if pyautogui.pixel(531, 800)[0] == 0: #Checks if the R value is 0 at x:581, and y:400
        click(531, 800)
    if pyautogui.pixel(624, 800)[0] == 0: #Checks if the R value is 0 at x:624, and y:400
        click(624, 800)
    if pyautogui.pixel(733, 800)[0] == 0: #Checks if the R value is 0 at x:733, and y:400
        click(733, 800)
    if pyautogui.pixel(840, 800)[0] == 0: #Checks if the R value is 0 at x:733, and y:400
        click(840, 800)