# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'yandex_dictionary.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(767, 740)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEditText = QLineEdit(self.centralwidget)
        self.lineEditText.setObjectName(u"lineEditText")

        self.horizontalLayout.addWidget(self.lineEditText)

        self.pushButtonOK = QPushButton(self.centralwidget)
        self.pushButtonOK.setObjectName(u"pushButtonOK")

        self.horizontalLayout.addWidget(self.pushButtonOK)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelLanguageSelect = QLabel(self.centralwidget)
        self.labelLanguageSelect.setObjectName(u"labelLanguageSelect")

        self.horizontalLayout_2.addWidget(self.labelLanguageSelect)

        self.comboBoxLanguageSelect = QComboBox(self.centralwidget)
        self.comboBoxLanguageSelect.setObjectName(u"comboBoxLanguageSelect")

        self.horizontalLayout_2.addWidget(self.comboBoxLanguageSelect)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelDefSelect = QLabel(self.centralwidget)
        self.labelDefSelect.setObjectName(u"labelDefSelect")

        self.horizontalLayout_3.addWidget(self.labelDefSelect)

        self.comboBoxDefSelect = QComboBox(self.centralwidget)
        self.comboBoxDefSelect.setObjectName(u"comboBoxDefSelect")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxDefSelect.sizePolicy().hasHeightForWidth())
        self.comboBoxDefSelect.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.comboBoxDefSelect)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelDef = QLabel(self.centralwidget)
        self.labelDef.setObjectName(u"labelDef")

        self.verticalLayout.addWidget(self.labelDef)

        self.plainTextEditDef = QPlainTextEdit(self.centralwidget)
        self.plainTextEditDef.setObjectName(u"plainTextEditDef")
        self.plainTextEditDef.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEditDef)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelTranslate = QLabel(self.centralwidget)
        self.labelTranslate.setObjectName(u"labelTranslate")

        self.verticalLayout_3.addWidget(self.labelTranslate)

        self.plainTextEditTranslate = QPlainTextEdit(self.centralwidget)
        self.plainTextEditTranslate.setObjectName(u"plainTextEditTranslate")
        self.plainTextEditTranslate.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.plainTextEditTranslate)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelSyn = QLabel(self.centralwidget)
        self.labelSyn.setObjectName(u"labelSyn")

        self.verticalLayout_4.addWidget(self.labelSyn)

        self.plainTextEditSyn = QPlainTextEdit(self.centralwidget)
        self.plainTextEditSyn.setObjectName(u"plainTextEditSyn")
        self.plainTextEditSyn.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.plainTextEditSyn)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 767, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434\u0447\u0438\u043a-\u0441\u043b\u043e\u0432\u0430\u0440\u044c", None))
        self.lineEditText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.pushButtonOK.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.labelLanguageSelect.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u044f\u0437\u044b\u043a\u0430", None))
        self.labelDefSelect.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u043d\u043e\u043c\u0435\u0440\u0430 \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u0430:", None))
        self.labelDef.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.labelTranslate.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434:", None))
        self.labelSyn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u043e\u043d\u0438\u043c\u044b:", None))
    # retranslateUi

