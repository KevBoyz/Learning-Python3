import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])

window = QWidget()
window.setWindowTitle('Hello')
window.setGeometry(500, 300, 280, 80)

msg = QLabel("<h1>Hello World!</h1>", parent=window)
msg.move(60, 15)

window.show()
sys.exit(app.exec())
