from threading import Thread
from time import sleep


def th1():
    for c in range(0, 5):
        sleep(1)
        print('Task n1')


def mainth():
    for c in range(0, 5):
        sleep(1)
        print('Task n2')


Thread(target=th1).start()
mainth()
print('Task2 has finished')

