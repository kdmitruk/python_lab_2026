from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout
import requests


class MainWidget(QWidget):
    def __init__(self, /):
        super().__init__()
        self.setWindowTitle("Pogoda")
        edit = QLineEdit("Lublin")
        searchWithArgument = lambda: self.search (edit.text())
        edit.returnPressed.connect(searchWithArgument)
        button = QPushButton("OK")
        button.clicked.connect(searchWithArgument)
        layout = QGridLayout(self)
        layout.addWidget(QLabel("Miasto"), 0, 0)
        layout.addWidget(self.edit, 0, 1)
        layout.addWidget(button, 1, 0, 1, 2)



    def search(self, city):
        r = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={city}')
        print(r.json())
