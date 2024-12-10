"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""
import time

from PySide6 import QtWidgets, QtGui
from ui.weather import Ui_Form
from a_threads import WeatherHandler


class WeatherWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.__initSignals()
        self.validateLineEdits()


    def __initSignals(self):
        self.ui.pushButtonHandle.clicked.connect(self.__handleThread)

    def __handleThread(self, status):
        self.ui.pushButtonHandle.setText("Стоп" if status else "Старт")
        lat = None
        lon = None

        if not status:
            self.thread.status = False
            self.ui.textBrowserWeather.append("Опрос сервера завершён.")
            self.thread.terminate()  # Уничтожаем для предотвращения вылета программы из-за внедрения данных в
            # текущий поток
            self.lineEditsSwitch()
        else:
            if self.currentLatCheck() and self.currentLonCheck():
                lat = float(self.ui.lineEditLat.text().replace(',', '.'))
                lon = float(self.ui.lineEditLon.text().replace(',', '.'))
                if self.ui.lineEditDelay.text():
                    delay = float(self.ui.lineEditDelay.text().replace(',', '.'))
                else:
                    delay = 10
                self.thread = WeatherHandler(lat, lon)
                self.thread.delay = delay

                self.thread.started.connect(lambda: self.lineEditsSwitch())
                self.thread.weather_info.connect(self.showWeatherInfo)
                self.thread.start()
            else:
                self.ui.textBrowserWeather.setText("Неверные координаты.\nШирота должна быть в интервале: [-90, 90]\n"
                                                   "Долгота должна быть в интервале: [-180, 180]")
                self.ui.pushButtonHandle.setChecked(False)
                self.ui.pushButtonHandle.setText("Старт")

    def validateLineEdits(self) -> None:
        """
        Валидация полей ввода
        :return: None
        """
        self.ui.lineEditDelay.setValidator(QtGui.QRegularExpressionValidator(r"\d{,2}[\. | \,]{1}\d{,3}"))
        self.ui.lineEditLat.setValidator(QtGui.QRegularExpressionValidator(r"\-?\d{,2}[\. | \,]{1}\d{,2}"))
        self.ui.lineEditLon.setValidator(QtGui.QRegularExpressionValidator(r"\-?\d{,3}[\. | \,]{1}\d{,2}"))

    def currentLatCheck(self) -> bool:
        """
        Метод проверяет поле ввода широты на существование и на соответствие нужному интервалу [-90, 90]
        :return: bool
        """
        if self.ui.lineEditLat.text() and -90 <= float(self.ui.lineEditLat.text().replace(',', '.')) <= 90:
            return True
        else:
            return False

    def currentLonCheck(self) -> bool:
        """
        Метод проверяет поле ввода долготы на существование и на соответствие нужному интервалу [-180, 180]
        :return: bool
        """
        if self.ui.lineEditLon.text() and -180 <= float(self.ui.lineEditLon.text().replace(',', '.')) <= 180:
            return True
        else:
            return False

    def lineEditsSwitch(self) -> None:
        """
        Метод переключает блокировку полей ввода
        :return: None
        """
        switcher = False if self.ui.lineEditLat.isEnabled() else True
        self.ui.lineEditLat.setEnabled(switcher)
        self.ui.lineEditLon.setEnabled(switcher)
        self.ui.lineEditDelay.setEnabled(switcher)

    def showWeatherInfo(self, data):
        self.ui.textBrowserWeather.setText(f"Время: {time.ctime()}")
        self.ui.textBrowserWeather.append(f"Задержка обновления: {self.thread.delay} с")
        self.ui.textBrowserWeather.append(f"Широта: {round(data["latitude"], 2)}")
        self.ui.textBrowserWeather.append(f"Долгота: {round(data["longitude"], 2)}")
        self.ui.textBrowserWeather.append(f"Время на сервере: {data["current_weather"]["time"]}")
        self.ui.textBrowserWeather.append(f"Задержка на сервере: {data["current_weather"]["interval"]} "
                                          f"{data["current_weather_units"]["interval"]}")
        self.ui.textBrowserWeather.append(f"Температура: {round(data["current_weather"]["temperature"], 2)} "
                                          f"{data["current_weather_units"]["temperature"]}")
        self.ui.textBrowserWeather.append(f"Скорость ветра: {data["current_weather"]["windspeed"]} "
                                          f"{data["current_weather_units"]["windspeed"]}")
        self.ui.textBrowserWeather.append(f"Направление ветра: {data["current_weather"]["winddirection"]} "
                                          f"{data["current_weather_units"]["winddirection"]}")
        self.ui.textBrowserWeather.append("День" if data["current_weather"]["is_day"] else "Ночь")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = WeatherWidget()
    window.show()

    app.exec()
