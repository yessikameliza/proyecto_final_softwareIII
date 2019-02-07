# coding: utf-8

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\registroDocentes.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from logica.Persistence import register_docent
from logica.Persistence import obtener_matter


class RegistroDocentes(object):
    message_box: QMessageBox
    aux2 = " "
    con = 0

    def setup_ui(self, main_window):
        main_window.setObjectName("Registro de docentes")
        main_window.resize(538, 777)
        main_window.setStyleSheet("background-color: rgb(128, 195, 161)")
        a = 540
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 50, 341, 61))
        self.label.setStyleSheet("\n"
                                 "font: 75 8pt \"Segoe Print\";")
        self.label.setObjectName("label")
        self.nombre = QtWidgets.QLabel(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(60, 170, 91, 21))
        self.nombre.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.nombre.setObjectName("nombre")
        self.identifi = QtWidgets.QLabel(self.centralwidget)
        self.identifi.setGeometry(QtCore.QRect(60, 220, 141, 31))
        self.identifi.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.identifi.setObjectName("identifi")
        self.tipo = QtWidgets.QLabel(self.centralwidget)
        self.tipo.setGeometry(QtCore.QRect(60, 270, 71, 31))
        self.tipo.setStyleSheet("\n"
                                "font: 75 8pt \"Segoe Print\";")
        self.tipo.setObjectName("tipo")
        self.txtnombre = QtWidgets.QTextEdit(self.centralwidget)
        self.txtnombre.setGeometry(QtCore.QRect(250, 170, 241, 31))
        self.txtnombre.setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "font: 10pt \"MS Shell Dlg 2\";\n"
                                     "background-color: rgb(255, 255, 255);")
        self.txtnombre.setObjectName("txtNombre")

        self.txtident = QtWidgets.QTextEdit(self.centralwidget)
        self.txtident.setGeometry(QtCore.QRect(250, 220, 241, 31))
        self.txtident.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "font: 10pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(255, 255, 255);")
        self.txtident.setObjectName("txtIdent")
        self.txttipo = QtWidgets.QTextEdit(self.centralwidget)
        self.txttipo.setGeometry(QtCore.QRect(250, 270, 241, 31))
        self.txttipo.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 10pt \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(255, 255, 255);")
        self.txttipo.setObjectName("txtTipo")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(150, 120, 221, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btnaceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnaceptar.setGeometry(QtCore.QRect(260, 640, 101, 31))
        self.btnaceptar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 51, 51);")
        self.btnaceptar.setObjectName("btnAceptar")
        self.btnlimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnlimpiar.setGeometry(QtCore.QRect(390, 640, 101, 31))
        self.btnlimpiar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 51, 51);")
        self.btnlimpiar.setObjectName("btnLimpiar")
        self.comboasignatura = QtWidgets.QComboBox(self.centralwidget)
        self.comboasignatura.setGeometry(QtCore.QRect(250, 480, 241, 31))
        self.comboasignatura.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(0, 0, 0);")
        self.comboasignatura.setObjectName("comboAsignatura")
        res = obtener_matter()

        for aux in res:
            aux2 = str((aux[2]))
            print(aux2)
            self.comboasignatura.addItem(aux2)

        self.combociudad = QtWidgets.QComboBox(self.centralwidget)
        self.combociudad.setGeometry(QtCore.QRect(250, 540, 241, 31))
        self.combociudad.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.combociudad.setObjectName("comboCiudad")
        itemsa = ('', 'Armenia', 'Pereira', 'Buga')
        self.combociudad.addItems(itemsa)
        self.btnregresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnregresar.setGeometry(QtCore.QRect(60, 640, 101, 31))
        self.btnregresar.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(0, 51, 51);")
        self.btnregresar.setObjectName("btnRegresar")
        self.txtlimhoras = QtWidgets.QTextEdit(self.centralwidget)
        self.txtlimhoras.setGeometry(QtCore.QRect(250, 320, 241, 31))
        self.txtlimhoras.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       "font: 10pt \"MS Shell Dlg 2\";\n"
                                       "background-color: rgb(255, 255, 255);")
        self.txtlimhoras.setObjectName("txtLimHoras")
        self.asignatura_2 = QtWidgets.QLabel(self.centralwidget)
        self.asignatura_2.setGeometry(QtCore.QRect(60, 320, 131, 31))
        self.asignatura_2.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_2.setObjectName("asignatura_2")
        self.asignatura_3 = QtWidgets.QLabel(self.centralwidget)
        self.asignatura_3.setGeometry(QtCore.QRect(60, 370, 131, 31))
        self.asignatura_3.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_3.setObjectName("asignatura_3")
        self.txttelefono = QtWidgets.QTextEdit(self.centralwidget)
        self.txttelefono.setGeometry(QtCore.QRect(250, 370, 241, 31))
        self.txttelefono.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       "font: 10pt \"MS Shell Dlg 2\";\n"
                                       "background-color: rgb(255, 255, 255);")
        self.txttelefono.setObjectName("txtTelefono")
        self.asignatura_4 = QtWidgets.QLabel(self.centralwidget)
        self.asignatura_4.setGeometry(QtCore.QRect(60, 480, 131, 31))
        self.asignatura_4.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_4.setObjectName("asignatura")
        self.asignatura_5 = QtWidgets.QLabel(self.centralwidget)
        self.asignatura_5.setGeometry(QtCore.QRect(60, 420, 131, 31))
        self.asignatura_5.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_5.setObjectName("Estado")
        self.labelciudad = QtWidgets.QLabel(self.centralwidget)
        self.labelciudad.setGeometry(QtCore.QRect(60, 540, 131, 31))
        self.labelciudad.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.labelciudad.setObjectName("Ciudad")
        self.comboestado = QtWidgets.QComboBox(self.centralwidget)
        self.comboestado.setGeometry(QtCore.QRect(250, 420, 241, 31))
        self.comboestado.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.comboestado.setCurrentText("")
        self.comboestado.setObjectName("comboEstado")
        items = ('', 'ACTIVO', 'INACTIVO')
        self.comboestado.addItems(items)

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 538, 21))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.btnaceptar.clicked.connect(self.venta_acep)
        self.btnlimpiar.clicked.connect(self.limpiar)

        self.retranslate_ui(main_window)

        QtCore.QMetaObject.connectSlotsByName(main_window)

    def limpiar(self):
        self.txtnombre.clear()
        self.txtident.clear()
        self.txttelefono.clear()
        self.txtlimhoras.clear()
        self.txttipo.clear()
        self.comboestado.clear()
        self.comboasignatura.clear()

    def venta_acep(self):
        try:
            nomb = self.txtnombre.toPlainText()
            tipo = self.txttipo.toPlainText()
            lim = self.txtlimhoras.toPlainText()
            tel = self.txttelefono.toPlainText()
            iden = self.txtident.toPlainText()
            esta = str(self.comboestado.currentText())
            asig = str(self.comboasignatura.currentText())
            ciudad = str(self.combociudad.currentText())
            limit = int(lim)
            name = str(nomb)
            type = str(tipo)
            phone = str(tel)
            ident = str(iden)
            print(limit)
            if len(nomb) == 0 | len(tipo) == 0 | len(lim) == 0 | len(tel) == 0 | len(iden) == 0 | len(esta) == 0:
                self.mostrar_mensaje("Alerta", "¡Hay campos vacios!", "", QMessageBox.Warning, False)
            else:
                register_docent(name, esta, limit, type, phone, ident, asig, ciudad)
                self.mostrar_mensaje("Información", "¡Datos registrados con exito!", "", QMessageBox.Warning, False)
        except ValueError:
            self.mostrar_mensaje("Información", "¡La entrada es incorrecta, escriba un numero entero!",
                                "", QMessageBox.Warning, False)
            # Back up the reference to the exceptionhook
            sys._excepthook = sys.excepthook

    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        print(exctype, value, traceback)
        # Call the normal Exception hook after
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)
        # Set the exception hook to our wrapping function
        sys.excepthook = my_exception_hook

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
        main_window.setWindowTitle(_translate("MainWindow", "Registro docentes"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#000000;\">Registro de Docentes</span></p></body></html>"))
        self.nombre.setText(_translate("MainWindow",
                                       "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Nombre:</span></p></body></html>"))
        self.identifi.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Identificacíon:</span></p></body></html>"))
        self.tipo.setText(_translate("MainWindow",
                                     "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Tipo:</span></p></body></html>"))
        self.btnaceptar.setText(_translate("MainWindow", "ACEPTAR"))
        self.btnlimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.btnregresar.setText(_translate("MainWindow", "REGRESAR"))
        self.asignatura_2.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Limite de horas:</span></p><p><br/></p></body></html>"))
        self.asignatura_3.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Telefono:</span></p></body></html>"))
        self.asignatura_4.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Asignatura:</span></p></body></html>"))
        self.asignatura_5.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Estado:</span></p><p><br/></p></body></html>"))
        self.labelciudad.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Ciudad:</span></p><p><br/></p></body></html>"))
