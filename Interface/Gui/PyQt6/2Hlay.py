import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

app = QApplication([])

window = QWidget()
window.setWindowTitle('PyQT App')

layout = QHBoxLayout()
layout.addWidget(QPushButton('Left'))
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Rigth'))

window.setLayout(layout)
window.show()
sys.exit(app.exec())
