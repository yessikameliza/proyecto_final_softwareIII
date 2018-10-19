# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\eliminarDocente.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from logica.Persistence import delete_Docent
from PyQt5.QtWidgets import QMessageBox


class eliminarDocente(object):
    message_box = QMessageBox

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(534, 321)
        MainWindow.setStyleSheet("background-color: rgb(128, 195, 161)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 30, 381, 61))
        self.label.setStyleSheet("\n"
                                 "font: 75 8pt \"Segoe Print\";")
        self.label.setObjectName("label")
        self.txtIdentBuscar = QtWidgets.QTextEdit(self.centralwidget)
        self.txtIdentBuscar.setGeometry(QtCore.QRect(190, 180, 201, 31))
        self.txtIdentBuscar.setStyleSheet("color: rgb(0, 0, 0);\n"
                                          "font: 10pt \"MS Shell Dlg 2\";\n"
                                          "background-color: rgb(255, 255, 255);")
        self.txtIdentBuscar.setObjectName("txtIdentBuscar")
        self.codigo = QtWidgets.QLabel(self.centralwidget)
        self.codigo.setGeometry(QtCore.QRect(200, 120, 191, 31))
        self.codigo.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
                                  "color: rgb(255, 255, 255);")
        self.codigo.setObjectName("codigo")
        self.codigo_2 = QtWidgets.QLabel(self.centralwidget)
        self.codigo_2.setGeometry(QtCore.QRect(260, 140, 61, 21))
        self.codigo_2.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
                                    "color: rgb(255, 255, 255);")
        self.codigo_2.setObjectName("codigo_2")
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setGeometry(QtCore.QRect(190, 250, 91, 31))
        self.btnEliminar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(0, 51, 51);")
        self.btnEliminar.setObjectName("btnEliminar")
        self.btnLimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpiar.setGeometry(QtCore.QRect(300, 250, 91, 31))
        self.btnLimpiar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 51, 51);")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.btnRegresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 250, 101, 31))
        self.btnRegresar.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(0, 51, 51);")
        self.btnRegresar.setObjectName("btnRegresar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def eliminar(self):
        iden = str(self.txtIdentBuscar.toPlainText())
        res = delete_Docent(iden)
        if not None == res:
            self.mostrarMensaje("Información", "¡El docente se ha eliminado con exito!", "", QMessageBox.Warning,
                                False)
        else:
            self.mostrarMensaje("Alerta", "¡Identificación no encontrada!", "", QMessageBox.Warning,
                                False)

    def limpiar(self):
        self.txtIdentBuscar.clear()

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Eliminar docente"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#000000;\">Eliminar docentes</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.codigo.setText(_translate("MainWindow",
                                       "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#000000;\">Ingrese identificación del</span></p></body></html>"))
        self.codigo_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#000000;\">docente</span></p></body></html>"))
        self.btnEliminar.setText(_translate("MainWindow", "ELIMINAR"))
        self.btnLimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.btnRegresar.setText(_translate("MainWindow", "REGRESAR"))
