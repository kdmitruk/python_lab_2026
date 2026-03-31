from PySide6.QtWidgets import QWidget, QApplication


def main():
    app = QApplication()
    widget = QWidget()
    widget.show()

    app.exec()

if __name__ == '__main__':
    main()