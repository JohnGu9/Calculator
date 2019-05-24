import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, qApp

from cal import Ui_MainWindow

import webbrowser

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!



class myWin(QMainWindow):


    def __init__(self):
        super().__init__()
        self.operation = ''
        self.parameter_1, parameter_2 = '', ''  

    def Calculate(self):
        global text
        global ui

        sender = self.sender()
        self.statusBar().showMessage(sender.text()) 

        if sender.text()>='0' and sender.text()<='9':
            text = text + sender.text()

        elif sender.text() == '+' or sender.text() == '-' or sender.text() == '*' or sender.text() == '/' :
            self.operation = sender.text()
            self.parameter_1 = int(text)
            text = ''

        elif sender.text() == '=':  
            self.parameter_2 = int(text)
            self.result = self.parameter_1

            if self.operation == '+':
                self.result += self.parameter_2
            elif self.operation == '-':
                self.result -= self.parameter_2
            elif self.operation == '*':                
                self.result *= self.parameter_2
            elif self.operation == '/':                
                self.result /= self.parameter_2

            text = str(self.result)
            self.parameter_1 = self.result
            
        elif sender.text() == 'CE':
            self.operation = ''
            self.parameter_1, parameter_2 = '', ''
            text = ''

        else:   #debug
             print(sender.text()) 

        ui.lineEdit.setText(text)


class myMainWin(Ui_MainWindow):

    Website_url = 'https://github.com/JohnGu9'

    def __init__(self):
        super().__init__()  

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.Quit.triggered.connect(lambda:QtCore.QCoreApplication.instance().quit())
        self.license.triggered.connect(lambda:self.lineEdit.setText('No license'))
        self.Webusite.triggered.connect(lambda:webbrowser.open(self.Website_url))



if __name__ == '__main__':  

    text = ''
    app = QApplication(sys.argv)
    window = myWin()

    ui = myMainWin()
    ui.setupUi(window)
    ui.lineEdit.setText(text)

    window.show()

    sys.exit(app.exec_())