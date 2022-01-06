from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from plyer import vibrator, battery, notification
from os import listdir
import shutil as sh

if 'body5.kv' not in listdir('.'):
    sh.move('assets/body5.kv', '.')


class MyBoxLayout(BoxLayout):
    propriedade = StringProperty()

    def notificar(self, *args):
        notification.notify('Titulo', 'Notificação')

    def bateria(self, *args):
        self.propriedade = str(battery.status['percentage']) + '%'

    def vibrar(self, *args):
        vibrator.vibrate(2)


class Body5App(App):
    def build(self):
        return MyBoxLayout()


Body5App().run()
sh.move('body5.kv', './assets')
