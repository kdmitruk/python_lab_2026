from PySide6.QtWidgets import QWidget, QApplication
from mainwidget import *

def main():
    app = QApplication()
    widget = MainWidget()
    widget.show()

    app.exec()

if __name__ == '__main__':
    main()