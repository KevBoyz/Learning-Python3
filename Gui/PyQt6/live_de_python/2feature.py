from PySide6.QtWidgets import *
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

#from __feature__ import true_property

app = QApplication()

font = QFont()
font.pixelSize = 500
font.bold()

label = QLabel('Live de Python')
label.font = font
label.alignment = Qt.AlignmentFlag.AlignCenter

label.show()


button = QPushButton('Botão')
button.font = font

#button.show()

app.exec()
