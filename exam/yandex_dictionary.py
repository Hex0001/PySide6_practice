"""
Переводчик
"""

import requests
from PySide6 import QtWidgets
from exam.ui.yandex_dictionary import Ui_MainWindow


class YandexDictionaryWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__definitions = None
        self.__key = "dict.1.1.20241211T164235Z.c1b2d886faf5dc29.15588c680d5eeaa543fd1f1921cdc4e1b4e7f597"
        self.__ui_lng = "ru"

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__initLanguages()
        self.__initSignals()

        self.__mean = []

    def __initLanguages(self):
        url = f"https://dictionary.yandex.net/api/v1/dicservice.json/getLangs?key={self.__key}"

        response = requests.get(url)
        self.ui.comboBoxLanguageSelect.addItems(response.json())
        self.ui.comboBoxLanguageSelect.setCurrentText("en-ru")

    def __initSignals(self):
        self.ui.pushButtonOK.clicked.connect(self.onPushButtonOK)
        self.ui.comboBoxDefSelect.currentTextChanged.connect(self.onComboBoxDefChanged)

    def onPushButtonOK(self):
        url = f"https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={self.__key}&lang={self.ui.comboBoxLanguageSelect.currentText()}&text={self.ui.lineEditText.text()}&ui={self.__ui_lng}"
        response = requests.get(url)
        self.__definitions = Definitions(response.json()["def"])

        self.ui.comboBoxDefSelect.clear()
        self.ui.comboBoxDefSelect.addItems([str(i + 1) for i in range(self.__definitions.getLength())])

        if self.ui.comboBoxDefSelect.currentText():
            self.ui.plainTextEditDef.setPlainText(
                self.__definitions.getDefText(int(self.ui.comboBoxDefSelect.currentText()) - 1))
            self.ui.plainTextEditSyn.setPlainText(
                self.__definitions.getSynText(int(self.ui.comboBoxDefSelect.currentText()) - 1))
            self.ui.plainTextEditSyn.appendPlainText(
                f"Возможные варианты перевода:\n{self.__definitions.getMeanText(int(self.ui.comboBoxDefSelect.currentText()) - 1)}")
            self.ui.plainTextEditTranslate.setPlainText(
                self.__definitions.getTrText(int(self.ui.comboBoxDefSelect.currentText()) - 1))
            self.ui.plainTextEditTranslate.appendPlainText(
                self.__definitions.getExText(int(self.ui.comboBoxDefSelect.currentText()) - 1))
        else:
            self.ui.plainTextEditDef.setPlainText("Слово не найдено")
            self.ui.plainTextEditSyn.clear()
            self.ui.plainTextEditTranslate.clear()

    def onComboBoxDefChanged(self):
        if self.ui.comboBoxDefSelect.currentText():
            self.ui.plainTextEditDef.setPlainText(
                self.__definitions.getDefText(int(self.ui.comboBoxDefSelect.currentText()) - 1))
            self.ui.plainTextEditSyn.setPlainText(
                self.__definitions.getSynText(int(self.ui.comboBoxDefSelect.currentText()) - 1))
            self.ui.plainTextEditSyn.appendPlainText(
                f"Возможные варианты перевода:\n{self.__definitions.getMeanText(int(self.ui.comboBoxDefSelect.currentText()) - 1)}")
            self.ui.plainTextEditTranslate.setPlainText(
                self.__definitions.getTrText(int(self.ui.comboBoxDefSelect.currentText()) - 1))
            self.ui.plainTextEditTranslate.appendPlainText(
                self.__definitions.getExText(int(self.ui.comboBoxDefSelect.currentText()) - 1))


class Definitions:
    def __init__(self, definitions: list[dict]):
        self.__def_keys_russian = {"text": "Слово",
                                   "pos": "Часть речи",
                                   "asp": "Вид глагола",
                                   "ts": "Транскрипция",
                                   "anm": "Одушевленность"}
        self.__tr_syn_keys_russian = {"pos": "Часть речи",
                                      "gen": "Пол",
                                      "fr": "Частота употребления",
                                      "asp": "Вид глагола",
                                      "ts": "Транскрипция"}

        self.__definitions = definitions

    def getLength(self):
        return len(self.__definitions)

    def getDefText(self, index=0):
        text = ''

        text += f"{self.__definitions[index]["text"]}\n"
        for key, value in self.__definitions[index].items():
            if key not in ("text", "tr", "gen"):
                text += f"{self.__def_keys_russian[key]}: {value}\n"
        return text

    def getTrText(self, index=0):
        text = ''
        translations = self.__definitions[index]["tr"]

        for translation in translations:
            text += f"{translation["text"]}\n"
        return text

    def getSynText(self, index=0):
        text = ''
        translations = self.__definitions[index]["tr"]

        for translation in translations:
            if "syn" in translation.keys():
                for syn in translation["syn"]:
                    text += f"{syn["text"]}\n"
                    for key, value in syn.items():
                        if key != "text":
                            text += f"    {self.__tr_syn_keys_russian[key]}: {value}\n"
        return text

    def getMeanText(self, index=0):
        text = ''
        translations = self.__definitions[index]["tr"]

        for translation in translations:
            if "mean" in translation.keys():
                for mean in translation["mean"]:
                    text += f"{mean["text"]}\n"
        return text

    def getExText(self, index=0):
        text = ''
        translations = self.__definitions[index]["tr"]

        for translation in translations:
            if "ex" in translation.keys():
                for ex in translation["ex"]:
                    text += f"{ex["text"]}, перевод: {ex["tr"]}\n"
        return text


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = YandexDictionaryWindow()
    window.show()

    app.exec()
