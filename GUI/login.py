# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from GUI.ventanaPrincipal import VentanaPrincipal
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication


class Login(QMainWindow):
    message_box: QMessageBox

    def setup_ui(self, form):
        form.setObjectName("Form")
        form.resize(376, 373)
        form.setStyleSheet("background-color: rgb(128, 195, 161)")
        self.label = QtWidgets.QLabel(form)
        self.label.setGeometry(QtCore.QRect(40, 30, 281, 61))
        self.label.setStyleSheet("\n"
                                 "font: 75 8pt \"Segoe Print\";")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(form)
        self.frame.setGeometry(QtCore.QRect(60, 120, 261, 221))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.txtusuario = QtWidgets.QTextEdit(self.frame)
        self.txtusuario.setGeometry(QtCore.QRect(30, 30, 211, 31))
        self.txtusuario.setStyleSheet("color: rgb(0, 0, 0);\n"
                                      "background-color: rgb(128, 195, 161)\n"
                                      "")
        self.txtusuario.setObjectName("nomUsuario")
        self.txtusuario.setToolTip('Ingrese nombre de usuario')
        self.txtusuario.setPlaceholderText('Ingrese nombre de usuario')
        self.txtcontrasena = QtWidgets.QLineEdit(self.frame)
        self.txtcontrasena.setGeometry(QtCore.QRect(30, 90, 211, 31))
        self.txtcontrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtcontrasena.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(128, 195, 161)\n"
                                         "")
        self.txtcontrasena.setObjectName("Contraseña")
        self.txtcontrasena.setToolTip('Ingrese su contraseña')
        self.txtcontrasena.setPlaceholderText('Ingrese contraseña')
        self.btnagregar = QtWidgets.QPushButton(self.frame)
        self.btnagregar.setGeometry(QtCore.QRect(30, 160, 211, 41))
        self.btnagregar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 51, 51);")
        self.btnagregar.setObjectName("btnAgregar")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 141, 21))
        self.label_2.setStyleSheet("font: 75 10pt \"Segoe Print\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 66, 91, 20))
        self.label_3.setStyleSheet("font: 75 10pt \"Segoe Print\";")
        self.label_3.setObjectName("label_3")
        self.retranslate_ui(form)
        self.btnagregar.clicked.connect(self.ingresar)

        QtCore.QMetaObject.connectSlotsByName(form)

    def ingresar(self):
        usuario = self.txtusuario.toPlainText()
        contra = self.txtcontrasena.text()
        QMessageBox.Ok
        if len(usuario) == 0 | len(contra) == 0:
            self.mostrar_mensaje("Alerta", "Ingrese usuario y/o contraseña", "", QMessageBox.Warning, False)
        else:
            if usuario == 'admin' and contra == '12345':
                self.ventana = QtWidgets.QMainWindow()
                self.ui = VentanaPrincipal()
                self.ui.setup_ui(self.ventana)
                self.ventana.show()
            else:
                self.mostrar_mensaje("Alerta", "El usuario o la contraseña son incorrectos", "", QMessageBox.Warning,
                                    False)

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

    def retranslate_ui(self, form):

        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Login"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#000000;\">Log-in</span></p></body></html>"))
        self.btnagregar.setText(_translate("Form", "Iniciar Sesion"))
        self.label_2.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-weight:600;\">Nombre de usuario </span></p></body></html>"))
        self.label_3.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-weight:600;\">Contraseña</span></p></body></html>"))
