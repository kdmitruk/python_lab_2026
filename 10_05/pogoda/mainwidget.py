from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QGridLayout
import requests


class MainWidget (QWidget):
    def __init__(self, /):
        super().__init__()

        self.setWindowTitle("Pogoda")

        self.edit = QLineEdit("Lublin")
        searchWithParameter = lambda: self.search(self.edit.text())
        self.edit.returnPressed.connect(searchWithParameter)

        self.button = QPushButton("Okay")
        self.button.clicked.connect(searchWithParameter)

        self.layout = QGridLayout(self)
        self.layout.addWidget(QLabel("Miasto"), 0, 0)
        self.layout.addWidget(self.edit, 0, 1)
        self.layout.addWidget(self.button, 1, 0, 1, 2)


    def search(self, city):
        request = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}")
        data = request.json()
        print(data)
        print(request.status_code)
        if request.status_code != 200:
            return
        print(data["results"])
        for result in data["results"]:
            output = f"{result["name"]}, {result["latitude"]}, {result["longitude"]}"
            print(output)

