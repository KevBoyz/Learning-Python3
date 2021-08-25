import pygame
from pygame import display
from pygame.image import load
from pygame.transform import scale
from pygame.sprite import Sprite, GroupSingle, Group
from pygame import event
from pygame.locals import QUIT, KEYDOWN, K_SPACE, K_a, K_d
from pygame.time import Clock

pygame.init()


class SpaceShip(Sprite):
    def __init__(self, bullet):
        super().__init__()
        self.image = load('Sprites/spaceship.png')  # Sprite
        self.rect = self.image.get_rect(center=(540, 550))  # Hit box
        self.speed = 3
        self.bullet = bullet

    def shot(self):
        self.bullet.add(Bullet(self.rect.x + 105, self.rect.y))
        self.bullet.add(Bullet(self.rect.x + 45, self.rect.y + 90))
        self.bullet.add(Bullet(self.rect.x + 160, self.rect.y + 90))
        self.bullet.update()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            if not self.rect.x <= 0:
                self.rect.x -= self.speed
        elif keys[K_d]:
            if not self.rect.x >= 1080:
                self.rect.x += self.speed


class Bullet(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = load('Sprites/bullet.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 4

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()


class OVNI(Sprite):
    def __init__(self):
        super().__init__()
        self.image = load('Sprites/ovni.png')
        self.rect = self.image.get_rect(center=(540, 50))
        self.direction = 0

    def update(self):
        if self.direction == 0:
            self.rect.x -= 2
            if self.rect.x <= 0:
                self.direction = 1
        else:
            self.rect.x += 2
            if self.rect.x >= 850:
                self.direction = 0

bullet = Group()

spship = SpaceShip(bullet)
nave = GroupSingle(spship)

ovni = OVNI()
ufo = GroupSingle(ovni)

size = (1080, 700)
window = display.set_mode(
    display=0,  # display = monitor
    size=size,
    depth=0,
    vsync=0,
    flags=0
)

display.set_caption('Nego Dí Rapariga NÃO - Brega version')
bg = scale(load('images/space-bg.jpg'), size)

clock = Clock()
while True:
    clock.tick(300)  # Frames per second
    for ev in event.get():  # Close event
        if ev.type == QUIT:
            pygame.quit()
        if ev.type == KEYDOWN:
            if ev.key == K_SPACE:
                spship.shot()

    window.blit(bg, (0, 0))  # (200, 50) Position, 4 cartesian quadrant
    nave.draw(window)
    ufo.draw(window)
    bullet.draw(window)
    nave.update()
    bullet.update()
    ufo.update()
    display.update()
