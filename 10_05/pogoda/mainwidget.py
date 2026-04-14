from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QGridLayout, QMessageBox, QListWidget, QListWidgetItem
import requests
from settingsdialog import SettingsDialog

class MainWidget (QWidget):
    def __init__(self, /):
        super().__init__()

        self.setWindowTitle("Pogoda")

        self.edit = QLineEdit("Lublin")
        searchWithParameter = lambda: self.search(self.edit.text())
        self.edit.returnPressed.connect(searchWithParameter)

        self.button = QPushButton("Okay")
        self.button.clicked.connect(searchWithParameter)

        self.citylist = QListWidget()

        self.weatherLabel = QLabel()
        self.settingsButon = QPushButton("Settings")
        self.settingsButon.clicked.connect(self.execSettings)

        self.layout = QGridLayout(self)
        self.layout.addWidget(QLabel("Miasto"), 0, 0)
        self.layout.addWidget(self.edit, 0, 1)
        self.layout.addWidget(self.button, 1, 0, 1, 2)
        #                                      wiersz, kolumna, rowSpam, colSpan
        self.layout.addWidget(self.citylist, 2, 0, 1, 2)
        self.layout.addWidget(self.weatherLabel, 3, 0, 1, 2)
        self.citylist.itemPressed.connect(self.showWeather)
        self.layout.addWidget(self.settingsButon,4,0,1,2)
    def search(self, city):

        request = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}")
        data = request.json()
        print(data)
        print(request.status_code)
        try:
            if request.status_code != 200:
                raise Exception ("błąd ładowania strony")
            if "results" not in data:
                raise Exception ("nie znaleziono miasta")
            data = data["results"]
        except Exception as error:
            QMessageBox.critical(self, "BŁĄD", str(error))

        citiesData = [(result["name"], result["latitude"], result["longitude"]) for result in data]
        self.pullList(citiesData)


    def pullList(self, citiesData):
        self.citylist.clear()
        for name, latitude, longitude in citiesData:
            item=QListWidgetItem(name)
            item.setData(Qt.UserRole, (latitude, longitude))
            self.citylist.addItem(item)

    def showWeather(self, item):

        data = item.data(Qt.UserRole)
        latitude, longitude = data
        request = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
        data = request.json()
        temp = data["current"]["temperature_2m"]
        self.weatherLabel.setText(f"{temp}")

    def execSettings(self):
        settingsDialog = SettingsDialog(self)
        settingsDialog.exec()




