from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout


class MainWidget(QWidget):
    def __init__(self, /):
        super().__init__()
        self.setWindowTitle("Pogoda")
        self.label = QLabel("Miasto")
        self.edit = QLineEdit()
        self.button = QPushButton("OK")
        layout = QGridLayout(self)
        layout.addWidget(self.label, 0, 0)
        layout.addWidget(self.edit, 0, 1)
        layout.addWidget(self.button, 1, 0, 1, 2)