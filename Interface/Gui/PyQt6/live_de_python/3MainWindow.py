from PySide6.QtWidgets import *
from PySide6.QtGui import QFont, QAction
from PySide6.QtCore import Qt


font = QFont()
font.setPixelSize(30)
font.bold()

app = QApplication()

window = QMainWindow()

menu = window.menuBar()
file_menu = menu.addMenu('Arquivo')
action = QAction('Ação')
file_menu.addAction(action)

content = QWidget()

layout = QVBoxLayout()

label = QLabel('Live de Python')
label.setFont(font)
label.setAlignment(Qt.AlignmentFlag.AlignCenter)

button = QPushButton('Botão')
button.setFont(font)

layout.addWidget(label)
layout.addWidget(button)

content.setLayout(layout)
window.setCentralWidget(content)

window.show()

app.exec()
