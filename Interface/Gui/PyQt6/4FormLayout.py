from sys import exit
from PyQt6.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit

app = QApplication([])
window = QWidget()
window.setWindowTitle('PyQT App')

layout = QFormLayout()
layout.addRow("UserName", QLineEdit())
layout.addRow("Password", QLineEdit())

window.setLayout(layout)
window.show()

exit(app.exec())
