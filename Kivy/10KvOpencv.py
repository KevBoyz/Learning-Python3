from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2


class MainApp(MDApp):
    def build(self):
        layout = MDBoxLayout(orientation='vertical')
        self.image = Image()
        layout.add_widget(self.image)
        self.capture = cv2.VideoCapture(0)
        layout.add_widget(MDRaisedButton(
            text='Click me',
            pos_hint={'center_x': .5, 'center_y': .5},
            size_hint=(None, None))
        )
        Clock.schedule_interval(self.load_video, 1.0/38.0)
        return layout

    def load_video(self, *args):
        ret, frame = self.capture.read()
        buffer = cv2.flip(frame, 0).tostring()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture


MainApp().run()
