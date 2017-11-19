'''
testing pyautogui
'''


import pyautogui


pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)

try:
    while True:
        pass
except KeyboardInterrupt:
    print('done')
'''
x, y = pyautogui.position()
while True:
    if (x, y) != pyautogui.position():
        x, y = pyautogui.position()
        print(x, y)'''

#pyautogui.click(31, 50)
'''while True:
    pyautogui.moveTo(100, 150)'''

'''currentMouseX, currentMouseY = pyautogui.position()
>>> pyautogui.moveTo(100, 150)
>>> pyautogui.click()
>>> pyautogui.moveRel(None, 10)  # move mouse 10 pixels down
>>> pyautogui.doubleClick()
>>> pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.
>>> pyautogui.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
>>> pyautogui.press('esc')
>>> pyautogui.keyDown('shift')
>>> pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
>>> pyautogui.keyUp('shift')
>>> pyautogui.hotkey('ctrl', 'c')'''
