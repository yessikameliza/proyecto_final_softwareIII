# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\eliminarAsignatura.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from logica.Persistence import delete_matter


class EliminarAsignatura(object):
    message_box: QMessageBox

    def setup_ui(self, main_window):
        main_window.setObjectName("Eliminar Asignaturas")
        main_window.resize(536, 328)
        main_window.setStyleSheet("background-color: rgb(128, 195, 161)")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.txtcodtbuscar = QtWidgets.QTextEdit(self.centralwidget)
        self.txtcodtbuscar.setGeometry(QtCore.QRect(180, 180, 201, 31))
        self.txtcodtbuscar.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "font: 10pt \"MS Shell Dlg 2\";\n"
                                         "background-color: rgb(255, 255, 255);")
        self.txtcodtbuscar.setObjectName("txtCodtBuscar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 30, 381, 61))
        self.label.setStyleSheet("\n"
                                 "font: 75 8pt \"Segoe Print\";")
        self.label.setObjectName("label")
        self.btneliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btneliminar.setGeometry(QtCore.QRect(180, 260, 91, 31))
        self.btneliminar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(0, 51, 51);")
        self.btneliminar.setObjectName("btnEliminar")
        self.btnregresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnregresar.setGeometry(QtCore.QRect(10, 260, 101, 31))
        self.btnregresar.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(0, 51, 51);")
        self.btnregresar.setObjectName("btnRegresar")
        self.btnlimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnlimpiar.setGeometry(QtCore.QRect(290, 260, 91, 31))
        self.btnlimpiar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 51, 51);")
        self.btnlimpiar.setObjectName("btnLimpiar")
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
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 536, 21))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.btneliminar.clicked.connect(self.eliminar)
        self.btnlimpiar.clicked.connect(self.limpiar)
        self.retranslate_ui(main_window)

        QtCore.QMetaObject.connectSlotsByName(main_window)

    def limpiar(self):
        self.txtcodtbuscar.clear()

    def eliminar(self):
        try:
            cod = self.txtcodtbuscar.toPlainText()
            res = delete_matter(cod)

            if not None == res:
                self.mostrar_mensaje("Información", "¡La asignatura se ha eliminado con exito!", "", QMessageBox.Warning,
                                    False)
            else:
                self.mostrar_mensaje("Alerta", "¡Codigo no encontrado¡", "", QMessageBox.Warning,
                                    False)
        except ValueError:
            self.mostrar_mensaje("Información", "¡La entrada es incorrecta, verifique lo ingresado!",
                                "", QMessageBox.Warning, False)

    def mostrar_mensaje(self, titulo: str, texto: str, texto_informativo: str, tipo_mensaje: QMessageBox,
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

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "Eliminar asignaturas"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#000000;\">Eliminar asignaturas</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.btneliminar.setText(_translate("MainWindow", "ELIMINAR"))
        self.btnregresar.setText(_translate("MainWindow", "REGRESAR"))
        self.btnlimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.codigo_2.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#000000;\">asignatura</span></p></body></html>"))
        self.codigo.setText(_translate("MainWindow",
                                       "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#000000;\">Ingrese codigo de la</span></p></body></html>"))
