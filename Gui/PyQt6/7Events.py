import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel


def greet():
    if msg.text():
        msg.setText("")
    else:
        msg.setText("Greet")


app = QApplication([])

window = QWidget()
window.setWindowTitle('PyQT App')

layout = QVBoxLayout()
button = QPushButton("Greet", clicked=greet)
layout.addWidget(button)
msg = QLabel()
layout.addWidget(msg)

window.setLayout(layout)
window.show()
sys.exit(app.exec())
