# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\eliminarDocente.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from logica.Persistence import delete_docent
from PyQt5.QtWidgets import QMessageBox, QMainWindow


class EliminarDocente(QMainWindow):
    message_box = QMessageBox

    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(534, 321)
        main_window.setStyleSheet("background-color: rgb(128, 195, 161)")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 30, 381, 61))
        self.label.setStyleSheet("\n"
                                 "font: 75 8pt \"Segoe Print\";")
        self.label.setObjectName("label")
        self.txtidentbuscar = QtWidgets.QTextEdit(self.centralwidget)
        self.txtidentbuscar.setGeometry(QtCore.QRect(190, 180, 201, 31))
        self.txtidentbuscar.setStyleSheet("color: rgb(0, 0, 0);\n"
                                          "font: 10pt \"MS Shell Dlg 2\";\n"
                                          "background-color: rgb(255, 255, 255);")
        self.txtidentbuscar.setObjectName("txtIdentBuscar")
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
        self.btneliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btneliminar.setGeometry(QtCore.QRect(190, 250, 91, 31))
        self.btneliminar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(0, 51, 51);")
        self.btneliminar.setObjectName("btnEliminar")
        self.btnlimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnlimpiar.setGeometry(QtCore.QRect(300, 250, 91, 31))
        self.btnlimpiar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 51, 51);")
        self.btnlimpiar.setObjectName("btnLimpiar")
        self.btnregresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnregresar.setGeometry(QtCore.QRect(20, 250, 101, 31))
        self.btnregresar.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(0, 51, 51);")
        self.btnregresar.setObjectName("btnRegresar")
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 21))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        print("entrooo acá 2")
        self.retranslate_ui(main_window)
        self.btneliminar.clicked.connect(self.eliminar)
        self.btnlimpiar.clicked.connect(self.limpiar)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def eliminar(self):
        buton = QMessageBox.question(self, 'Advertencia', "¿Esta seguro de eliminar este docente?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        print("entrooo acá2")
        if buton == QMessageBox.Yes:
            iden = str(self.txtidentbuscar.toPlainText())
            res = delete_docent(iden)

            if None != res:
                QMessageBox.information(self, "Informacion", "¡El docente se ha eliminado con exito!")
            else:
                self.mostrar_mensaje("Alerta", "¡Identificación no encontrada!", "", QMessageBox.Warning, False)

    def limpiar(self):
        self.txtidentbuscar.clear()

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
        main_window.setWindowTitle(_translate("MainWindow", "Eliminar docente"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#000000;\">Eliminar docentes</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.codigo.setText(_translate("MainWindow",
                                       "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#000000;\">Ingrese identificación del</span></p></body></html>"))
        self.codigo_2.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#000000;\">docente</span></p></body></html>"))
        self.btneliminar.setText(_translate("MainWindow", "ELIMINAR"))
        self.btnlimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.btnregresar.setText(_translate("MainWindow", "REGRESAR"))
