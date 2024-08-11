from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import shutil as sh

sh.move('./assets/body2.kv', '.')


class MyBoxLayout(BoxLayout):
    ...


class body2App(App):
    def build(self):
        return MyBoxLayout()


body2App().run()
sh.move('body2.kv', './assets')
