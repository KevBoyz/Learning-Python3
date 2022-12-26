from PyQt6.QtWidgets import *


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')

        self.layout = QFormLayout()

        self.loginField = QLineEdit()
        self.loginField.setPlaceholderText('Loginnn')
        self.passwordField = QLineEdit()
        self.passwordField.setPlaceholderText('Passwwordd')

        self.layout.addRow('Login', self.loginField)
        self.layout.addRow('Password', self.passwordField)

        self.send_button = QPushButton("Login")
        self.send_button.clicked.connect(self.check_login)
        self.layout.addWidget(self.send_button)

        self.setLayout(self.layout)

    def check_login(self):
        if self.loginField.text() == "Kevin" and self.passwordField.text() == '123':
            print('Your are logged')
        else:
            print('Please try again')


app = QApplication([])
form = LoginForm()
form.show()

app.exec()
