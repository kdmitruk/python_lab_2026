from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QWidget, QApplication
from mainwidget import *

def main():
    app = QApplication()
    QCoreApplication.setOrganizationName("Pogodynka")
    QCoreApplication.setApplicationName("Pogoda")
    widget = MainWidget()
    widget.show()

    app.exec()

if __name__ == '__main__':
    main()