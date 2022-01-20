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
        self.cap = cv2.VideoCapture(0)
        layout.add_widget(MDRaisedButton(
            text='Click me',
            pos_hint={'center_x': .5, 'center_y': .5},
            size_hint=(None, None))
        )
        Clock.schedule_interval(self.load_video, 1.0/38.0)
        return layout

    def load_video(self, *args):
        ret, frame = self.cap.read()
        ret, frame1 = self.cap.read()
        ret, frame2 = self.cap.read()
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour) < 900:
                continue
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        buffer = cv2.flip(frame1, 0).tostring()
        texture = Texture.create(size=(frame1.shape[1], frame1.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture


MainApp().run()
