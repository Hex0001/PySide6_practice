"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings_form.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""
from winreg import KEY_WOW64_64KEY

from PySide6 import QtWidgets, QtCore
from PySide6.scripts.project import QTPATHS_CMD
from urllib3.poolmanager import key_fn_by_scheme

from practice_2.b_laboratory.ui.d_eventfilter_settings_form import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.dial.installEventFilter(self)
        self.ui.horizontalSlider.installEventFilter(self)

        self.ui.lcdNumber.setDigitCount(7)  # Установленные 5 знаков из ui мало для bin
        self.lcd_modes = {"hex": QtWidgets.QLCDNumber.Mode.Hex,
                          "dec": QtWidgets.QLCDNumber.Mode.Dec,
                          "oct": QtWidgets.QLCDNumber.Mode.Oct,
                          "bin": QtWidgets.QLCDNumber.Mode.Bin}
        self.ui.comboBox.addItems(self.lcd_modes.keys())
        self.ui.comboBox.currentTextChanged.connect(lambda mode: self.ui.lcdNumber.setMode(self.lcd_modes[mode]))
        self.__loadSettings()

    def eventFilter(self, watched, event):
        if watched == self.ui.dial:
            if event.type() == QtCore.QEvent.Type.KeyPress:
                if event.key() == QtCore.Qt.Key.Key_Plus:
                    self.ui.dial.setValue(self.ui.dial.value() + 1)
                elif event.key() == QtCore.Qt.Key.Key_Minus:
                    self.ui.dial.setValue(self.ui.dial.value() - 1)
            self.ui.lcdNumber.display(self.ui.dial.value())
            self.ui.horizontalSlider.setValue(self.ui.dial.value())

        if watched == self.ui.horizontalSlider:
            if event.type() == QtCore.QEvent.Type.MouseMove:
                self.ui.lcdNumber.display(self.ui.horizontalSlider.value())
                self.ui.dial.setValue(self.ui.horizontalSlider.value())

        return super().eventFilter(watched, event)

    def closeEvent(self, event):
        self.__saveSettings()
        return super().closeEvent(event)

    def __loadSettings(self):
        settings = QtCore.QSettings("comboBox_LCD")
        self.ui.comboBox.setCurrentText(settings.value("comboBoxText", "dec"))
        self.ui.lcdNumber.setMode(self.lcd_modes[settings.value("comboBoxText", "dec")])
        self.ui.dial.setValue(settings.value("lcdNumberValue", 0))

    def __saveSettings(self):
        settings = QtCore.QSettings("comboBox_LCD")
        settings.setValue("comboBoxText", self.ui.comboBox.currentText())
        settings.setValue("lcdNumberValue", int(self.ui.lcdNumber.value()))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
