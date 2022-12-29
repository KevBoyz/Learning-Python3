from PySide6.QtWidgets import *
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

app = QApplication()

font = QFont()
font.setPixelSize(30)
font.bold()

label = QLabel('Live de Python')
label.setFont(font)
label.setAlignment(Qt.AlignmentFlag.AlignCenter)

label.show()


button = QPushButton('Botão')
button.setFont(font)

button.show()

app.exec()
