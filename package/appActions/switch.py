import random
import pyautogui

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