import pyautogui

import time

pyautogui.hotkey('alt','tab')
time.sleep(0.3)
pyautogui.hotkey('alt','f4')
pyautogui.press('alt')
pyautogui.press('right')
pyautogui.press('enter')
pyautogui.press('down',5)
pyautogui.press('enter')