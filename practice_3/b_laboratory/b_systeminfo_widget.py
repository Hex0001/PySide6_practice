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
        self.thread.systemInfoProgress.connect(self.showSystemInfo)
        self.ui.pushButtonDelay.clicked.connect(self.onPushButtonDelay)

    def showSystemInfo(self, sys_info):
        self.ui.lineEditCPU.setText(str(sys_info[0]))
        self.ui.progressBarCPU.setValue(sys_info[0])
        self.ui.lineEditRAM.setText(str(sys_info[1]))
        self.ui.progressBarRAM.setValue(sys_info[1])

    def onPushButtonDelay(self):
        try:
            delay = float(self.ui.lineEditDelay.text().replace(',', '.'))
        except ValueError:
            print("Ошибка. Необходимо ввести значение задержки.")
        else:
            self.thread.delay = delay
            self.ui.labelCurrentDelay.setText(f"Текущая задержка: {delay} с")
            self.thread.terminate()
            self.thread.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = SystemInfoWidget()
    window.show()

    app.exec()
