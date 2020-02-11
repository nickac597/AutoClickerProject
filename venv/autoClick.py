#Author: Nicholas Catalano
import pyautogui
import random

avgRand = 0

mousePos = pyautogui.position()
i = 1
# loop 160 clicks
while i < 160:
    print("click: ", i)
    i += 1
    # End of range of both randoms added = 60 seconds
    # Takes each random pause and adds them together
    randPause = random.uniform(0.01, 49.24)
    randPause2 = random.uniform(0.01, 10.76)
    totalPause = randPause + randPause2

    # click at initial position and pause for the totalPause found earlier
    pyautogui.doubleClick(x=mousePos.x, y=mousePos.y)
    pyautogui.PAUSE = 2
    # move the mouse by positive or negative 8 pixels on each axis
    # relative to the positon of the mouse
    randMove = random.uniform(-8, 8)
    randMove2 = random.uniform(-8, 8)
    pyautogui.moveRel(randMove, randMove2, )
