# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\ActualizarAsignaturas.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
from typing import Any

from PyQt5 import QtCore, QtGui, QtWidgets
from logica.Persistence import searchhMatter
from logica.Persistence import update_Matter


class actualizarAsignatura(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Actualizar Asignaturas")
        MainWindow.resize(722, 647)
        MainWindow.setStyleSheet("background-color: rgb(0, 51, 51)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 381, 61))
        self.label.setStyleSheet("\n"
                                 "font: 75 8pt \"Segoe Print\";")
        self.label.setObjectName("label")
        self.txtCodigoBuscar = QtWidgets.QTextEdit(self.centralwidget)
        self.txtCodigoBuscar.setGeometry(QtCore.QRect(30, 190, 191, 31))
        self.txtCodigoBuscar.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "font: 10pt \"MS Shell Dlg 2\";\n"
                                           "background-color: rgb(255, 255, 255);")
        self.txtCodigoBuscar.setObjectName("txtCodigoBuscar")
        self.codigo = QtWidgets.QLabel(self.centralwidget)
        self.codigo.setGeometry(QtCore.QRect(20, 150, 221, 31))
        self.codigo.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
                                  "color: rgb(255, 255, 255);")
        self.codigo.setObjectName("codigo")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(30, 250, 101, 31))
        self.btnBuscar.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(0, 204, 102);")
        self.btnBuscar.setObjectName("btnBuscar")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(260, 110, 441, 421))
        self.groupBox.setStyleSheet("font: 75 14pt \"Segoe Print\";\n"
                                    "color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.codigo_2 = QtWidgets.QLabel(self.groupBox)
        self.codigo_2.setGeometry(QtCore.QRect(10, 50, 91, 31))
        self.codigo_2.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.codigo_2.setObjectName("codigo_2")
        self.semestre = QtWidgets.QLabel(self.groupBox)
        self.semestre.setGeometry(QtCore.QRect(10, 290, 211, 31))
        self.semestre.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.semestre.setObjectName("semestre")
        self.boxSemestre = QtWidgets.QSpinBox(self.groupBox)
        self.boxSemestre.setGeometry(QtCore.QRect(220, 290, 71, 22))
        self.boxSemestre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.boxSemestre.setMinimum(1)
        self.boxSemestre.setMaximum(6)
        self.boxSemestre.setProperty("value", 1)
        self.boxSemestre.setObjectName("boxSemestre")
        self.numCreditos = QtWidgets.QLabel(self.groupBox)
        self.numCreditos.setGeometry(QtCore.QRect(10, 150, 171, 61))
        self.numCreditos.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.numCreditos.setObjectName("numCreditos")
        self.numHorasSemestre = QtWidgets.QLabel(self.groupBox)
        self.numHorasSemestre.setGeometry(QtCore.QRect(10, 200, 211, 61))
        self.numHorasSemestre.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.numHorasSemestre.setObjectName("numHorasSemestre")
        self.nombre = QtWidgets.QLabel(self.groupBox)
        self.nombre.setGeometry(QtCore.QRect(10, 100, 91, 21))
        self.nombre.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.nombre.setObjectName("nombre")
        self.txtNumHorSemestre = QtWidgets.QTextEdit(self.groupBox)
        self.txtNumHorSemestre.setGeometry(QtCore.QRect(220, 190, 201, 31))
        self.txtNumHorSemestre.setStyleSheet("color: rgb(0, 0, 0);\n"
                                             "font: 10pt \"MS Shell Dlg 2\";\n"
                                             "background-color: rgb(255, 255, 255);")
        self.txtNumHorSemestre.setObjectName("txtNumHorSemestre")
        self.boxCreditos = QtWidgets.QSpinBox(self.groupBox)
        self.boxCreditos.setGeometry(QtCore.QRect(220, 150, 71, 22))
        self.boxCreditos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.boxCreditos.setMinimum(1)
        self.boxCreditos.setMaximum(6)
        self.boxCreditos.setProperty("value", 1)
        self.boxCreditos.setObjectName("boxCreditos")
        self.txtCodigo = QtWidgets.QTextEdit(self.groupBox)
        self.txtCodigo.setGeometry(QtCore.QRect(220, 50, 201, 31))
        self.txtCodigo.setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "font: 10pt \"MS Shell Dlg 2\";\n"
                                     "background-color: rgb(255, 255, 255);")
        self.txtCodigo.setObjectName("txtCodigo")
        self.txtNombre = QtWidgets.QTextEdit(self.groupBox)
        self.txtNombre.setGeometry(QtCore.QRect(220, 100, 201, 31))
        self.txtNombre.setStyleSheet("color: rgb(0, 0, 0);\n"
                                     "font: 10pt \"MS Shell Dlg 2\";\n"
                                     "background-color: rgb(255, 255, 255);")
        self.txtNombre.setObjectName("txtNombre")
        self.btnLimpiar = QtWidgets.QPushButton(self.groupBox)
        self.btnLimpiar.setGeometry(QtCore.QRect(340, 350, 81, 31))
        self.btnLimpiar.setStyleSheet("font: 75 11pt \"Segoe Print\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 204, 102);")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.btnActualizar = QtWidgets.QPushButton(self.groupBox)
        self.btnActualizar.setGeometry(QtCore.QRect(220, 350, 111, 31))
        self.btnActualizar.setStyleSheet("font: 75 11pt \"Segoe Print\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(0, 204, 102);")
        self.btnActualizar.setObjectName("btnActualizar")
        self.semestre_2 = QtWidgets.QLabel(self.groupBox)
        self.semestre_2.setGeometry(QtCore.QRect(10, 240, 131, 31))
        self.semestre_2.setStyleSheet("font: 10pt \"Segoe Print\";\n"
                                      "color: rgb(255, 255, 255);")
        self.semestre_2.setObjectName("semestre_2")
        self.txtCodRequis = QtWidgets.QTextEdit(self.groupBox)
        self.txtCodRequis.setGeometry(QtCore.QRect(220, 240, 201, 31))
        self.txtCodRequis.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "font: 10pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(255, 255, 255);")
        self.txtCodRequis.setObjectName("txtCodRequis")
        self.btnRegresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(40, 450, 101, 31))
        self.btnRegresar.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(0, 204, 102);")
        self.btnRegresar.setObjectName("btnRegresar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnBuscar.clicked.connect(self.buscar)
        self.btnActualizar.clicked.connect(self.actualizar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def buscar(self):
        codBuscar = str(self.txtCodigoBuscar.toPlainText())
        res: Any = searchhMatter(codBuscar)
        if not None == res:
            print(res[1], res[2])
            self.txtCodigo.setText(str(res[1]))
            self.txtNombre.setText(str(res[2]))
            self.boxSemestre.setProperty("value", str(res[3]))
            self.boxCreditos.setProperty("value", str(res[4]))
            self.txtCodRequis.setText(str(res[5]))
            self.txtNumHorSemestre.setText(str(res[7]))
        else:
            print("no existe")
    def actualizar(self):
        cod = str(self.txtCodigo.toPlainText())
        nom = str(self.txtNombre.toPlainText())
        ubiSemestre = int(self.boxSemestre.text())
        numCreditos = self.boxCreditos.text()
        codRequisito = self.txtCodRequis.toPlainText()
        numHoursSem: str = self.txtNumHorSemestre.toPlainText()
        num: int = int(numHoursSem)
        update_Matter(cod, nom, ubiSemestre, numCreditos, codRequisito, num)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Actualizar asignaturas"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Actualizar  asignaturas</span></p><p align=\"center\"><br/></p></body></html>"))
        self.codigo.setText(_translate("MainWindow",
                                       "<html><head/><body><p>Ingrese código de la asignatura:</p><p><br/></p></body></html>"))
        self.btnBuscar.setText(_translate("MainWindow", "BUSCAR"))
        self.groupBox.setTitle(_translate("MainWindow", "Actualizar datos"))
        self.codigo_2.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Codigo:</span></p><p><br/></p></body></html>"))
        self.semestre.setText(_translate("MainWindow",
                                         "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Semestre:</span></p><p><br/></p><p><br/></p></body></html>"))
        self.numCreditos.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Numero de creditos:</span></p><p><br/></p></body></html>"))
        self.numHorasSemestre.setText(_translate("MainWindow",
                                                 "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Num. horas por semestre:</span></p><p><br/></p></body></html>"))
        self.nombre.setText(_translate("MainWindow",
                                       "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Nombre:</span></p></body></html>"))
        self.btnLimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.btnActualizar.setText(_translate("MainWindow", "ACTUALIZAR"))
        self.semestre_2.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" font-size:11pt;\">Cod. Requisito:</span></p></body></html>"))
        self.btnRegresar.setText(_translate("MainWindow", "REGRESAR"))
