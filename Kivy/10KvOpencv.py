from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
import cv2


class MainApp(MDApp):
    def build(self):
        layout = MDBoxLayout(orientation='vertical')
        self.image = Image()
        layout.add_widget(MDRaisedButton(
            text='Click me',
            pos_hint={'center_x': .5, 'center_y': .5},
            size_hint=(None, None))
        )
        return layout


MainApp().run()
