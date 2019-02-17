# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\ActualizarAsignaturas.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
from typing import Any

from PyQt5 import QtCore, QtGui, QtWidgets
from logica.Persistence import search_matter
from logica.Persistence import update_matter

from PyQt5.QtWidgets import QMessageBox


class ActualizarAsignatura(object):
    message_box: QMessageBox

    def setup_ui(self, main_window):
        main_window.setObjectName("Actualizar Asignaturas")
        main_window.resize(722, 647)
        main_window.setStyleSheet("background-color: rgb(128, 195, 161)")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 381, 61))
        self.label.setStyleSheet("\n"
                                 "font: 75 8pt \"Segoe Print\";")
        self.label.setObjectName("label")
        self.txtcodigobuscar = QtWidgets.QTextEdit(self.centralwidget)
        self.txtcodigobuscar.setGeometry(QtCore.QRect(30, 190, 191, 31))
        self.txtcodigobuscar.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "font: 10pt \"MS Shell Dlg 2\";\n"
                                           "background-color: rgb(255, 255, 255);")
        self.txtcodigobuscar.setObjectName("txtCodigoBuscar")
        self.codigo = QtWidgets.QLabel(self.centralwidget)
        self.codigo.setGeometry(QtCore.QRect(20, 150, 221, 31))
        self.codigo.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
                                  "color: rgb(0, 0, 0);")
        self.codigo.setObjectName("codigo")
        self.btnbuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnbuscar.setGeometry(QtCore.QRect(30, 250, 101, 31))
        self.btnbuscar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(0, 51, 51);")
        self.btnbuscar.setObjectName("btnBuscar")
        self.groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox.setGeometry(QtCore.QRect(260, 110, 441, 421))
        self.groupbox.setStyleSheet("font: 75 14pt \"Segoe Print\";\n"
                                    "color: rgb(0, 0, 0);")
        self.groupbox.setObjectName("groupBox")
        self.codigo_2 = QtWidgets.QLabel(self.groupbox)
        self.codigo_2.setGeometry(QtCore.QRect(10, 50, 91, 31))
        self.codigo_2.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.codigo_2.setObjectName("codigo_2")
        self.semestre = QtWidgets.QLabel(self.groupbox)
        self.semestre.setGeometry(QtCore.QRect(10, 290, 211, 31))
        self.semestre.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.semestre.setObjectName("semestre")
        self.boxsemestre = QtWidgets.QSpinBox(self.groupbox)
        self.boxsemestre.setGeometry(QtCore.QRect(220, 290, 71, 22))
        self.boxsemestre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.boxsemestre.setMinimum(1)
        self.boxsemestre.setMaximum(6)
        self.boxsemestre.setProperty("value", 1)
        self.boxsemestre.setObjectName("boxSemestre")
        self.numcreditos = QtWidgets.QLabel(self.groupbox)
        self.numcreditos.setGeometry(QtCore.QRect(10, 150, 171, 61))
        self.numcreditos.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.numcreditos.setObjectName("numCreditos")
        self.numhorassemestre = QtWidgets.QLabel(self.groupbox)
        self.numhorassemestre.setGeometry(QtCore.QRect(10, 200, 211, 61))
        self.numhorassemestre.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.numhorassemestre.setObjectName("numHorasSemestre")
        self.nombre = QtWidgets.QLabel(self.groupbox)
        self.nombre.setGeometry(QtCore.QRect(10, 100, 91, 21))
        self.nombre.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.nombre.setObjectName("nombre")
        self.txtnumhorsemestre = QtWidgets.QTextEdit(self.groupbox)
        self.txtnumhorsemestre.setGeometry(QtCore.QRect(220, 190, 201, 31))
        self.txtnumhorsemestre.setStyleSheet("color: rgb(0, 0, 0);\n"
                                             "font: 10pt \"MS Shell Dlg 2\";\n"
                                             "background-color: rgb(255, 255, 255);")
        self.txtnumhorsemestre.setObjectName("txtNumHorSemestre")
        self.boxcreditos = QtWidgets.QSpinBox(self.groupbox)
        self.boxcreditos.setGeometry(QtCore.QRect(220, 150, 71, 22))
        self.boxcreditos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.boxcreditos.setMinimum(1)
        self.boxcreditos.setMaximum(6)
        self.boxcreditos.setProperty("value", 1)
        self.boxcreditos.setObjectName("boxCreditos")
        self.txtcodigo = QtWidgets.QTextEdit(self.groupbox)
        self.txtcodigo.setGeometry(QtCore.QRect(220, 50, 201, 31))
        self.txtcodigo.setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "font: 10pt \"MS Shell Dlg 2\";\n"
                                     "background-color: rgb(255, 255, 255);")
        self.txtcodigo.setObjectName("txtCodigo")
        self.txtnombre = QtWidgets.QTextEdit(self.groupbox)
        self.txtnombre.setGeometry(QtCore.QRect(220, 100, 201, 31))
        self.txtnombre.setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "font: 10pt \"MS Shell Dlg 2\";\n"
                                     "background-color: rgb(255, 255, 255);")
        self.txtnombre.setObjectName("txtNombre")
        self.btnlimpiar = QtWidgets.QPushButton(self.groupbox)
        self.btnlimpiar.setGeometry(QtCore.QRect(340, 350, 81, 31))
        self.btnlimpiar.setStyleSheet("font: 75 11pt \"Segoe Print\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 55, 55);")
        self.btnlimpiar.setObjectName("btnLimpiar")
        self.btnactualizar = QtWidgets.QPushButton(self.groupbox)
        self.btnactualizar.setGeometry(QtCore.QRect(220, 350, 111, 31))
        self.btnactualizar.setStyleSheet("font: 75 11pt \"Segoe Print\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(0, 55, 55);")
        self.btnactualizar.setObjectName("btnActualizar")
        self.semestre_2 = QtWidgets.QLabel(self.groupbox)
        self.semestre_2.setGeometry(QtCore.QRect(10, 240, 131, 31))
        self.semestre_2.setStyleSheet("font: 10pt \"Segoe Print\";\n"
                                      "color: rgb(255, 255, 255);")
        self.semestre_2.setObjectName("semestre_2")
        self.txtcodrequis = QtWidgets.QTextEdit(self.groupbox)
        self.txtcodrequis.setGeometry(QtCore.QRect(220, 240, 201, 31))
        self.txtcodrequis.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "font: 10pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(255, 255, 255);")
        self.txtcodrequis.setObjectName("txtCodRequis")
        self.btnregresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnregresar.setGeometry(QtCore.QRect(40, 450, 101, 31))
        self.btnregresar.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(0, 55, 55);")
        self.btnregresar.setObjectName("btnRegresar")
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 21))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslate_ui(main_window)
        self.btnbuscar.clicked.connect(self.buscar)
        self.btnactualizar.clicked.connect(self.actualizar)
        self.btnlimpiar.clicked.connect(self.limpiar)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def limpiar(self):
        self.txtcodigo.clear()
        self.txtnombre.clear()
        self.boxsemestre.clear()
        self.boxcreditos.clear()
        self.txtcodrequis.clear()
        self.txtnumhorsemestre.clear()

    def buscar(self):
        codbuscar = str(self.txtcodigobuscar.toPlainText())
        res: Any = search_matter(codbuscar)
        if not None == res:
            print(res[1], res[2])
            self.txtcodigo.setText(str(res[1]))
            self.txtnombre.setText(str(res[2]))
            self.boxsemestre.setProperty("value", str(res[3]))
            self.boxcreditos.setProperty("value", str(res[4]))
            self.txtcodrequis.setText(str(res[5]))
            self.txtnumhorsemestre.setText(str(res[7]))
        else:
            self.mostrar_mensaje("Alerta", "¡El código ingresado no existe!", "", QMessageBox.Warning, False)
            print("no existe")

    def actualizar(self):
        try:
            cod = str(self.txtcodigo.toPlainText())
            nom = str(self.txtnombre.toPlainText())
            ubisemestre = int(self.boxsemestre.text())
            numcreditos = self.boxcreditos.text()
            codrequisito = self.txtcodrequis.toPlainText()
            numhourssem: str = self.txtnumhorsemestre.toPlainText()
            num: int = int(numhourssem)

            if len(cod) == 0 | len(nom) == 0 | len(ubisemestre) == 0 | len(numcreditos) == 0 | len(codrequisito) == 0 \
                    | len(numhourssem) == 0:
                self.mostrar_mensaje("Alerta", "¡Hay espacios vacios, digite todos los campos!", "", QMessageBox.Warning,
                                    False)
            else:
                update_matter(cod, nom, ubisemestre, numcreditos, codrequisito, num)
                QMessageBox.information(self, "Informacion", "¡Se han actualizado los datos correctamente!")

        except ValueError: \
                self.mostrar_mensaje("Alerta", "¡La entrada es incorrecta, escriba un numero entero!",
                                    "", QMessageBox.Warning, False)

    def mostrar_mensaje(self, titulo: str, texto: str, texto_informativo: str, tipo_mensaje: QMessageBox, estado: bool):
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
        main_window.setWindowTitle(_translate("MainWindow", "Actualizar asignaturas"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#000000;\">Actualizar  asignaturas</span></p><p align=\"center\"><br/></p></body></html>"))
        self.codigo.setText(_translate("MainWindow",
                                       "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Ingrese código de la asignatura:</p><p><br/></p></body></html>"))
        self.btnbuscar.setText(_translate("MainWindow", "BUSCAR"))
        self.groupbox.setTitle(_translate("MainWindow", "Actualizar datos"))
        self.codigo_2.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Codigo:</span></p><p><br/></p></body></html>"))
        self.semestre.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Semestre:</span></p><p><br/></p><p><br/></p></body></html>"))
        self.numcreditos.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Numero de creditos:</span></p><p><br/></p></body></html>"))
        self.numhorassemestre.setText(_translate("MainWindow",
                                                 "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Num. horas por semestre:</span></p><p><br/></p></body></html>"))
        self.nombre.setText(_translate("MainWindow",
                                       "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Nombre:</span></p></body></html>"))
        self.btnlimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.btnactualizar.setText(_translate("MainWindow", "ACTUALIZAR"))
        self.semestre_2.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Cod. Requisito:</span></p></body></html>"))
        self.btnregresar.setText(_translate("MainWindow", "REGRESAR"))
