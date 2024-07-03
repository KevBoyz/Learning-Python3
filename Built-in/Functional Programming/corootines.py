from queue import Queue


class Scheduler:  # Super primitivo
    def __init__(self) -> None:
        self.queue = Queue()

    def add_coro(self, coro):
        self.queue.put(iter(coro))

    def run(self):
        while not self.queue.empty():
            task = self.queue.get()
            try:
                val = next(task)
                print(f'{val=}:')
                self.queue.put(task)
            except StopIteration:
                print(f'Stop Iteration at {task}')


s = Scheduler()
s.add_coro(range(0, 10))
s.add_coro(range(11, 15))
#s.run()

# 02


def coro():
    while True:
        val = yield
        print(val)


"""c = coro()
next(c)  # init
c.send('Ahh Zé da manga')
c.close()
"""

def runtime_mean():
    mean = None
    n = 0
    total = 0
    while True:
        inp = yield mean
        n += 1
        total += inp
        mean = total / n


m = runtime_mean()
next(m)
print(m.send(10))
print(m.send(15))


