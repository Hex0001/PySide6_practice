# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weather.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 350)
        Form.setMinimumSize(QSize(300, 350))
        Form.setMaximumSize(QSize(600, 600))
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelLat = QLabel(Form)
        self.labelLat.setObjectName(u"labelLat")

        self.verticalLayout.addWidget(self.labelLat)

        self.labelLon = QLabel(Form)
        self.labelLon.setObjectName(u"labelLon")

        self.verticalLayout.addWidget(self.labelLon)

        self.labelDelay = QLabel(Form)
        self.labelDelay.setObjectName(u"labelDelay")

        self.verticalLayout.addWidget(self.labelDelay)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEditLat = QLineEdit(Form)
        self.lineEditLat.setObjectName(u"lineEditLat")

        self.verticalLayout_2.addWidget(self.lineEditLat)

        self.lineEditLon = QLineEdit(Form)
        self.lineEditLon.setObjectName(u"lineEditLon")

        self.verticalLayout_2.addWidget(self.lineEditLon)

        self.lineEditDelay = QLineEdit(Form)
        self.lineEditDelay.setObjectName(u"lineEditDelay")

        self.verticalLayout_2.addWidget(self.lineEditDelay)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.textBrowserWeather = QTextBrowser(Form)
        self.textBrowserWeather.setObjectName(u"textBrowserWeather")

        self.verticalLayout_3.addWidget(self.textBrowserWeather)

        self.pushButtonHandle = QPushButton(Form)
        self.pushButtonHandle.setObjectName(u"pushButtonHandle")
        self.pushButtonHandle.setCheckable(True)
        self.pushButtonHandle.setChecked(False)

        self.verticalLayout_3.addWidget(self.pushButtonHandle)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Weather", None))
        self.labelLat.setText(QCoreApplication.translate("Form", u"\u0428\u0438\u0440\u043e\u0442\u0430", None))
        self.labelLon.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u043b\u0433\u043e\u0442\u0430", None))
        self.labelDelay.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430", None))
        self.pushButtonHandle.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
    # retranslateUi

