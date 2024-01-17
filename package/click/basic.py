import pyautogui
import time
import random

def randomClick():
    while(True):
        # Random position
        x, y = random.randrange(100, 1500), random.randrange(100, 1000)

        # move mouse to that position
        pyautogui.moveTo(x, y)
        # click
        pyautogui.click()
        # time delay for action
        randomTime = random.randrange(60,120)
        time.sleep(randomTime) 