"""
Модуль в котором содержаться потоки Qt
"""

import time
import traceback
from winreg import QueryValue

import psutil
import requests
from PySide6 import QtCore
from stua.os import system


class SystemInfo(QtCore.QThread):
    systemInfoProgress = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1

        while True:
            cpu_value = psutil.cpu_percent()
            ram_value = psutil.virtual_memory().percent
            self.systemInfoProgress.emit([cpu_value, ram_value])
            time.sleep(self.delay)


class WeatherHandler(QtCore.QThread):
    weather_info = QtCore.Signal(dict)

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)
        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        self.__status = None

    @property
    def delay(self):
        return self.__delay

    @delay.setter
    def delay(self, delay):
        self.__delay = delay

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    def run(self) -> None:
        self.__status = True

        try:
            while self.__status:
                response = requests.get(self.__api_url)
                data = response.json()
                self.weather_info.emit(data)
                self.sleep(self.__delay)
        except Exception:
            traceback.print_exc()
            self.__status = False
