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
    lat = QtCore.Signal(str)
    lon = QtCore.Signal(str)
    time = QtCore.Signal(str)
    interval = QtCore.Signal(str)
    temperature = QtCore.Signal(str)
    windspeed = QtCore.Signal(str)
    winddirection = QtCore.Signal(str)
    is_day = QtCore.Signal(bool)

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)
        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        self.__status = None

    def getDelay(self):
        return self.__delay

    def setDelay(self, delay):
        self.__delay = delay

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = status

    def run(self) -> None:
        self.__status = True

        try:
            while self.__status:
                response = requests.get(self.__api_url)
                data = response.json()
                self.lat.emit(f"{round(data["latitude"], 2)}")
                self.lon.emit(f"{round(data["longitude"], 2)}")
                self.time.emit(f"{data["current_weather"]["time"]}")
                self.interval.emit(f"{data["current_weather"]["interval"]} {data["current_weather_units"]["interval"]}")
                self.temperature.emit(f"{round(data["current_weather"]["temperature"], 2)} {data["current_weather_units"]["temperature"]}")
                self.windspeed.emit(f"{data["current_weather"]["windspeed"]} {data["current_weather_units"]["windspeed"]}")
                self.winddirection.emit(f"{data["current_weather"]["winddirection"]} {data["current_weather_units"]["winddirection"]}")
                self.is_day.emit(data["current_weather"]["is_day"])
                self.sleep(self.__delay)
        except Exception:
            traceback.print_exc()
            self.__status = False
