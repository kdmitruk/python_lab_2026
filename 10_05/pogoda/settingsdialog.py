from PySide6.QtWidgets import QDialog, QCheckBox, QGridLayout, QDialogButtonBox


class SettingsDialog(QDialog):
    def __init__(self, weatherVariables, parent):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        codeBox = QCheckBox("Weather code")
        temperatureBox = QCheckBox("Temperature box")
        pressureBox = QCheckBox("Pressure box")

        self.boxes = {
            "weather_code": codeBox,
            "temperature_2m": temperatureBox,
            "pressure_msl": pressureBox
        }

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        self.layout = QGridLayout(self)
        self.layout.addWidget(codeBox)
        self.layout.addWidget(temperatureBox)
        self.layout.addWidget(pressureBox)
        self.layout.addWidget(buttonBox)

        self.restoreVariables(weatherVariables)

    def weatherVariables(self):
        weatherVariables = set()
        for key, checkbox in self.boxes.items():
            if checkbox.isChecked():
                weatherVariables.add(key)
        return weatherVariables

    def restoreVariables(self, variables):
        for key, checkbox in self.boxes.items():
            checkbox.setChecked(key in variables)
