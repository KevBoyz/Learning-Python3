from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout


class MyRoot(BoxLayout):
    ...


class Body8App(App):
    @staticmethod
    def alarm(*args):
        sound = SoundLoader.load('al1.mp3')
        sound.play()

    def build(self):
        return MyRoot()






Body8App().run()


