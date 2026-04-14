from PySide6.QtWidgets import QDialog, QCheckBox, QVBoxLayout, QDialogButtonBox


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
        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        layout.addWidget(buttonBox)

    def weatherVariables(self):
        result = {}
        for key, box in self.boxes.items():
            result[key] = box.isChecked()
        return result