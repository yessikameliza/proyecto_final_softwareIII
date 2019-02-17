# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\registroAsignaturas.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
from xml.dom import ValidationErr

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from logica.Persistence import register_matter


class RegistroAsignaturas(object):
    message_box: QMessageBox

    def setup_ui(self, main_window):
        main_window.setObjectName("Registro de asignaturas")
        main_window.resize(531, 573)
        main_window.setStyleSheet("background-color: rgb(128, 195, 161)")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 381, 61))
        self.label.setStyleSheet("\n"
                                 "font: 75 8pt \"Segoe Print\";")
        self.label.setObjectName("label")
        self.txtcodigo = QtWidgets.QTextEdit(self.centralwidget)
        self.txtcodigo.setGeometry(QtCore.QRect(260, 140, 221, 31))
        self.txtcodigo.setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "font: 10pt \"MS Shell Dlg 2\";\n"
                                     "background-color: rgb(255, 255, 255);")
        self.txtcodigo.setObjectName("txtcodigo")
        self.nombre = QtWidgets.QLabel(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(40, 190, 91, 21))
        self.nombre.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.nombre.setObjectName("nombre")
        self.codigo = QtWidgets.QLabel(self.centralwidget)
        self.codigo.setGeometry(QtCore.QRect(40, 140, 91, 31))
        self.codigo.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.codigo.setObjectName("codigo")
        self.txtnombre = QtWidgets.QTextEdit(self.centralwidget)
        self.txtnombre.setGeometry(QtCore.QRect(260, 190, 221, 31))
        self.txtnombre.setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "font: 10pt \"MS Shell Dlg 2\";\n"
                                     "background-color: rgb(255, 255, 255);")
        self.txtnombre.setObjectName("txtnombre")
        self.numcreditos = QtWidgets.QLabel(self.centralwidget)
        self.numcreditos.setGeometry(QtCore.QRect(40, 250, 171, 61))
        self.numcreditos.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.numcreditos.setObjectName("numcreditos")
        self.txtnumhorsemestre = QtWidgets.QTextEdit(self.centralwidget)
        self.txtnumhorsemestre.setGeometry(QtCore.QRect(260, 290, 221, 31))
        self.txtnumhorsemestre.setStyleSheet("color: rgb(0, 0, 0);\n"
                                             "font: 10pt \"MS Shell Dlg 2\";\n"
                                             "background-color: rgb(255, 255, 255);")
        self.txtnumhorsemestre.setObjectName("txtNumHorSemestre")
        self.numhorassemestre = QtWidgets.QLabel(self.centralwidget)
        self.numhorassemestre.setGeometry(QtCore.QRect(40, 300, 211, 41))
        self.numhorassemestre.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.numhorassemestre.setObjectName("numhorassemestre")
        self.btnaceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnaceptar.setGeometry(QtCore.QRect(260, 480, 101, 31))
        self.btnaceptar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 51, 51);")
        self.btnaceptar.setObjectName("btnAceptar")
        self.btnlimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnlimpiar.setGeometry(QtCore.QRect(370, 480, 111, 31))
        self.btnlimpiar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 51, 51);")
        self.btnlimpiar.setObjectName("btnLimpiar")
        self.btnregresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnregresar.setGeometry(QtCore.QRect(40, 480, 101, 31))
        self.btnregresar.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(0, 51, 51);")
        self.btnregresar.setObjectName("btnRegresar")
        self.semestre = QtWidgets.QLabel(self.centralwidget)
        self.semestre.setGeometry(QtCore.QRect(40, 410, 211, 31))
        self.semestre.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.semestre.setObjectName("semestre")
        self.boxsemestre = QtWidgets.QSpinBox(self.centralwidget)
        self.boxsemestre.setGeometry(QtCore.QRect(260, 410, 71, 22))
        self.boxsemestre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.boxsemestre.setMinimum(1)
        self.boxsemestre.setMaximum(6)
        self.boxsemestre.setProperty("value", 1)
        self.boxsemestre.setObjectName("boxsemestre")
        self.boxcreditos = QtWidgets.QSpinBox(self.centralwidget)
        self.boxcreditos.setGeometry(QtCore.QRect(260, 250, 71, 22))
        self.boxcreditos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.boxcreditos.setMinimum(1)
        self.boxcreditos.setMaximum(6)
        self.boxcreditos.setProperty("value", 1)
        self.boxcreditos.setObjectName("boxcreditos")
        self.semestre_2 = QtWidgets.QLabel(self.centralwidget)
        self.semestre_2.setGeometry(QtCore.QRect(40, 350, 211, 31))
        self.semestre_2.setStyleSheet("font: 10pt \"Segoe Print\";\n"
                                      "color: rgb(255, 255, 255);")
        self.semestre_2.setObjectName("semestre_2")
        self.txtcodreq = QtWidgets.QTextEdit(self.centralwidget)
        self.txtcodreq.setGeometry(QtCore.QRect(260, 350, 221, 31))
        self.txtcodreq.setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "font: 10pt \"MS Shell Dlg 2\";\n"
                                     "background-color: rgb(255, 255, 255);")
        self.txtcodreq.setObjectName("txtCodReq")
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 21))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.btnaceptar.clicked.connect(self.registrar_materias)
        self.btnlimpiar.clicked.connect(self.limpiar)

        self.retranslate_ui(main_window)

        QtCore.QMetaObject.connectSlotsByName(main_window)

    def limpiar(self):
        self.txtnombre.clear()
        self.txtcodreq.clear()
        self.txtnumhorsemestre.clear()
        self.txtcodigo.clear()
        self.boxsemestre.clear()
        self.boxcreditos.clear()

    def registrar_materias(self):
        try:
            cod = str(self.txtcodigo.toPlainText())
            nombre = str(self.txtnombre.toPlainText())
            numcred = str(self.boxcreditos.text())
            numhorsem = self.txtnumhorsemestre.toPlainText()
            codreq = str(self.txtcodreq.toPlainText())
            sem = self.boxsemestre.text()
            semes = int(sem)
            numhoras = int(numhorsem)
            if len(cod) == 0 | len(nombre) == 0 | len(numcred) == 0 | len(numhoras) == 0 | len(codreq) == 0 | len(
                    sem) == 0:
                self.mostrar_mensaje("Alerta", "¡Hay campos vacios!", "", QMessageBox.Warning, False)
            else:
                register_matter(cod, nombre, semes, numcred, codreq, numhoras)
                QMessageBox.information(self, "Informacion", "¡Datos registrados con exito!")

        except ValueError:
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
        main_window.setWindowTitle(_translate("MainWindow", "Registro asignaturas"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#000000;\">Registro de asignaturas</span></p><p align=\"center\"><br/></p></body></html>"))
        self.nombre.setText(_translate("MainWindow",
                                       "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Nombre:</span></p></body></html>"))
        self.codigo.setText(_translate("MainWindow",
                                       "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Codigo:</span></p><p><br/></p></body></html>"))
        self.numcreditos.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Numero de creditos:</span></p><p><br/></p></body></html>"))
        self.numhorassemestre.setText(_translate("MainWindow",
                                                 "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Num. horas por semestre:</span></p><p><br/></p></body></html>"))
        self.btnaceptar.setText(_translate("MainWindow", "ACEPTAR"))
        self.btnlimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.btnregresar.setText(_translate("MainWindow", "REGRESAR"))
        self.semestre.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Semestre:</span></p><p><br/></p><p><br/></p></body></html>"))
        self.semestre_2.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#000000; \">Cod. Requisito:</span></p></body></html>"))
