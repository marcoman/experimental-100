# This app drives the popular no-internet TREX game by Google.
# I suspect what i need to do is open the browser indepenedent of this application, and then run it.  I don't think I'm driving the web application from this app.

import pyautogui
# import pyautogui._pyautogui_x11 as platformModule
import pyautogui._pyautogui_win as platformModule
import mss
import os

    
from time import sleep
# os.environ['DISPLAY'] = ':0'
# with mss.mss() as sct:
#     sct.shot()



TREX_GAME = "https://elgoog.im/t-rex/"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language': 'en-US,en;q=0.5',
           'Accept-Encoding': 'gzip, deflate',
           'Connection': 'keep-alive',
           'Upgrade-Insecure-Requests': '1',
           'Cache-Control': 'max-age=0'
           }

TEST_URL = TREX_GAME

screenWidth, screenHeight = pyautogui.size()
print(f'Your screen height and width are {screenHeight} and {screenWidth}')

# for i in range(0, 50):
#     print(f'Loop {i}')
#     currentMouseX, currentMouseY = pyautogui.position()
#     print(f'X: {currentMouseX} Y: {currentMouseY}')
#     if (currentMouseX < 300 and currentMouseY < 300):
#         print("Clicking")
#         pyautogui.press('space')
#     else:
#         print("Not clicking")

#     sleep(0.25 )

XPOS = 600
CONFIDENCE = 1
REGION = (300, 1245, 200, 15)
PIXEL_LEFT = 1000

while (True):
    # currentMouseX, currentMouseY = pyautogui.position()
    # print(pyautogui.pixel(currentMouseX, currentMouseY))
    if pyautogui.pixelMatchesColor(PIXEL_LEFT,1185, (83,83,83), tolerance=8):
        # print('obstacle!')
        pyautogui.press('space')
    elif pyautogui.pixelMatchesColor(PIXEL_LEFT,1500, (83,83,83), tolerance=8):
        # print(pyautogui.position())
        # print('obstacle!')
        pyautogui.press('down')
      
