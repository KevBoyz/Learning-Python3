from kivy.network.urlrequest import UrlRequest
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from os import listdir
import shutil as sh

if 'body4.kv' not in listdir('.'):
    sh.move('assets/body4.kv', '.')


class MyBoxLayout(BoxLayout):
    prop_text = StringProperty()

    def request(self, *args):
        self.prop_text = 'Loading...'

        def on_success(req, result):
            self.prop_text = str(result)

        def on_error(req, response):
            self.prop_text = f'Error: {str(response)}'

        def on_failure(req, response):
            self.prop_text = f'Error2: {str(response)}'

        self.req = UrlRequest(
            'https://pokeapi.co/api/v2/pokemon/blaziken',
            on_success=on_success, on_error=on_error,
            on_failure=on_failure, verify=False
        )


class body4App(App):
    def build(self):
        return MyBoxLayout()


body4App().run()
sh.move('body4.kv', './assets')

