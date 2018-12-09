# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calculator(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(252, 416)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(0, 80, 251, 41))
        self.label.setStyleSheet("QLabel { qproperty-alignment: \'AlignVCenter | AlignRight\';} QLabel { border: 1px solidgray;}\n"
"\n"
"background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(0, 130, 61, 61))
        self.pushButton_clear.setStyleSheet("QPushButton {border: 1px solid gray;}\n"
"QPushButton:pressed {background-color: rgb(177, 0, 255);}\n"
"QPushButton {background-color: rgb(253, 100, 67);}\n"
"\n"
"\n"
"")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_plusMinus = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_plusMinus.setGeometry(QtCore.QRect(60, 130, 61, 61))
        self.pushButton_plusMinus.setStyleSheet("QPushButton {border: 1px solid gray;}\n"
"QPushButton:pressed {background-color: rgb(177, 0, 255);}\n"
"QPushButton {background-color: rgb(253, 100, 67);}\n"
"\n"
"\n"
"")
        self.pushButton_plusMinus.setObjectName("pushButton_plusMinus")
        self.pushButton_percent = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_percent.setGeometry(QtCore.QRect(120, 130, 61, 61))
        self.pushButton_percent.setStyleSheet("QPushButton {border: 1px solid gray;}\n"
"QPushButton:pressed {background-color: rgb(177, 0, 255);}\n"
"QPushButton {background-color: rgb(253, 100, 67);}\n"
"\n"
"\n"
"")
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.pushButton_divide = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_divide.setGeometry(QtCore.QRect(180, 130, 71, 61))
        self.pushButton_divide.setStyleSheet("QPushButton {border: 1px solid gray;}\n"
"QPushButton:pressed {background-color: rgb(177, 0, 255);}\n"
"QPushButton {background-color: rgb(253, 100, 67);}\n"
"\n"
"\n"
"")
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_multiple = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_multiple.setGeometry(QtCore.QRect(180, 190, 71, 61))
        self.pushButton_multiple.setStyleSheet("QPushButton {border: 1px solid gray;}\n"
"QPushButton:pressed {background-color: rgb(177, 0, 255);}\n"
"QPushButton {background-color: rgb(253, 100, 67);}\n"
"\n"
"\n"
"")
        self.pushButton_multiple.setObjectName("pushButton_multiple")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 190, 61, 61))
        self.pushButton_8.setStyleSheet("QPushButton {border: 1px solid gray;}\n"
"QPushButton:pressed {background-color: rgb(84, 86, 255);}\n"
"QPushButton {background-color: rgb(84, 189, 255);}\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 190, 61, 61))
        self.pushButton_7.setStyleSheet("QPushButton {border: 1px solid gray;}\n"
"QPushButton:pressed {background-color: rgb(84, 86, 255);}\n"
"QPushButton {background-color: rgb(84, 189, 255);}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_9.setGeometry(QtCore.QRect(120, 190, 61, 61))
        self.pushButton_9.setStyleSheet("QPushButton {border: 1px solid gray;}\n"
"QPushButton:pressed {background-color: rgb(84, 86, 255);}\n"
"QPushButton {background-color: rgb(84, 189, 255);}\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_subtract = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_subtract.setGeometry(QtCore.QRect(180, 250, 71, 51))
        self.pushButton_subtract.setStyleSheet("QPushButton {border: 1px solid gray;}\n"
"QPushButton:pressed {background-color: rgb(177, 0, 255);}\n"
"QPushButton {background-color: rgb(253, 100, 67);}\n"
"\n"
"\n"
"")
        self.pushButton_subtract.setObjectName("pushButton_subtract")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 250, 61, 51))
        self.pushButton_5.setStyleSheet("QPushButton {border: 1px solid gray;}\n"
"QPushButton:pressed {background-color: rgb(84, 86, 255);}\n"
"QPushButton {background-color: rgb(84, 189, 255);}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 250, 61, 51))
        self.pushButton_4.setStyleSheet("QPushButton {border: 1px solid gray;}\n"
"QPushButton:pressed {background-color: rgb(84, 86, 255);}\n"
"QPushButton {background-color: rgb(84, 189, 255);}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 250, 61, 51))
        self.pushButton_6.setStyleSheet("QPushButton {border: 1px solid gray;}\n"
"QPushButton:pressed {background-color: rgb(84, 86, 255);}\n"
"QPushButton {background-color: rgb(84, 189, 255);}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_add = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_add.setGeometry(QtCore.QRect(180, 300, 71, 51))
        self.pushButton_add.setStyleSheet("QPushButton {border: 1px solid gray;}\n"
"QPushButton:pressed {background-color: rgb(177, 0, 255);}\n"
"QPushButton {background-color: rgb(253, 100, 67);}\n"
"\n"
"\n"
"")
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 300, 61, 51))
        self.pushButton_2.setStyleSheet("QPushButton {border: 1px solid gray;}\n"
"QPushButton:pressed {background-color: rgb(84, 86, 255);}\n"
"QPushButton {background-color: rgb(84, 189, 255);}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 300, 61, 51))
        self.pushButton_1.setStyleSheet("QPushButton {border: 1px solid gray;}\n"
"QPushButton:pressed {background-color: rgb(84, 86, 255);}\n"
"QPushButton {background-color: rgb(84, 189, 255);}\n"
"")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 300, 61, 51))
        self.pushButton_3.setStyleSheet("QPushButton {border: 1px solid gray;}\n"
"QPushButton:pressed {background-color: rgb(84, 86, 255);}\n"
"QPushButton {background-color: rgb(84, 189, 255);}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_0.setGeometry(QtCore.QRect(0, 350, 121, 61))
        self.pushButton_0.setStyleSheet("QPushButton {border: 1px solid gray;}\n"
"QPushButton:pressed {background-color: rgb(84, 86, 255);}\n"
"QPushButton {background-color: rgb(84, 189, 255);}\n"
"")
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_decimal = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_decimal.setGeometry(QtCore.QRect(120, 350, 61, 61))
        self.pushButton_decimal.setStyleSheet("QPushButton {border: 1px solid gray;}\n"
"QPushButton:pressed {background-color: rgb(177, 0, 255);}\n"
"QPushButton {background-color: rgb(253, 100, 67);}\n"
"\n"
"\n"
"")
        self.pushButton_decimal.setObjectName("pushButton_decimal")
        self.pushButton_equals = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_equals.setGeometry(QtCore.QRect(180, 350, 71, 61))
        self.pushButton_equals.setStyleSheet("QPushButton {border: 1px solid gray;}\n"
"QPushButton:pressed {background-color: rgb(177, 0, 255);}\n"
"QPushButton {background-color: rgb(253, 100, 67);}\n"
"\n"
"\n"
"")
        self.pushButton_equals.setObjectName("pushButton_equals")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(148, 10, 101, 41))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "0"))
        self.pushButton_clear.setText(_translate("MainWindow", "C"))
        self.pushButton_plusMinus.setText(_translate("MainWindow", "+/-"))
        self.pushButton_percent.setText(_translate("MainWindow", "%"))
        self.pushButton_divide.setText(_translate("MainWindow", "÷"))
        self.pushButton_multiple.setText(_translate("MainWindow", "X"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_subtract.setText(_translate("MainWindow", "-"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_decimal.setText(_translate("MainWindow", "."))
        self.pushButton_equals.setText(_translate("MainWindow", "="))
        self.label_2.setText(_translate("MainWindow", "ktora_godzina"))

