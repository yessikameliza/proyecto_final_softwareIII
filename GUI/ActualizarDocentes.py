# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\ActualizarDocentes.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
from typing import Any

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from logica.Persistence import search_docent
from logica.Persistence import update_docent
from logica.Persistence import obtener_matter


class ActualizarDocente(QMainWindow):
    message_box: QMessageBox


    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(687, 640)
        main_window.setStyleSheet("background-color: rgb(128, 195, 161)")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox.setGeometry(QtCore.QRect(250, 90, 421, 501))
        self.groupbox.setStyleSheet("font: 75 14pt \"Segoe Print\";\n"
                                    "color: rgb(0, 0, 0);")
        self.groupbox.setObjectName("groupBox")
        self.tipo = QtWidgets.QLabel(self.groupbox)
        self.tipo.setGeometry(QtCore.QRect(10, 160, 71, 31))
        self.tipo.setStyleSheet("\n"
                                "font: 75 8pt \"Segoe Print\";")
        self.tipo.setObjectName("tipo")
        self.comboasignatura = QtWidgets.QComboBox(self.groupbox)
        self.comboasignatura.setGeometry(QtCore.QRect(180, 360, 221, 31))
        self.comboasignatura.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(0, 0, 0);")
        res = obtener_matter()
        self.comboasignatura.addItem('')
        for aux in res:
            aux2 = str((aux[2]))
            print(aux2)

            self.comboasignatura.addItem(aux2)

        self.comboasignatura.setObjectName("comboAsignatura")

        self.identifi = QtWidgets.QLabel(self.groupbox)
        self.identifi.setGeometry(QtCore.QRect(10, 110, 141, 31))
        self.identifi.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.identifi.setObjectName("identifi")
        self.asignatura_2 = QtWidgets.QLabel(self.groupbox)
        self.asignatura_2.setGeometry(QtCore.QRect(10, 210, 131, 31))
        self.asignatura_2.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_2.setObjectName("asignatura_2")
        self.nombre = QtWidgets.QLabel(self.groupbox)
        self.nombre.setGeometry(QtCore.QRect(10, 60, 91, 21))
        self.nombre.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.nombre.setObjectName("nombre")
        self.asignatura_4 = QtWidgets.QLabel(self.groupbox)
        self.asignatura_4.setGeometry(QtCore.QRect(10, 360, 131, 31))
        self.asignatura_4.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_4.setObjectName("asignatura_4")

        self.txtident = QtWidgets.QTextEdit(self.groupbox)
        self.txtident.setGeometry(QtCore.QRect(180, 110, 221, 31))
        self.txtident.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "font: 10pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(255, 255, 255);")
        self.txtident.setObjectName("txtIdent")
        self.asignatura_3 = QtWidgets.QLabel(self.groupbox)
        self.asignatura_3.setGeometry(QtCore.QRect(10, 260, 131, 31))
        self.asignatura_3.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_3.setObjectName("asignatura_3")
        self.txttelefono = QtWidgets.QTextEdit(self.groupbox)
        self.txttelefono.setGeometry(QtCore.QRect(180, 260, 221, 31))
        self.txttelefono.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       "font: 10pt \"MS Shell Dlg 2\";\n"
                                       "background-color: rgb(255, 255, 255);")
        self.txttelefono.setObjectName("txtTelefono")

        self.txtnombre = QtWidgets.QTextEdit(self.groupbox)
        self.txtnombre.setGeometry(QtCore.QRect(180, 60, 221, 31))
        self.txtnombre.setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "font: 10pt \"MS Shell Dlg 2\";\n"
                                     "background-color: rgb(255, 255, 255);")
        self.txtnombre.setObjectName("txtNombre")
        self.txttipo = QtWidgets.QTextEdit(self.groupbox)
        self.txttipo.setGeometry(QtCore.QRect(180, 160, 221, 31))
        self.txttipo.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 10pt \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(255, 255, 255);")
        self.txttipo.setObjectName("txtTipo")
        self.txtlimhoras = QtWidgets.QTextEdit(self.groupbox)
        self.txtlimhoras.setGeometry(QtCore.QRect(180, 210, 221, 31))
        self.txtlimhoras.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       "font: 10pt \"MS Shell Dlg 2\";\n"
                                       "background-color: rgb(255, 255, 255);")
        self.txtlimhoras.setObjectName("txtLimHoras")
        self.btnactualizar = QtWidgets.QPushButton(self.groupbox)
        self.btnactualizar.setGeometry(QtCore.QRect(180, 450, 111, 31))
        self.btnactualizar.setStyleSheet("font: 75 11pt \"Segoe Print\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(0, 51, 51);")
        self.btnactualizar.setObjectName("btnActualizar")
        self.btnlimpiar = QtWidgets.QPushButton(self.groupbox)
        self.btnlimpiar.setGeometry(QtCore.QRect(300, 450, 101, 31))
        self.btnlimpiar.setStyleSheet("font: 75 11pt \"Segoe Print\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 51, 51);")
        self.btnlimpiar.setObjectName("btnLimpiar")
        self.comboestado = QtWidgets.QComboBox(self.groupbox)
        self.comboestado.setGeometry(QtCore.QRect(180, 310, 221, 31))
        self.comboestado.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.comboestado.setObjectName("comboEstado")
        self.comboestado.setCurrentText("")
        items = ('','ACTIVO', 'INACTIVO')
        self.comboestado.addItems(items)

        self.combociudad = QtWidgets.QComboBox(self.groupbox)
        self.combociudad.setGeometry(QtCore.QRect(180, 410, 221, 31))
        self.combociudad.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.combociudad.setObjectName("comboCiudad")
        itemsa = ('', 'Armenia', 'Pereira', 'Buga')
        self.combociudad.addItems(itemsa)

        self.asignatura_5 = QtWidgets.QLabel(self.groupbox)
        self.asignatura_5.setGeometry(QtCore.QRect(10, 310, 131, 31))
        self.asignatura_5.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_5.setObjectName("asignatura_5")

        self.ciudad = QtWidgets.QLabel(self.groupbox)
        self.ciudad.setGeometry(QtCore.QRect(10, 410, 141, 31))
        self.ciudad.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.ciudad.setObjectName("ciudad")



        self.codigo = QtWidgets.QLabel(self.centralwidget)
        self.codigo.setGeometry(QtCore.QRect(30, 120, 191, 31))
        self.codigo.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
                                  "color: rgb(255, 255, 255);")
        self.codigo.setObjectName("codigo")
        self.txtidentbuscar = QtWidgets.QTextEdit(self.centralwidget)
        self.txtidentbuscar.setGeometry(QtCore.QRect(30, 170, 191, 31))
        self.txtidentbuscar.setStyleSheet("color: rgb(0, 0, 0);\n"
                                          "font: 10pt \"MS Shell Dlg 2\";\n"
                                          "background-color: rgb(255, 255, 255);")
        self.txtidentbuscar.setObjectName("txtIdentBuscar")
        self.btnbuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnbuscar.setGeometry(QtCore.QRect(30, 230, 101, 31))
        self.btnbuscar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(0, 51, 51);")
        self.btnbuscar.setObjectName("btnBuscar")

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
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 687, 21))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.retranslate_ui(main_window)
        print("paso esto 3")

        self.btnbuscar.clicked.connect(self.buscar)
        self.btnactualizar.clicked.connect(self.actualiza)
        self.btnlimpiar.clicked.connect(self.limpiar)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def limpiar(self):
        self.txtnombre.clear()
        self.txttipo.clear()
        self.txtlimhoras.clear()
        self.txttelefono.clear()
        self.txtident.clear()
        self.comboestado.clear()
        self.combociudad.clear()
        self.comboasignatura.clear()
        items = ('', 'ACTIVO', 'INACTIVO')
        self.comboestado.addItems(items)
        itemsa = ('', 'Armenia', 'Pereira', 'Buga')
        self.combociudad.addItems(itemsa)
        res = obtener_matter()
        self.comboasignatura.addItem('')
        for aux in res:
            aux2 = str((aux[2]))
            print(aux2)

            self.comboasignatura.addItem(aux2)


    def actualiza(self):
        try:
            nomb = str(self.txtnombre.toPlainText())
            tipo = str(self.txttipo.toPlainText())
            lim = int(self.txtlimhoras.toPlainText())
            tel = str(self.txttelefono.toPlainText())
            iden = str(self.txtident.toPlainText())
            esta = str(self.comboestado.currentText())
            materia = str(self.comboasignatura.currentText())
            ciudad = str(self.combociudad.currentText())

            if len(nomb) == 0 | len(tipo) == 0 | len(lim) == 0 | len(tel) == 0 | len(iden) == 0 | len(esta) == 0:
                self.mostrar_mensaje("Alerta", "¡Hay espacios vacios, digite todos los campos!", "", QMessageBox.Warning,
                                    False)
            else:
                update_docent(nomb, esta, lim, tipo, tel, iden, materia, ciudad)
                QMessageBox.information(self, "Informacion", "¡Se han actualizado los datos correctamente!")
                self.limpiar()
        except ValueError:
            self.mostrar_mensaje("Alerta", "¡La entrada es incorrecta, escriba un numero entero!",
                                "", QMessageBox.Warning, False)

    def buscar(self):
        id = self.txtidentbuscar.toPlainText()
        fila: Any = search_docent(id)
        if not None == fila:
            self.txtident.setText(str(fila[6]))
            self.txtnombre.setText(str(fila[1]))
            self.txtlimhoras.setText(str(fila[3]))
            self.txttipo.setText(str(fila[4]))
            self.txttelefono.setText(str(fila[5]))
            self.comboasignatura.setItemText(0, str(fila[7]))

            if str(fila[2]) == "ACTIVO":
                self.comboestado.setItemText(0, str(fila[2]))
                self.comboestado.setItemText(1, 'INACTIVO')
                self.comboestado.setItemText(2, '')
            else:
                self.comboestado.setItemText(0, str(fila[2]))
                self.comboestado.setItemText(1, 'ACTIVO')
                self.comboestado.setItemText(2, '')

            if str(fila[8]) == "Armenia":
                self.combociudad.setItemText(0, str(fila[8]))
                self.combociudad.setItemText(1, 'Pereira')
                self.combociudad.setItemText(2, 'Buga')
                self.combociudad.setItemText(3, '')
            else:
                if str(fila[8]) == "Pereira":
                    self.combociudad.setItemText(0, str(fila[8]))
                    self.combociudad.setItemText(1, 'Armenia')
                    self.combociudad.setItemText(2, 'Buga')
                    self.combociudad.setItemText(3, '')
                else:
                    self.combociudad.setItemText(0, str(fila[8]))
                    self.combociudad.setItemText(1, 'Armenia')
                    self.combociudad.setItemText(2, 'Pereira')
                    self.combociudad.setItemText(3, '')
        else:
            print("no existe el docente")
            self.mostrar_mensaje("Alerta", "¡La identificación ingresada no existe!", "", QMessageBox.Warning, False)


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
        main_window.setWindowTitle(_translate("MainWindow", "Actualizar docentes"))
        self.groupbox.setTitle(_translate("MainWindow", "Actualizar datos"))
        self.tipo.setText(_translate("MainWindow",
                                     "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Tipo:</span></p></body></html>"))
        self.identifi.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;pt; color:#000000;\">Identificacíon:</span></p></body></html>"))
        self.asignatura_2.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Limite de horas:</span></p><p><br/></p></body></html>"))
        self.nombre.setText(_translate("MainWindow",
                                       "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Nombre:</span></p></body></html>"))
        self.asignatura_4.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Asignatura:</span></p></body></html>"))
        self.asignatura_3.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Telefono:</span></p></body></html>"))

        self.btnactualizar.setText(_translate("MainWindow", "ACTUALIZAR"))
        self.btnlimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.asignatura_5.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Estado:</span></p></body></html>"))
        self.codigo.setText(_translate("MainWindow",
                                       "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#000000;\">Ingrese identificación del</span></p></body></html>"))
        self.btnbuscar.setText(_translate("MainWindow", "BUSCAR"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#000000;\">Actualizar docentes</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
        self.codigo_2.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#000000;\">docente</span></p></body></html>"))
        self.ciudad.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Ciudad:</span></p></body></html>"))
