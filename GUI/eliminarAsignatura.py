# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\eliminarAsignatura.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class eliminarAsignatura(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Eliminar Asignaturas")
        MainWindow.resize(536, 328)
        MainWindow.setStyleSheet("background-color: rgb(0, 51, 51)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtCodtBuscar = QtWidgets.QTextEdit(self.centralwidget)
        self.txtCodtBuscar.setGeometry(QtCore.QRect(180, 180, 201, 31))
        self.txtCodtBuscar.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.txtCodtBuscar.setObjectName("txtCodtBuscar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 30, 381, 61))
        self.label.setStyleSheet("\n"
"font: 75 8pt \"Segoe Print\";")
        self.label.setObjectName("label")
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setGeometry(QtCore.QRect(180, 260, 91, 31))
        self.btnEliminar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 204, 102);")
        self.btnEliminar.setObjectName("btnEliminar")
        self.btnRegresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(10, 260, 101, 31))
        self.btnRegresar.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 204, 102);")
        self.btnRegresar.setObjectName("btnRegresar")
        self.btnLimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpiar.setGeometry(QtCore.QRect(290, 260, 91, 31))
        self.btnLimpiar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 204, 102);")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.codigo_2 = QtWidgets.QLabel(self.centralwidget)
        self.codigo_2.setGeometry(QtCore.QRect(240, 150, 71, 21))
        self.codigo_2.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);")
        self.codigo_2.setObjectName("codigo_2")
        self.codigo = QtWidgets.QLabel(self.centralwidget)
        self.codigo.setGeometry(QtCore.QRect(210, 130, 191, 21))
        self.codigo.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);")
        self.codigo.setObjectName("codigo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 536, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Eliminar asignaturas"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Eliminar asignaturas</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.btnEliminar.setText(_translate("MainWindow", "ELIMINAR"))
        self.btnRegresar.setText(_translate("MainWindow", "REGRESAR"))
        self.btnLimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.codigo_2.setText(_translate("MainWindow", "<html><head/><body><p>asignatura</p></body></html>"))
        self.codigo.setText(_translate("MainWindow", "<html><head/><body><p>Ingrese codigo de la</p><p><br/></p></body></html>"))

