from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox
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
        layout.addWidget(edit, 0, 1)
        layout.addWidget(button, 1, 0, 1, 2)

    def search(self, city):
        r = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={city}')
        try:
            if r.status_code != 200:
                raise Exception("Błąd odpowiedzi")
            results = r.json()
            if "results" not in results:
                raise Exception(f"Nie znaleziono miasta {city}.")
            results = results["results"]
            for result in results:
                print(f"{result["name"]}: {result["latitude"]}, {result["longitude"]}")
        except Exception as error:
            print(f"{error}")
            QMessageBox.information(
                self,
                "Błąd",
                f"{error}"
            )
