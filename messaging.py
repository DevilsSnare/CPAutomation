import pyautogui
import time

time.sleep(5)
for i in range(0, 200):
    pyautogui.typewrite("wasssup!")
    pyautogui.press('enter')
    time.sleep(1)