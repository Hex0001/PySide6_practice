"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""


import time
from PySide6 import QtWidgets, QtCore
from ui.c_signals_events_form import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.spinBoxX.setMaximum(self.screen().geometry().width() - 100)  # Значение 100,
        # чтобы окно не уходило за экран
        self.ui.spinBoxY.setMaximum(self.screen().geometry().height() - 100)

        self.initSignals()


    def initSignals(self):
        # Перемещение окна
        self.ui.pushButtonLT.clicked.connect(self.onPushButtonLTClicked)
        self.ui.pushButtonRT.clicked.connect(self.onPushButtonRTClicked)
        self.ui.pushButtonCenter.clicked.connect(self.onPushButtonCenter)
        self.ui.pushButtonLB.clicked.connect(self.onPushButtonLB)
        self.ui.pushButtonRB.clicked.connect(self.onPushButtonRB)
        self.ui.pushButtonMoveCoords.clicked.connect(self.onPushButtonMoveCoords)

        # Получение информации
        self.ui.pushButtonGetData.clicked.connect(self.onPushButtonGetData)

    def onPushButtonLTClicked(self):
        self.move(0, 0)

    def onPushButtonRTClicked(self):
        self.move(self.screen().geometry().width() - self.width(), 0)

    def onPushButtonCenter(self):
        self.move((self.screen().geometry().width() - self.width())/2,
                  (self.screen().geometry().height() - self.height())/2)

    def onPushButtonLB(self):
        self.move(0, self.screen().geometry().height() - self.height())

    def onPushButtonRB(self):
        self.move(self.screen().geometry().width() - self.width(),
                  self.screen().geometry().height() - self.height())

    def onPushButtonMoveCoords(self):
        self.move(int(self.ui.spinBoxX.text()), int(self.ui.spinBoxY.text()))
        self.ui.spinBoxX.setValue(0)
        self.ui.spinBoxY.setValue(0)

    def onPushButtonGetData(self):
        self.ui.plainTextEdit.setPlainText(f"Время: {time.ctime()}\n"
                                           f"Количество экранов: {str(len(QtWidgets.QApplication.screens()))}\n"
                                           f"Основное окно: {QtWidgets.QApplication.activeWindow().windowTitle()}\n"
                                           f"Разрешение экрана: {self.screen().geometry().width()}x{self.screen().geometry().height()}\n"
                                           f"Монитор: {self.screen().name()}\n"
                                           f"Размеры окна: {self.width()}x{self.height()}\n"
                                           f"Минимальные размеры окна: {self.minimumWidth()}x{self.minimumHeight()}\n"
                                           f"Текущее положение (координаты) окна: {self.x()}x{self.y()}\n"
                                           f"Координаты центра приложения: {int((self.x() + self.width())/2)}x{int((self.y() + self.height())/2)}\n"
                                           f" Отслеживание состояния окна: {self.window().windowState()}")

    def moveEvent(self, event):
        print(f"-----Время перемещения окна: {time.ctime()}-----\n"
              f"Старая позиция: {event.oldPos().x()}x{event.oldPos().y()}\n"
              f"Новая позиция: {event.pos().x()}x{event.pos().y()}")

    def resizeEvent(self, event):
        print(f"-----Время изменения размера окна: {time.ctime()}-----\n"
              f"Новый размер окна: {event.size().width()}x{event.size().height()}")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
