"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets
from PySide6.QtCore import QFlag

from b_systeminfo_widget import SystemInfoWidget
from c_weatherapi_widget import WeatherWidget


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = QtWidgets.QWidget()
    window.setMaximumSize(800, 800)
    window.setWindowTitle("Двухпоточный виджет")

    system_info_widget = SystemInfoWidget()
    system_info_label = QtWidgets.QLabel("Системные данные")
    system_info_label.setStyleSheet("color: red; font-size: 20px; font-weight:600")
    weather_widget = WeatherWidget()
    weather_label = QtWidgets.QLabel("Погода")
    weather_label.setStyleSheet("color: red; font-size: 20px; font-weight:600")

    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(system_info_label)
    layout.addWidget(system_info_widget)
    layout.addWidget(weather_label)
    layout.addWidget(weather_widget)

    window.setLayout(layout)
    window.show()

    app.exec()
