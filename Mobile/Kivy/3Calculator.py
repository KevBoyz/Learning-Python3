from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import shutil as sh

sh.move('assets/body3.kv', '.')


class MyBoxLayout(BoxLayout):
    prop0 = StringProperty('0')  # Html class looks like

    def change(self, *args):
        if self.prop0 != '0o0':
            self.prop0 = '0o0'
        else:
            self.prop0 = '0'


class Body3App(App):
    def build(self):
        return MyBoxLayout()


Body3App().run()
sh.move('body3.kv', './assets')
