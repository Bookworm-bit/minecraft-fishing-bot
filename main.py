import keyboard
import pyautogui
import win32api
import win32con
import time
import numpy as np
import random
from PIL import Image

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.1, 0.4))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

# click(900, 300)  
f1 = Image.open('s').convert('RGBA')
f1_array = np.array(f1)
e = np.matrix(f1_array.ravel())

print(e)