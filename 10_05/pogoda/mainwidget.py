from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QGridLayout


class MainWidget (QWidget):
    def __init__(self, /):
        super().__init__()

        self.setWindowTitle("Pogoda")

        self.label = QLabel("Miasto")

        self.edit = QLineEdit()
        self.edit.returnPressed.connect(self.copyText)

        self.button = QPushButton("Okay")
        self.button.clicked.connect(self.copyText)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.edit, 0, 1)
        self.layout.addWidget(self.button, 1, 0, 1, 2)

    def copyText(self):
        text = self.edit.text()
        self.label.setText(text)
