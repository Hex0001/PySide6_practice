"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
from PySide6 import QtWidgets, QtGui
from ui.system_info import Ui_Form
from a_threads import SystemInfo


class SystemInfoWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.lineEditDelay.setValidator(QtGui.QRegularExpressionValidator(r"\d{,2}[\.|\,]{1}\d{,3}"))

        self.__initThreads()
        self.__initSignals()

    def __initThreads(self):
        self.thread = SystemInfo()
        self.thread.start()

    def __initSignals(self):
        self.thread.systemInfoProgress.connect(lambda data: self.ui.lineEditCPU.setText(str(data[0])))
        self.thread.systemInfoProgress.connect(lambda data: self.ui.progressBarCPU.setValue(data[0]))
        self.thread.systemInfoProgress.connect(lambda data: self.ui.lineEditRAM.setText(str(data[1])))
        self.thread.systemInfoProgress.connect(lambda data: self.ui.progressBarRAM.setValue(data[1]))
        self.ui.pushButtonDelay.clicked.connect(self.onPushButtonDelay)

    def onPushButtonDelay(self):
        delay = float(self.ui.lineEditDelay.text().replace(',', '.'))
        self.thread.delay = delay
        self.ui.labelCurrentDelay.setText(f"Текущая задержка: {str(delay)} с")
        self.thread.terminate()
        self.thread.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = SystemInfoWidget()
    window.show()

    app.exec()
