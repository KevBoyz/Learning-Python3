import psutil as p
from dashing import HSplit, VSplit, VGauge
from time import sleep
from tqdm import tqdm


def byt_to_gb(byts):
    return byts / 1024 / 1024 / 1024


def ram_memory():
    mem = p.virtual_memory()
    total = byt_to_gb(mem.total)
    available = byt_to_gb(mem.available)
    used = byt_to_gb(mem.used)
    return f'{available:.2f}gb free of {total:.2f}gb | Using {used:.2f}gb'


# ram_memory()

"""
ui = HSplit(
    VSplit(
        VGauge(title='RAM'),
        title='Memoria Ram',
        border_color=3,
    )
)
while True:
    sleep(1.5)
    mem_tui = ui.items[0]
    ram_tui = mem_tui.items[0]
    ram_tui.value = p.virtual_memory().percent
    ram_tui.title = f'{p.virtual_memory().percent}%'
    ui.display()
"""

# print(p.cpu_freq())
# print(p.cpu_percent())
# print(p.cpu_stats())

"""print(p.cpu_count())  # Threads
print(p.cpu_count(logical=False))  # nucleus
print(p.cpu_freq(percpu=True))"""

cpu_bar = tqdm(total=100, colour='green')
cpu_bar.set_description('cpu-usage')

# ram_bar = tqdm(total=byt_to_gb(p.virtual_memory().total), colour='yellow')
# ram_bar.set_description('ram-usage')

print(p.cpu_times())

while True:
    cpu_bar.n = (p.cpu_percent(interval=1))
    cpu_bar.refresh()

    # ram_bar.n = (byt_to_gb(p.virtual_memory().used))
    # ram_bar.refresh()
