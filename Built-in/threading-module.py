import threading as th
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from random import randint


def th1(max_value):
    for c in range(0, max_value):
        sleep(0.1)
        print(f'T1 Processes left: {max_value - c}')


def main():
    for c in range(0, 10):
        sleep(0.2)
        print(f'T2 Processes left: {10 - c}')


# daemon is a process that runs in the background
# daemon thread will shut down immediately when the program exits

# sub = th.Thread(target=th1, args=(50,), daemon=True)
# sub.start()
# sub.join()  # Wait the tread ends
# main()


def thprocess(name):
    print(f'th {name} initialized')
    sleep(name)
    print(f'th {name} finished')


# Hard-way to handle multiple threads
"""
threads = []
for c in range(3):
    thread = th.Thread(target=thprocess, args=(c+1, c+1))
    threads.append(thread)
    thread.start()

for index, thread in enumerate(threads):  # 1 per 1
    thread.join()
    print(f'th {index+1} is done')
"""
# Using the threadPoolExecutor

# with ThreadPoolExecutor(max_workers=3) as executor:  # Start up a group of threads
#   executor.map(thprocess, (1, 2, 3))

# th.Timer(3, thprocess, args=(4,)).start()  # Schedule a function with threading

# Multiple threads handle





