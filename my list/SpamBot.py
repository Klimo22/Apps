import pyautogui as auto
import time

time.sleep(4)
for i in range(5):
    time.sleep(0.5)
    auto.write('ThisIsSpam')
    auto.press('enter')
