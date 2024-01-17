import pyautogui
import random

from ..appActions.info import getAppId

def press():
    pyautogui.press('right') # Press arrow right key 

def keyDown():
    pyautogui.keyDown()

def keyUp():
    pyautogui.keyUp()

# Random press action
def randomTyping():
    numRand = random.randrange(1,3)

    match numRand:
        case 1:
            press()
        case 2:
            keyDown()
        case 3: 
            keyUp()
        case _:
            pyautogui.click()

def keyPressAuto():
    while(True):
        if(getAppId() == 95629 or getAppId() == 810): # Only press if the id of the app is Word or Visual code apps
            press()