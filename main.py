from PySide6 import QtWidgets


# app = QtWidgets.QApplication()
#
# window = QtWidgets.QWidget()
# window.setWindowTitle("Простейшее окно")
# window.show()
#
# app.exec()

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    w = Window()
    w.show()

    app.exec()
