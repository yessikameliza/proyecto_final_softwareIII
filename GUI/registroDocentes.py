# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\registroDocentes.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class registroDocentes(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 777)
        MainWindow.setStyleSheet("background-color: rgb(0, 51, 51)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 50, 341, 61))
        self.label.setStyleSheet("\n"
"font: 75 8pt \"Segoe Print\";")
        self.label.setObjectName("label")
        self.nombre = QtWidgets.QLabel(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(60, 170, 91, 21))
        self.nombre.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.nombre.setObjectName("nombre")
        self.identifi = QtWidgets.QLabel(self.centralwidget)
        self.identifi.setGeometry(QtCore.QRect(60, 220, 141, 31))
        self.identifi.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.identifi.setObjectName("identifi")
        self.tipo = QtWidgets.QLabel(self.centralwidget)
        self.tipo.setGeometry(QtCore.QRect(60, 270, 71, 31))
        self.tipo.setStyleSheet("\n"
"font: 75 8pt \"Segoe Print\";")
        self.tipo.setObjectName("tipo")
        self.txtNombre = QtWidgets.QTextEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(250, 170, 241, 31))
        self.txtNombre.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.txtNombre.setObjectName("txtNombre")
        self.txtIdent = QtWidgets.QTextEdit(self.centralwidget)
        self.txtIdent.setGeometry(QtCore.QRect(250, 220, 241, 31))
        self.txtIdent.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.txtIdent.setObjectName("txtIdent")
        self.txtTipo = QtWidgets.QTextEdit(self.centralwidget)
        self.txtTipo.setGeometry(QtCore.QRect(250, 270, 241, 31))
        self.txtTipo.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.txtTipo.setObjectName("txtTipo")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(150, 120, 221, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(260, 640, 101, 31))
        self.btnAceptar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 204, 102);")
        self.btnAceptar.setObjectName("btnAceptar")
        self.btnLimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpiar.setGeometry(QtCore.QRect(390, 640, 101, 31))
        self.btnLimpiar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 204, 102);")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.comboAsignatura = QtWidgets.QComboBox(self.centralwidget)
        self.comboAsignatura.setGeometry(QtCore.QRect(250, 480, 171, 31))
        self.comboAsignatura.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboAsignatura.setObjectName("comboAsignatura")
        self.btnAgregar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAgregar.setGeometry(QtCore.QRect(430, 480, 61, 31))
        self.btnAgregar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 204, 102);")
        self.btnAgregar.setObjectName("btnAgregar")
        self.btnRegresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(60, 640, 101, 31))
        self.btnRegresar.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 204, 102);")
        self.btnRegresar.setObjectName("btnRegresar")
        self.txtLimHoras = QtWidgets.QTextEdit(self.centralwidget)
        self.txtLimHoras.setGeometry(QtCore.QRect(250, 320, 241, 31))
        self.txtLimHoras.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.txtLimHoras.setObjectName("txtLimHoras")
        self.asignatura_2 = QtWidgets.QLabel(self.centralwidget)
        self.asignatura_2.setGeometry(QtCore.QRect(60, 320, 131, 31))
        self.asignatura_2.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_2.setObjectName("asignatura_2")
        self.asignatura_3 = QtWidgets.QLabel(self.centralwidget)
        self.asignatura_3.setGeometry(QtCore.QRect(60, 370, 131, 31))
        self.asignatura_3.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_3.setObjectName("asignatura_3")
        self.txtTelefono = QtWidgets.QTextEdit(self.centralwidget)
        self.txtTelefono.setGeometry(QtCore.QRect(250, 370, 241, 31))
        self.txtTelefono.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.txtTelefono.setObjectName("txtTelefono")
        self.asignatura_4 = QtWidgets.QLabel(self.centralwidget)
        self.asignatura_4.setGeometry(QtCore.QRect(60, 480, 131, 31))
        self.asignatura_4.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_4.setObjectName("asignatura_4")
        self.asignatura_5 = QtWidgets.QLabel(self.centralwidget)
        self.asignatura_5.setGeometry(QtCore.QRect(60, 420, 131, 31))
        self.asignatura_5.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_5.setObjectName("asignatura_5")
        self.comboEstado = QtWidgets.QComboBox(self.centralwidget)
        self.comboEstado.setGeometry(QtCore.QRect(250, 420, 241, 31))
        self.comboEstado.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboEstado.setCurrentText("")
        self.comboEstado.setObjectName("comboEstado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 538, 21))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Registro de Docentes</span></p></body></html>"))
        self.nombre.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Nombre:</span></p></body></html>"))
        self.identifi.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Identificacíon:</span></p></body></html>"))
        self.tipo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Tipo:</span></p></body></html>"))
        self.btnAceptar.setText(_translate("MainWindow", "ACEPTAR"))
        self.btnLimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.btnAgregar.setText(_translate("MainWindow", "+"))
        self.btnRegresar.setText(_translate("MainWindow", "REGRESAR"))
        self.asignatura_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Limite de horas:</span></p><p><br/></p></body></html>"))
        self.asignatura_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Telefono:</span></p></body></html>"))
        self.asignatura_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Asignatura:</span></p></body></html>"))
        self.asignatura_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Estado:</span></p><p><br/></p></body></html>"))

