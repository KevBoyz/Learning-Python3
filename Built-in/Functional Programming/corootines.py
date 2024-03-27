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


def coro():
    print('Mim de')
    val = yield
    print(val)


c = coro()
next(c)
c.send('Ahh Zé da manga')

