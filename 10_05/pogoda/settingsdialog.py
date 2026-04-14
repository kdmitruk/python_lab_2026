from PySide6.QtWidgets import QDialog, QCheckBox, QGridLayout, QDialogButtonBox


class SettingsDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.codeBox = QCheckBox("Weather code")
        self.temperatureBox = QCheckBox("Temperature box")
        self.pressureBox = QCheckBox("Pressure box")
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.codeBox)
        self.layout.addWidget(self.temperatureBox)
        self.layout.addWidget(self.pressureBox)
        self.layout.addWidget(buttonBox)




