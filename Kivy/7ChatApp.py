from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import socket
from threading import Thread

client = server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def make_invisible(widget):
    widget.visible = False
    widget.size_hint_x = None
    widget.size_hint_y = None
    widget.height = 0
    widget.width = 0
    widget.text = ""
    widget.opacity = 0


class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()

    def send_message(self):
        client.send(f'{self.nickname_text.text}: {self.message_text.text}'.encode('utf-8'))
        self.message_text.text = ''

    def connect_to_server(self):
        if self.nickname_text != "":
            client.connect((self.ip_text.text, 7562))
            msg = client.recv(1024).decode('utf-8')
            if msg == "NICK":
                client.send(self.nickname_text.text.encode('utf-8'))
                self.send_btn.disabled = False
                self.message_text.disabled = False
                self.connect_btn.disabled = True
                self.ip_text.disabled = True
                make_invisible(self.connection_grid)
                make_invisible(self.connect_btn)
                thread = Thread(target=self.receive)
                thread.start()

    def receive(self):
        stop = False
        while not stop:
            try:
                msg = client.recv(1024).decode('utf-8')
                self.chat_text.text += msg + '\n'
            except Exception as e:
                print(f'!ERROR: {e}')
                client.close()
                stop = True


class Body7App(App):
    def build(self):
        return MyRoot()


Body7App().run()