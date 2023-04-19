import time
import pyautogui
from PIL import Image
import mss
import cv2
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

URL = "https://trex-runner.com/"
Chrome = Image.open("chrome.png")
obstacle = "cactus.png"
name_input = "name.png"
game_over = "game over.png"
player = "player.png"

# Open the browser
chrome_x, chrome_y = pyautogui.locateCenterOnScreen(Chrome, confidence=0.9)
pyautogui.click(chrome_x, chrome_y)
time.sleep(1)

# Go to the website
pyautogui.write(URL)
pyautogui.press("enter")
time.sleep(2)

# Enter name for score keeping
try:
    name_x, name_y = pyautogui.locateCenterOnScreen(name_input, confidence=0.9)
    pyautogui.click(name_x, name_y)
    name = pyautogui.prompt(text='Please write your name', title='Name for scoreboard' , default='')
    pyautogui.write(name)
    pyautogui.press("enter")
except TypeError:
    pass

# Start Game
width = 12
height = 5
# print(left, top, width, height)

pyautogui.press("space")
game_on = True
while game_on:
    gameover = pyautogui.locateCenterOnScreen(game_over, confidence=0.9)
    if gameover is not None:
        # game_on = False
        print("gane over")
        img.save("gameover.png")
        pyautogui.press("space")
        break
    with mss.mss() as sct:
        sct_img = sct.grab({"top": 545, "left": 692, "width": 212, "height": 62})
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        img.convert("L")
    cactus = np.array(img.getdata())
    threat = (cactus != (247, 247, 247)).any()
    if threat:
        time.sleep(0.1999)
        print("jump")
        pyautogui.keyDown("up")
        pyautogui.keyUp("up")
        img.save("jump.png")

