import pyautogui
import time

print("start")
while True:
    pyautogui.keyDown("r")
    pyautogui.keyUp("r")
    time.sleep(1)