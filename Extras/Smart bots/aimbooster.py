import pyautogui as pg
from keyboard import is_pressed
import win32api as w32
import win32con as w32con
from time import sleep


def locate_test():  # Try to locate an image on screen
    while True:     # This func do nothing with the automations, is just a test
        if not pg.locateOnScreen('<img-path>', confidence=0.9):
            print('I can\'t see it')
        else:
            print('I see the image')
        sleep(0.5)


def click(x, y=400):
    w32.SetCursorPos((x, y))
    w32.mouse_event(w32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.01)
    w32.mouse_event(w32con.MOUSEEVENTF_LEFTUP, 0, 0)


def shot():
    return pg.screenshot(region=(375, 297, 600, 420))


def run():
    width, height = 600, 420
    while not is_pressed('e'):
        im = shot()
        for x in range(0, width, 5):
            for y in range(0, height, 5):
                r, g, b = im.getpixel((x, y))
                if b == 195:
                    click(x+375, y+297)
                    sleep(0.05)
                    im = shot()
                    break


while True:
    if is_pressed('w'):
        run()
