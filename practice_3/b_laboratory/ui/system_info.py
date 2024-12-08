# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'system_info.ui'
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
    QProgressBar, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(336, 110)
        Form.setMaximumSize(QSize(750, 200))
        self.horizontalLayout_4 = QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelDelay = QLabel(Form)
        self.labelDelay.setObjectName(u"labelDelay")

        self.horizontalLayout.addWidget(self.labelDelay)

        self.lineEditDelay = QLineEdit(Form)
        self.lineEditDelay.setObjectName(u"lineEditDelay")

        self.horizontalLayout.addWidget(self.lineEditDelay)

        self.pushButtonDelay = QPushButton(Form)
        self.pushButtonDelay.setObjectName(u"pushButtonDelay")

        self.horizontalLayout.addWidget(self.pushButtonDelay)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.labelCurrentDelay = QLabel(Form)
        self.labelCurrentDelay.setObjectName(u"labelCurrentDelay")

        self.verticalLayout.addWidget(self.labelCurrentDelay)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelCPU = QLabel(Form)
        self.labelCPU.setObjectName(u"labelCPU")
        self.labelCPU.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_2.addWidget(self.labelCPU)

        self.lineEditCPU = QLineEdit(Form)
        self.lineEditCPU.setObjectName(u"lineEditCPU")
        self.lineEditCPU.setMaximumSize(QSize(150, 16777215))
        self.lineEditCPU.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEditCPU)

        self.progressBarCPU = QProgressBar(Form)
        self.progressBarCPU.setObjectName(u"progressBarCPU")
        self.progressBarCPU.setValue(24)

        self.horizontalLayout_2.addWidget(self.progressBarCPU)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelRAM = QLabel(Form)
        self.labelRAM.setObjectName(u"labelRAM")
        self.labelRAM.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_3.addWidget(self.labelRAM)

        self.lineEditRAM = QLineEdit(Form)
        self.lineEditRAM.setObjectName(u"lineEditRAM")
        self.lineEditRAM.setMaximumSize(QSize(150, 16777215))
        self.lineEditRAM.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEditRAM)

        self.progressBarRAM = QProgressBar(Form)
        self.progressBarRAM.setObjectName(u"progressBarRAM")
        self.progressBarRAM.setValue(24)

        self.horizontalLayout_3.addWidget(self.progressBarRAM)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"SystemInfo", None))
        self.labelDelay.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0438 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f, \u0441", None))
        self.pushButtonDelay.setText(QCoreApplication.translate("Form", u"OK", None))
        self.labelCurrentDelay.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0430: 1 \u0441", None))
        self.labelCPU.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 CPU", None))
        self.labelRAM.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 RAM", None))
    # retranslateUi

