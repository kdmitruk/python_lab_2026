from PySide6.QtWidgets import QDialog, QCheckBox, QVBoxLayout, QDialogButtonBox


class SettingsDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("settings")
        tempBox1 = QCheckBox("temperature_2m")
        tempBox2 = QCheckBox("weather_code")
        tempBox3 = QCheckBox("pressure_msl")
        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addWidget(tempBox1)
        layout.addWidget(tempBox2)
        layout.addWidget(tempBox3)
        layout.addWidget(buttonBox)
