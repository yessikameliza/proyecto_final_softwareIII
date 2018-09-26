# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(376, 373)
        Form.setStyleSheet("background-color: rgb(0, 51, 51)")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 30, 281, 61))
        self.label.setStyleSheet("\n"
"font: 75 8pt \"Segoe Print\";")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(60, 120, 261, 221))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(30, 30, 211, 31))
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 51, 51)\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 90, 211, 31))
        self.textEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 51, 51)\n"
"")
        self.textEdit_2.setObjectName("textEdit_2")
        self.btnAgregar = QtWidgets.QPushButton(self.frame)
        self.btnAgregar.setGeometry(QtCore.QRect(30, 160, 211, 41))
        self.btnAgregar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 204, 102);")
        self.btnAgregar.setObjectName("btnAgregar")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 141, 16))
        self.label_2.setStyleSheet("font: 75 10pt \"Segoe Print\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 91, 16))
        self.label_3.setStyleSheet("font: 75 10pt \"Segoe Print\";")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Log-in</span></p></body></html>"))
        self.btnAgregar.setText(_translate("Form", "Iniciar Sesion"))
        self.label_2.setText(_translate("Form", "Nombre de usuario "))
        self.label_3.setText(_translate("Form", "Contraseña"))

