from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox, QListWidget, \
    QListWidgetItem
import requests
from settingsdialog import SettingsDialog

class MainWidget(QWidget):
    avaiableVariables = ["temperature_2m","weather_code","pressure_msl"]
    def __init__(self, /):
        super().__init__()
        self.setWindowTitle("Pogoda")
        edit = QLineEdit("Lublin")
        searchWithArgument = lambda: self.search (edit.text())
        edit.returnPressed.connect(searchWithArgument)
        button = QPushButton("OK")
        button.clicked.connect(searchWithArgument)
        self.cityList = QListWidget()
        self.cityList.itemClicked.connect(self.load)
        self.weatherText = QLabel()
        settingsButton = QPushButton("Settings")
        settingsButton.clicked.connect(self.execSettings)
        layout = QGridLayout(self)
        layout.addWidget(QLabel("Miasto"), 0, 0)
        layout.addWidget(edit, 0, 1)
        layout.addWidget(button, 1, 0, 1, 2)
        layout.addWidget(self.cityList, 2, 0, 1, 2)
        layout.addWidget(self.weatherText, 3, 0, 1, 2)
        layout.addWidget(settingsButton, 4, 0, 1, 2)

    def search(self, city):
        r = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={city}')
        try:
            if r.status_code != 200:
                raise Exception("Błąd odpowiedzi")
            results = r.json()
            if "results" not in results:
                raise Exception(f"Nie znaleziono miasta {city}.")
            results = results["results"]
            cities = [(result["name"], result["latitude"], result["longitude"]) for result in results]
            self.pullList(cities)
        except Exception as error:
            print(f"{error}")
            QMessageBox.information(
                self,
                "Błąd",
                f"{error}"
            )

    def pullList(self, cities):
        self.cityList.clear()
        for name, latitude, longitude in cities:
             item = QListWidgetItem(name)
             item.setData(Qt.UserRole,(latitude,longitude))
             self.cityList.addItem(item)

    def load(self, item):
        latitude, longitude = item.data(Qt.UserRole)
        r = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m')
        results = r.json()
        temperature = results["current"]["temperature_2m"]
        self.weatherText.setText(f"{temperature}")

    def execSettings(self):
        dialog = SettingsDialog(self)
        dialog.exec()
        print (dialog.result())