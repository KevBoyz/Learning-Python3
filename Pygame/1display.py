from pygame import display
from pygame.image import load
from pygame.transform import scale


size = (1080, 700)
window = display.set_mode(
    display=0,  # display = monitor
    size=size,
    depth=0,
    vsync=0,
    flags=0
)

display.set_caption('Nego Dí Rapariga NÃO - Brega version')
bg = scale(load('images/david.jpg'), size)

window.blit(
    bg,
    (0, 0)  # (200, 50) Position, 4 cartesian quadrant
)
display.update()

while True:
    ...
