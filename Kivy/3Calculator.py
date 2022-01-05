from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import shutil as sh

sh.move('./assets/btns.kv', '.')


class MyBoxLayout(BoxLayout):
    prop0 = StringProperty('0')  # Html class looks like

    def change(self, *args):
        if self.prop0 != '0o0':
            self.prop0 = '0o0'
        else:
            self.prop0 = '0'



class btnsApp(App):
    def build(self):
        return MyBoxLayout()


btnsApp().run()
sh.move('btns.kv', './assets')
