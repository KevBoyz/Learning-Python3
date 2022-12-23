import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

app = QApplication([])

layout = QGridLayout()
layout.addWidget(QPushButton("Button"), 0, 0)
layout.addWidget(QPushButton("Button"), 0, 1)
layout.addWidget(QPushButton("Button"), 0, 2)
layout.addWidget(QPushButton("Button"), 1, 0, 1, 3)
layout.addWidget(QPushButton("Button"), 2, 0, 1, 1)
layout.addWidget(QPushButton("Button"), 2, 1, 1, 2)


window = QWidget()
window.setWindowTitle('PyQT App')
window.setLayout(layout)

window.show()
sys.exit(app.exec())

