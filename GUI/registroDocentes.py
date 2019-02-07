# coding: utf-8

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\registroDocentes.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from logica.Persistence import register_Docent
from logica.Persistence import obtener_Matter

class RegistroDocentes(object):
    message_box: QMessageBox
    aux2 = " "
    con = 0
    def setup_Ui(self, MainWindow):
        MainWindow.setObjectName("Registro de docentes")
        MainWindow.resize(538, 777)
        MainWindow.setStyleSheet("background-color: rgb(128, 195, 161)")
        a = 540
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.txtNombre = QtWidgets.QTextEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(250, 170, 241, 31))
        self.txtNombre.setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "font: 10pt \"MS Shell Dlg 2\";\n"
                                     "background-color: rgb(255, 255, 255);")
        self.txtNombre.setObjectName("txtNombre")

        self.txtIdent = QtWidgets.QTextEdit(self.centralwidget)
        self.txtIdent.setGeometry(QtCore.QRect(250, 220, 241, 31))
        self.txtIdent.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "font: 10pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(255, 255, 255);")
        self.txtIdent.setObjectName("txtIdent")
        self.txtTipo = QtWidgets.QTextEdit(self.centralwidget)
        self.txtTipo.setGeometry(QtCore.QRect(250, 270, 241, 31))
        self.txtTipo.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "font: 10pt \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(255, 255, 255);")
        self.txtTipo.setObjectName("txtTipo")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(150, 120, 221, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(260, 640, 101, 31))
        self.btnAceptar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 51, 51);")
        self.btnAceptar.setObjectName("btnAceptar")
        self.btnLimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpiar.setGeometry(QtCore.QRect(390, 640, 101, 31))
        self.btnLimpiar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 51, 51);")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.comboAsignatura = QtWidgets.QComboBox(self.centralwidget)
        self.comboAsignatura.setGeometry(QtCore.QRect(250, 480, 241, 31))
        self.comboAsignatura.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(0, 0, 0);")
        self.comboAsignatura.setObjectName("comboAsignatura")
        res = obtener_Matter()

        for aux in res:
            aux2 = str((aux[2]))
            print(aux2)
            self.comboAsignatura.addItem(aux2)

        self.comboCiudad = QtWidgets.QComboBox(self.centralwidget)
        self.comboCiudad.setGeometry(QtCore.QRect(250, 540, 241, 31))
        self.comboCiudad.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(0, 0, 0);")
        self.comboCiudad.setObjectName("comboCiudad")
        itemsa = ('', 'Armenia', 'Pereira', 'Buga')
        self.comboCiudad.addItems(itemsa)
        self.btnRegresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(60, 640, 101, 31))
        self.btnRegresar.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(0, 51, 51);")
        self.btnRegresar.setObjectName("btnRegresar")
        self.txtLimHoras = QtWidgets.QTextEdit(self.centralwidget)
        self.txtLimHoras.setGeometry(QtCore.QRect(250, 320, 241, 31))
        self.txtLimHoras.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       "font: 10pt \"MS Shell Dlg 2\";\n"
                                       "background-color: rgb(255, 255, 255);")
        self.txtLimHoras.setObjectName("txtLimHoras")
        self.asignatura_2 = QtWidgets.QLabel(self.centralwidget)
        self.asignatura_2.setGeometry(QtCore.QRect(60, 320, 131, 31))
        self.asignatura_2.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_2.setObjectName("asignatura_2")
        self.asignatura_3 = QtWidgets.QLabel(self.centralwidget)
        self.asignatura_3.setGeometry(QtCore.QRect(60, 370, 131, 31))
        self.asignatura_3.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_3.setObjectName("asignatura_3")
        self.txtTelefono = QtWidgets.QTextEdit(self.centralwidget)
        self.txtTelefono.setGeometry(QtCore.QRect(250, 370, 241, 31))
        self.txtTelefono.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       "font: 10pt \"MS Shell Dlg 2\";\n"
                                       "background-color: rgb(255, 255, 255);")
        self.txtTelefono.setObjectName("txtTelefono")
        self.asignatura_4 = QtWidgets.QLabel(self.centralwidget)
        self.asignatura_4.setGeometry(QtCore.QRect(60, 480, 131, 31))
        self.asignatura_4.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_4.setObjectName("asignatura")
        self.asignatura_5 = QtWidgets.QLabel(self.centralwidget)
        self.asignatura_5.setGeometry(QtCore.QRect(60, 420, 131, 31))
        self.asignatura_5.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.asignatura_5.setObjectName("Estado")
        self.labelCiudad = QtWidgets.QLabel(self.centralwidget)
        self.labelCiudad.setGeometry(QtCore.QRect(60, 540, 131, 31))
        self.labelCiudad.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.labelCiudad.setObjectName("Ciudad")
        self.comboEstado = QtWidgets.QComboBox(self.centralwidget)
        self.comboEstado.setGeometry(QtCore.QRect(250, 420, 241, 31))
        self.comboEstado.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.comboEstado.setCurrentText("")
        self.comboEstado.setObjectName("comboEstado")
        items = ('', 'ACTIVO', 'INACTIVO')
        self.comboEstado.addItems(items)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 538, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btnAceptar.clicked.connect(self.ventaAcep)
        self.btnLimpiar.clicked.connect(self.limpiar)


        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def limpiar(self):
        self.txtNombre.clear()
        self.txtIdent.clear()
        self.txtTelefono.clear()
        self.txtLimHoras.clear()
        self.txtTipo.clear()
        self.comboEstado.clear()
        self.comboAsignatura.clear()

    def ventaAcep(self):
       try:
        nomb = self.txtNombre.toPlainText()
        tipo = self.txtTipo.toPlainText()
        lim = self.txtLimHoras.toPlainText()
        tel = self.txtTelefono.toPlainText()
        iden = self.txtIdent.toPlainText()
        esta = str(self.comboEstado.currentText())
        asig = str(self.comboAsignatura.currentText())
        ciudad = str(self.comboCiudad.currentText())
        limit = int(lim)
        name = str(nomb)
        type = str(tipo)
        phone = str(tel)
        ident = str(iden)
        print(limit)
        if len(nomb) == 0 | len(tipo) == 0 | len(lim) == 0 | len(tel) == 0 | len(iden) == 0 | len(esta) == 0:
            self.mostrarMensaje("Alerta", "¡Hay campos vacios!", "", QMessageBox.Warning, False)
        else:
            register_Docent(name, esta, limit, type, phone, ident, asig, ciudad)
            self.mostrarMensaje("Información", "¡Datos registrados con exito!", "", QMessageBox.Warning, False)
       except ValueError:
           self.mostrarMensaje("Información", "¡La entrada es incorrecta, escriba un numero entero!",
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Registro docentes"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#000000;\">Registro de Docentes</span></p></body></html>"))
        self.nombre.setText(_translate("MainWindow",
                                       "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Nombre:</span></p></body></html>"))
        self.identifi.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Identificacíon:</span></p></body></html>"))
        self.tipo.setText(_translate("MainWindow",
                                     "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Tipo:</span></p></body></html>"))
        self.btnAceptar.setText(_translate("MainWindow", "ACEPTAR"))
        self.btnLimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.btnRegresar.setText(_translate("MainWindow", "REGRESAR"))
        self.asignatura_2.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Limite de horas:</span></p><p><br/></p></body></html>"))
        self.asignatura_3.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Telefono:</span></p></body></html>"))
        self.asignatura_4.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Asignatura:</span></p></body></html>"))
        self.asignatura_5.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Estado:</span></p><p><br/></p></body></html>"))
        self.labelCiudad.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Ciudad:</span></p><p><br/></p></body></html>"))
