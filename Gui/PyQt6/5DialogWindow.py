from sys import exit
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QFormLayout, QLineEdit, QDialog, QDialogButtonBox


class Window(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QDialog")
        dialogLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow("UserName", QLineEdit())
        formLayout.addRow("Password", QLineEdit())
        dialogLayout.addLayout(formLayout)
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )
        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)


app = QApplication([])
window = Window()
window.show()

exit(app.exec())
