from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from random import sample


def press(btn):
    btn.text = "".join(sample('Hello World', 11))


def release(btn):
    btn.color = "".join(sample('3f9a4b', 6))


class FirstApp(App):
    def build(self):
        button = Button(text='Hello World!', on_press=press, on_release=release)
        button.font_size = 30
        label = Label(text='The dark side of strength')
        label.font_size = 30
        inpt = TextInput()
        box = BoxLayout(orientation='vertical')
        box.add_widget(label)
        box.add_widget(inpt)
        box.add_widget(button)
        return box


FirstApp().run()
