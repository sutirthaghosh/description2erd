from mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import *
import nltk.data
import nltk


def copyText():
    ui.textEdit_Output.setPlainText(ui.textEdit_Input.toPlainText())


def sentence_segmentation():
    sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = sentence_detector.tokenize(ui.textEdit_Input.toPlainText())
    ui.textEdit_Output.setPlainText("Sentence Segmentation")
    ui.textEdit_Output.setPlainText("")
    for sentence in sentences:
        ui.textEdit_Output.append(sentence)
        ui.textEdit_Output.append('\n')
        print(sentence)

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
    sys.exit(app.exec_())


