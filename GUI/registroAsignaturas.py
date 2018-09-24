# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\registroAsignaturas.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 530)
        MainWindow.setStyleSheet("background-color: rgb(0, 51, 51)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 381, 61))
        self.label.setStyleSheet("\n"
"font: 75 8pt \"Segoe Print\";")
        self.label.setObjectName("label")
        self.txtCodigo = QtWidgets.QTextEdit(self.centralwidget)
        self.txtCodigo.setGeometry(QtCore.QRect(260, 140, 221, 31))
        self.txtCodigo.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.txtCodigo.setObjectName("txtCodigo")
        self.nombre = QtWidgets.QLabel(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(40, 200, 91, 21))
        self.nombre.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.nombre.setObjectName("nombre")
        self.codigo = QtWidgets.QLabel(self.centralwidget)
        self.codigo.setGeometry(QtCore.QRect(40, 140, 91, 31))
        self.codigo.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.codigo.setObjectName("codigo")
        self.txtNombre = QtWidgets.QTextEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(260, 200, 221, 31))
        self.txtNombre.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.txtNombre.setObjectName("txtNombre")
        self.numCreditos = QtWidgets.QLabel(self.centralwidget)
        self.numCreditos.setGeometry(QtCore.QRect(40, 260, 171, 61))
        self.numCreditos.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.numCreditos.setObjectName("numCreditos")
        self.txtNumHorSemestre = QtWidgets.QTextEdit(self.centralwidget)
        self.txtNumHorSemestre.setGeometry(QtCore.QRect(260, 310, 221, 31))
        self.txtNumHorSemestre.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.txtNumHorSemestre.setObjectName("txtNumHorSemestre")
        self.numHorasSemestre = QtWidgets.QLabel(self.centralwidget)
        self.numHorasSemestre.setGeometry(QtCore.QRect(40, 310, 211, 61))
        self.numHorasSemestre.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.numHorasSemestre.setObjectName("numHorasSemestre")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(260, 450, 101, 31))
        self.btnAceptar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 204, 102);")
        self.btnAceptar.setObjectName("btnAceptar")
        self.btnLimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpiar.setGeometry(QtCore.QRect(370, 450, 111, 31))
        self.btnLimpiar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 204, 102);")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.btnRegresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(40, 450, 101, 31))
        self.btnRegresar.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 204, 102);")
        self.btnRegresar.setObjectName("btnRegresar")
        self.semestre = QtWidgets.QLabel(self.centralwidget)
        self.semestre.setGeometry(QtCore.QRect(40, 370, 211, 61))
        self.semestre.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.semestre.setObjectName("semestre")
        self.boxSemestre = QtWidgets.QSpinBox(self.centralwidget)
        self.boxSemestre.setGeometry(QtCore.QRect(260, 370, 71, 22))
        self.boxSemestre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.boxSemestre.setMinimum(1)
        self.boxSemestre.setMaximum(6)
        self.boxSemestre.setProperty("value", 1)
        self.boxSemestre.setObjectName("boxSemestre")
        self.boxCreditos = QtWidgets.QSpinBox(self.centralwidget)
        self.boxCreditos.setGeometry(QtCore.QRect(260, 260, 71, 22))
        self.boxCreditos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.boxCreditos.setMinimum(1)
        self.boxCreditos.setMaximum(6)
        self.boxCreditos.setProperty("value", 1)
        self.boxCreditos.setObjectName("boxCreditos")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Registro de asignaturas</span></p><p align=\"center\"><br/></p></body></html>"))
        self.nombre.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Nombre:</span></p></body></html>"))
        self.codigo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Codigo:</span></p><p><br/></p></body></html>"))
        self.numCreditos.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Numero de creditos:</span></p><p><br/></p></body></html>"))
        self.numHorasSemestre.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Num. horas por semestre:</span></p><p><br/></p></body></html>"))
        self.btnAceptar.setText(_translate("MainWindow", "ACEPTAR"))
        self.btnLimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.btnRegresar.setText(_translate("MainWindow", "REGRESAR"))
        self.semestre.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Semestre:</span></p><p><br/></p><p><br/></p></body></html>"))

