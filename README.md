# About: auto-tracking-actions
This src aids in the execution of random clicks or keyboard presses. <br>
<b>Keep the screen from freezing!</b>

## The Ideas
- `randomClick()` The click will be auto with a random time of 1-2 minutes and a random spot.
- `keyPressAuto()` 
    - Replace `'right'` text in `press()` for they key you want to press auto
    - Replace nameId condition `(nameId == 95629 or nameId == 810)` with the id of the app can auto press
        - For check the `nameId` you can use `print(nameId)` with `time.sleep(3)` and move to the app current to see it `nameId`
- `switchApp()` Auto switch app after random time. You need check the app position with `print(pyautogui.position())`

## Run
```
python3 /auto-tracking-actions/index.py
```
