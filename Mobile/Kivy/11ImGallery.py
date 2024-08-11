from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
import os

kv = """
ScrollView:
    image_grid: image_grid
    do_scroll_x: False
    do_scroll_y: True
    GridLayout:
        id: image_grid
        cols: 3
        rows: 3
"""


class ImageGridApp(App):
    def build(self):
        return Builder.load_string(kv)

    def on_start(self):
        # I'm loading the same image for this example...
        grid = self.root.image_grid  # the gridlayout is the root widget.
        imlist = []
        for file in os.listdir('.'):
            if file.endswith('jpg') or file.endswith('png') or file.endswith('jpeg'):
                imlist.append(file)
        for i in range(grid.rows * grid.cols):
            try:
                grid.add_widget(Image(source=imlist[i]))
            except:
                pass


ImageGridApp().run()
