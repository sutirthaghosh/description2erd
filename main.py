from mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import *
import nltk.data
import nltk
import mkdb
import gexp
sentences = []


def copyText():
    ui.textEdit_Output.setPlainText(ui.textEdit_Input.toPlainText())


def sentence_segmentation():
    global sentences
    sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = sentence_detector.tokenize(ui.textEdit_Input.toPlainText())
    ui.textEdit_Output.setPlainText("Sentence Segmentation")
    ui.textEdit_Output.setPlainText("")
    for sentence in sentences:
        ui.textEdit_Output.append(sentence)
        ui.textEdit_Output.append('\n')
        print(sentence)


def tokenize():
    sentence_tokens = []
    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)
        words = [w.lower() for w in tokens if w.isalnum()]
        sentence_tokens.append(words)
    ui.textEdit_Output.setPlainText("")
    for words in sentence_tokens:
        for word in words:
            ui.textEdit_Output.moveCursor(QTextCursor.End)
            ui.textEdit_Output.insertPlainText(word+"    |   ")
        ui.textEdit_Output.append('\n')
        print(words)

def namedEntity():
    mkdb.createdb("words.db")
    sentence_tokens = []
    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)
        words = [w.lower() for w in tokens if w.isalnum()]
        sentence_tokens.append(words)
    ui.textEdit_Output.setPlainText("")
    for words in sentence_tokens:
        for word in words:
            ui.textEdit_Output.moveCursor(QTextCursor.End)
            entity = mkdb.searchname(word, 'Ename_synonym', 'Ename_base')
            ui.textEdit_Output.insertPlainText(word+"   {"+str(entity)+"}  ")
        ui.textEdit_Output.append('\n')
        print(words)

if __name__ == "__main__":
    import sys
    print("hi")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ##connections
    ui.textEdit_Input.textChanged.connect(copyText)
    ui.pushButton_4.clicked.connect(sentence_segmentation)
    ui.pushButton.clicked.connect(tokenize)
    ui.pushButton_3.clicked.connect(namedEntity)
    sys.exit(app.exec_())


