from PySide6.QtCore import QCoreApplication, QSettings
from PySide6.QtWidgets import QWidget, QApplication
from mainwidget import MainWidget

def main():
    app = QApplication()
    QCoreApplication.setOrganizationName("UMCS")
    QCoreApplication.setApplicationName("Pogoda")


    widget = MainWidget()

    widget.show()

    return app.exec()


if __name__ == '__main__':
    main()