from PySide6.QtWidgets import *
from PySide6.QtGui import QFont, QAction
from PySide6.QtCore import Qt
from qdarktheme import load_stylesheet


font = QFont()
font.setPixelSize(30)
font.bold()

font2 = QFont()
font2.setPixelSize(60)
font2.bold()

app = QApplication()
app.setStyleSheet(load_stylesheet())


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        menu = self.menuBar()
        file_menu = menu.addMenu("&Arquivo")

        new_action = QAction('&Novo', self)
        new_action.triggered.connect(lambda: print('Action1 triggered'))
        file_menu.addAction(new_action)

        open_action = QAction('&Abrir', self)
        open_action.triggered.connect(lambda: print('Action2 triggered'))        
        file_menu.addAction(open_action)

        content = QWidget()
        layout = QVBoxLayout()

        self.label = QLabel('Live de Python')
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button = QPushButton('PySide6 com Dunossauro')
        button.setFont(font)

        button.clicked.connect(self.click)

        layout.addWidget(self.label)
        layout.addWidget(button)

        content.setLayout(layout)
        self.setCentralWidget(content)

    def click(self):
        if self.label.text() == 'Live de Python':
            self.label.setText('#209')
        else:
            self.label.setText('Live de Python')


w = Window()
w.show()
app.exec()
