from PySide6.QtWidgets import QDialog, QCheckBox, QVBoxLayout, QDialogButtonBox, QComboBox


class SettingsDialog(QDialog):
    def __init__(self, parent,weatherVariables):
        super().__init__(parent)
        self.boxes = {}
        layout = QVBoxLayout(self)
        for key, checked in weatherVariables.items():
            box = QCheckBox (key)
            box.setChecked(checked)
            layout.addWidget(box)
            self.boxes[key] = box
        self.setWindowTitle("settings")
        self.temperatureUnitBox = QComboBox()
        self.temperatureUnitBox.addItem("C")
        self.temperatureUnitBox.addItem("F")
        layout.addWidget(self.temperatureUnitBox)
        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        layout.addWidget(buttonBox)
        self.boxes["temperature_2m"].toggled.connect(self.updateTemperatureUnitBoxVisibility)
        self.updateTemperatureUnitBoxVisibility()

    def weatherVariables(self):
        result = {}
        for key, box in self.boxes.items():
            result[key] = box.isChecked()
        return result

    def updateTemperatureUnitBoxVisibility(self):
        self.temperatureUnitBox.setVisible(self.boxes["temperature_2m"].isChecked())