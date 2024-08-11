from PyQt6.QtWidgets import *
from PyQt6.QtWebChannel import QWebChannel


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')

        self.layout = QFormLayout()

        self.loginField = QLineEdit()
        self.loginField.setPlaceholderText('Loginnn')
        self.passwordField = QLineEdit()
        self.passwordField.setPlaceholderText('Passwwordd')
        self.passwordField.setEchoMode(QLineEdit.EchoMode.Password)

        # This strings are used to instaciate QLabel's
        self.layout.addRow('<h4>Login</h4>', self.loginField)
        self.layout.addRow('<h4>Password</h4>', self.passwordField)

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
