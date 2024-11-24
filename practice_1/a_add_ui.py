from PySide6 import QtWidgets

from ui.b_login import Ui_Form

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

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # self.ui.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    w = Window()
    w.show()

    app.exec()