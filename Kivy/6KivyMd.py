from kivymd.app import MDApp
from kivymd.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from os import listdir
import shutil as sh

if 'body6.kv' not in listdir('.'):
    sh.move('assets/body6.kv', '.')


class MyScreen(FloatLayout):
    ...


class FormLogin(FloatLayout):
    dialog = None
    def open_card(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Password Retriever",
                type="custom",
                content_cls=Content(),

            )
        self.dialog.open()




class Content(BoxLayout):
    pass


class Body6App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.accent_palette = 'Purple'
        self.theme_cls.theme_style = 'Dark'
        return MyScreen()


Body6App().run()
sh.move('body6.kv', './assets')
