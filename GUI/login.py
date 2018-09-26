# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.ventanaPrincipal import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from GUI.excpecion1 import LoginException
class Login(QMainWindow):
    message_box: QMessageBox
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(376, 373)
        Form.setStyleSheet("background-color: rgb(0, 51, 51)")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 30, 281, 61))
        self.label.setStyleSheet("\n"
"font: 75 8pt \"Segoe Print\";")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(60, 120, 261, 221))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.txtUsuario = QtWidgets.QTextEdit(self.frame)
        self.txtUsuario.setGeometry(QtCore.QRect(30, 30, 211, 31))
        self.txtUsuario.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 51, 51)\n"
"")
        self.txtUsuario.setObjectName("nomUsuario")
        self.txtContrasena = QtWidgets.QTextEdit(self.frame)
        self.txtContrasena.setGeometry(QtCore.QRect(30, 90, 211, 31))
        self.txtContrasena.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 51, 51)\n"
"")
        self.txtContrasena.setObjectName("Contraseña")
        self.btnAgregar = QtWidgets.QPushButton(self.frame)
        self.btnAgregar.setGeometry(QtCore.QRect(30, 160, 211, 41))
        self.btnAgregar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 204, 102);")
        self.btnAgregar.setObjectName("btnAgregar")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 141, 16))
        self.label_2.setStyleSheet("font: 75 10pt \"Segoe Print\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 91, 16))
        self.label_3.setStyleSheet("font: 75 10pt \"Segoe Print\";")
        self.label_3.setObjectName("label_3")
        self.btnAgregar.clicked.connect(self.ingresar)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def ingresar(self):
        usuario = self.txtUsuario.toPlainText()
        contra = self.txtContrasena.toPlainText()
        if len(usuario) == 0 | len(contra) == 0:
            self.mostrarMensaje("Alerta", "Ingrese usuario y/o contraseña", "", QMessageBox.Warning, False)
        else:
         if usuario == 'alex' and contra == '123':
            print('alex')
            self.ventana = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.ventana)
            self.hide()
            self.close()
            self.ventana.show()
            self.hide()

         else:
            print("marica")
            self.mostrarMensaje("Alerta", "El usuario o la contraseña son incorrectos", "", QMessageBox.Warning, False)

    def mostrarMensaje(self, titulo: str, texto: str, texto_informativo: str, tipo_mensaje: QMessageBox, estado: bool):

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

    def retranslateUi(self, Form):

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Log-in</span></p></body></html>"))
        self.btnAgregar.setText(_translate("Form", "Iniciar Sesion"))
        self.label_2.setText(_translate("Form", "Nombre de usuario "))
        self.label_3.setText(_translate("Form", "Contraseña"))

