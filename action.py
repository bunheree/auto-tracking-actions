import time

# App import
from package.appActions.info import getAppName
from package.appActions.switch import switchApp
from package.click.basic import randomClick
from package.typing.basic import press

# screen size is 1728x1117

def customActions():
    while(True):
        # START: Press right only for 2 apps 95629, 810
        while(True):
            if(getAppName() == 'Code' or getAppName() == 'PhpStorm'):
                press()
            else:
                break      
        # END.

        # START: Random click
        while(True):
            if(getAppName() == 'Code' or getAppName() == 'PhpStorm'):
                break
            else:
                randomClick()
        # END: Random click

        time.sleep(1)

def init():
    # --- This line for check current position --
    # print(pyautogui.position())
    # time.sleep(2)

    # randomClick()
    customActions()

    
init()
# Document:  https://pyautogui.readthedocs.io/en/latest/keyboard.html