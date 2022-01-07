from kivymd.app import MDApp
from kivymd.uix.floatlayout import FloatLayout
from os import listdir
import shutil as sh

if 'body6.kv' not in listdir('.'):
    sh.move('assets/body6.kv', '.')


class MyScreen(FloatLayout):
    ...


class Body6App(MDApp):
    def build(self):
        return MyScreen()


Body6App().run()
sh.move('body6.kv', './assets')
