import pyautogui
import time
import random
from AppKit import NSWorkspace

# screen size is 1728x1117

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

# Swich app 
def switchApp():
    numRand = random.randrange(1,4)

    match numRand:
        case 1:
            # mail app position
            pyautogui.moveTo(x, y) # Check current position and replace app position here
        case 2:
            # slack app 
            pyautogui.moveTo(x, y)
        case 3: 
            # VScode app
            pyautogui.moveTo(x, y)
        case 4: 
            # Chrome
            pyautogui.moveTo(x, y)
        case _:
            pyautogui.click()

    pyautogui.click()

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

def keyPressAuto():
    while(True):
        nameId = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationProcessIdentifier']
        if(nameId == 95629 or nameId == 810): # Only press if the id of the app is Word or Visual code apps
            press()
        


def init():
    # --- This line for check current position --
    # print(pyautogui.position())
    # time.sleep(2)

    #keyPressAuto()
    randomClick()

    
init()
# Document:  https://pyautogui.readthedocs.io/en/latest/keyboard.html