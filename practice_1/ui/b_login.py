# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'b_login.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(470, 140)
        Form.setMaximumSize(QSize(470, 140))
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEditLogin = QLineEdit(Form)
        self.lineEditLogin.setObjectName(u"lineEditLogin")

        self.verticalLayout_2.addWidget(self.lineEditLogin)

        self.lineEditPassword = QLineEdit(Form)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        self.lineEditPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.lineEditPassword)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonLogin = QPushButton(Form)
        self.pushButtonLogin.setObjectName(u"pushButtonLogin")

        self.horizontalLayout_2.addWidget(self.pushButtonLogin)

        self.pushButtonCancel = QPushButton(Form)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")

        self.horizontalLayout_2.addWidget(self.pushButtonCancel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.pushButtonRegistration = QPushButton(Form)
        self.pushButtonRegistration.setObjectName(u"pushButtonRegistration")

        self.verticalLayout_3.addWidget(self.pushButtonRegistration)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.lineEditLogin.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448 \u0442\u0435\u043b\u0435\u0444\u043e\u043d/email/login_id", None))
        self.lineEditPassword.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButtonLogin.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.pushButtonRegistration.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

