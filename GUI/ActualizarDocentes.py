# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\ActualizarDocentes.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(687, 640)
        MainWindow.setStyleSheet("background-color: rgb(0, 51, 51)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(250, 90, 421, 501))
        self.groupBox.setStyleSheet("font: 75 14pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.tipo = QtWidgets.QLabel(self.groupBox)
        self.tipo.setGeometry(QtCore.QRect(10, 160, 71, 31))
        self.tipo.setStyleSheet("\n"
"font: 75 8pt \"Segoe Print\";")
        self.tipo.setObjectName("tipo")
        self.comboAsignatura = QtWidgets.QComboBox(self.groupBox)
        self.comboAsignatura.setGeometry(QtCore.QRect(180, 360, 171, 31))
        self.comboAsignatura.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboAsignatura.setObjectName("comboAsignatura")
        self.identifi = QtWidgets.QLabel(self.groupBox)
        self.identifi.setGeometry(QtCore.QRect(10, 110, 141, 31))
        self.identifi.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.identifi.setObjectName("identifi")
        self.asignatura_2 = QtWidgets.QLabel(self.groupBox)
        self.asignatura_2.setGeometry(QtCore.QRect(10, 210, 131, 31))
        self.asignatura_2.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_2.setObjectName("asignatura_2")
        self.nombre = QtWidgets.QLabel(self.groupBox)
        self.nombre.setGeometry(QtCore.QRect(10, 60, 91, 21))
        self.nombre.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.nombre.setObjectName("nombre")
        self.asignatura_4 = QtWidgets.QLabel(self.groupBox)
        self.asignatura_4.setGeometry(QtCore.QRect(10, 360, 131, 31))
        self.asignatura_4.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_4.setObjectName("asignatura_4")
        self.txtIdent = QtWidgets.QTextEdit(self.groupBox)
        self.txtIdent.setGeometry(QtCore.QRect(180, 110, 221, 31))
        self.txtIdent.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.txtIdent.setObjectName("txtIdent")
        self.asignatura_3 = QtWidgets.QLabel(self.groupBox)
        self.asignatura_3.setGeometry(QtCore.QRect(10, 260, 131, 31))
        self.asignatura_3.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_3.setObjectName("asignatura_3")
        self.txtTelefono = QtWidgets.QTextEdit(self.groupBox)
        self.txtTelefono.setGeometry(QtCore.QRect(180, 260, 221, 31))
        self.txtTelefono.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.txtTelefono.setObjectName("txtTelefono")
        self.btnAgregar = QtWidgets.QPushButton(self.groupBox)
        self.btnAgregar.setGeometry(QtCore.QRect(360, 360, 41, 31))
        self.btnAgregar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 204, 102);")
        self.btnAgregar.setObjectName("btnAgregar")
        self.txtNombre = QtWidgets.QTextEdit(self.groupBox)
        self.txtNombre.setGeometry(QtCore.QRect(180, 60, 221, 31))
        self.txtNombre.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.txtNombre.setObjectName("txtNombre")
        self.txtTipo = QtWidgets.QTextEdit(self.groupBox)
        self.txtTipo.setGeometry(QtCore.QRect(180, 160, 221, 31))
        self.txtTipo.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.txtTipo.setObjectName("txtTipo")
        self.txtLimHoras = QtWidgets.QTextEdit(self.groupBox)
        self.txtLimHoras.setGeometry(QtCore.QRect(180, 210, 221, 31))
        self.txtLimHoras.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.txtLimHoras.setObjectName("txtLimHoras")
        self.btnActualizar = QtWidgets.QPushButton(self.groupBox)
        self.btnActualizar.setGeometry(QtCore.QRect(180, 450, 111, 31))
        self.btnActualizar.setStyleSheet("font: 75 11pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 204, 102);")
        self.btnActualizar.setObjectName("btnActualizar")
        self.btnLimpiar = QtWidgets.QPushButton(self.groupBox)
        self.btnLimpiar.setGeometry(QtCore.QRect(300, 450, 101, 31))
        self.btnLimpiar.setStyleSheet("font: 75 11pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 204, 102);")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.comboEstado = QtWidgets.QComboBox(self.groupBox)
        self.comboEstado.setGeometry(QtCore.QRect(180, 310, 221, 31))
        self.comboEstado.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboEstado.setObjectName("comboEstado")
        self.asignatura_5 = QtWidgets.QLabel(self.groupBox)
        self.asignatura_5.setGeometry(QtCore.QRect(10, 310, 131, 31))
        self.asignatura_5.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_5.setObjectName("asignatura_5")
        self.codigo = QtWidgets.QLabel(self.centralwidget)
        self.codigo.setGeometry(QtCore.QRect(30, 120, 191, 31))
        self.codigo.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);")
        self.codigo.setObjectName("codigo")
        self.txtIdentBuscar = QtWidgets.QTextEdit(self.centralwidget)
        self.txtIdentBuscar.setGeometry(QtCore.QRect(30, 170, 191, 31))
        self.txtIdentBuscar.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.txtIdentBuscar.setObjectName("txtIdentBuscar")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(30, 230, 101, 31))
        self.btnBuscar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 204, 102);")
        self.btnBuscar.setObjectName("btnBuscar")
        self.btnRegresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(40, 540, 101, 31))
        self.btnRegresar.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 204, 102);")
        self.btnRegresar.setObjectName("btnRegresar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 381, 61))
        self.label.setStyleSheet("\n"
"font: 75 8pt \"Segoe Print\";")
        self.label.setObjectName("label")
        self.codigo_2 = QtWidgets.QLabel(self.centralwidget)
        self.codigo_2.setGeometry(QtCore.QRect(80, 140, 61, 21))
        self.codigo_2.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);")
        self.codigo_2.setObjectName("codigo_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 687, 21))
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
        self.groupBox.setTitle(_translate("MainWindow", "Actualizar datos"))
        self.tipo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Tipo:</span></p></body></html>"))
        self.identifi.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Identificacíon:</span></p></body></html>"))
        self.asignatura_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Limite de horas:</span></p><p><br/></p></body></html>"))
        self.nombre.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Nombre:</span></p></body></html>"))
        self.asignatura_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Asignatura:</span></p></body></html>"))
        self.asignatura_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Telefono:</span></p></body></html>"))
        self.btnAgregar.setText(_translate("MainWindow", "+"))
        self.btnActualizar.setText(_translate("MainWindow", "ACTUALIZAR"))
        self.btnLimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.asignatura_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Estado:</span></p></body></html>"))
        self.codigo.setText(_translate("MainWindow", "<html><head/><body><p>Ingrese identificación del</p><p/><p><br/></p></body></html>"))
        self.btnBuscar.setText(_translate("MainWindow", "BUSCAR"))
        self.btnRegresar.setText(_translate("MainWindow", "REGRESAR"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Actualizar docentes</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.codigo_2.setText(_translate("MainWindow", "<html><head/><body><p>docente</p><p><br/></p></body></html>"))

