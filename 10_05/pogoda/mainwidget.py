from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QGridLayout


class MainWidget (QWidget):
    def __init__(self, /):
        super().__init__()

        self.setWindowTitle("Pogoda")

        self.edit = QLineEdit()
        self.button = QPushButton("Okay")

        self.layout = QGridLayout(self)
        self.layout.addWidget(QLabel("Miasto"), 0, 0)
        self.layout.addWidget(self.edit, 0, 1)
        self.layout.addWidget(self.button, 1, 0, 1, 2)

