# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\eliminarAsignatura.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from logica.Persistence import delete_Matter
class eliminarAsignatura(object):
    message_box: QMessageBox
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Eliminar Asignaturas")
        MainWindow.resize(536, 328)
        MainWindow.setStyleSheet("background-color: rgb(128, 195, 161)")
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
"background-color: rgb(0, 51, 51);")
        self.btnEliminar.setObjectName("btnEliminar")
        self.btnRegresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(10, 260, 101, 31))
        self.btnRegresar.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 51, 51);")
        self.btnRegresar.setObjectName("btnRegresar")
        self.btnLimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpiar.setGeometry(QtCore.QRect(290, 260, 91, 31))
        self.btnLimpiar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 51, 51);")
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
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def limpiar(self):
        self.txtCodtBuscar.clear()

    def eliminar(self):
        cod = self.txtCodtBuscar.toPlainText()
        res = delete_Matter(cod)
        if not None == res:
          self.mostrarMensaje("Información", "¡La asignatura se ha eliminado con exito!", "", QMessageBox.Warning, False)
        else:
            self.mostrarMensaje("Alerta", "¡Codigo no encontrado¡", "", QMessageBox.Warning,
                                False)

    def mostrarMensaje(self, titulo: str, texto: str, texto_informativo: str, tipo_mensaje: QMessageBox,
                           estado: bool):

            self.message_box = QMessageBox()
            self.message_box.setWindowTitle(titulo)
            self.message_box.setText(texto)

            if len(texto_informativo) > 0:
                self.message_box.setInformativeText(texto_informativo)

            if estado:
                btn_si = self.message_box.addButton('Si', QMessageBox.ActionRole)
                btn_no = self.message_box.addButton('No', QMessageBox.ActionRole)
                self.message_box.setDefaultButton(btn_si, btn_no)
            else:
                btn_aceptar = self.message_box.addButton('Aceptar', QMessageBox.ActionRole)
                self.message_box.setDefaultButton(btn_aceptar)
            if tipo_mensaje is not None:
                self.message_box.setIcon(tipo_mensaje)
                self.message_box.exec_()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Eliminar asignaturas"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#000000;\">Eliminar asignaturas</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.btnEliminar.setText(_translate("MainWindow", "ELIMINAR"))
        self.btnRegresar.setText(_translate("MainWindow", "REGRESAR"))
        self.btnLimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.codigo_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#000000;\">asignatura</span></p></body></html>"))
        self.codigo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#000000;\">Ingrese codigo de la</span></p></body></html>"))

