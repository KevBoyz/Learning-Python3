class Gamer:
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def play(self):
        print(f'{self.name} are playing {self.game.name}')


class Game:
    def __init__(self, name):
        self.name = name


gamer = Gamer('Kevin', Game('Borderlands 2'))

gamer.play()
