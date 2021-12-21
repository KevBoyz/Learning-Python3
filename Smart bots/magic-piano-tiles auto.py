import pyautogui as pg
from keyboard import is_pressed
import win32api as w32
import win32con as w32con
from time import sleep


def click(x, y=400):
    w32.SetCursorPos((x, y))
    w32.mouse_event(w32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.01)
    w32.mouse_event(w32con.MOUSEEVENTF_LEFTUP, 0, 0)


def run():
    while True:
        if is_pressed('w'):
            while True:
                if is_pressed('e'):
                    break
                else:
                    if pg.pixel(543, 400)[0] == 0:
                        click(543)
                    if pg.pixel(630, 400)[0] == 0:
                        click(630)
                    if pg.pixel(726, 400)[0] == 0:
                        click(726)
                    if pg.pixel(811, 400)[0] == 0:
                        click(811)
        else:
            continue


run()
