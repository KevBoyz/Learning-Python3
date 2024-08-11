from kivy.app import App
from kivy.lang import Builder


class Main(App):
    def build(self):
        return Builder.load_file('body9.kv')

    def pic_taken(self):
        print('Got pic')

    def change_cam(self, instance):
        cam = instance.parent.ids.xcamera
        if cam.index == 0:
            cam.index = int(cam.index) + 1
        elif cam.index == 1:
            cam.index = int(cam.index) - 1
        else:
            cam.index = cam.index



Main().run()
