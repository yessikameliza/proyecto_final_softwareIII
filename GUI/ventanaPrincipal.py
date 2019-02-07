# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\ventanaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from GUI.registroFechas import Ui_Form
from GUI.registroDocentes import RegistroDocentes
from GUI.registroAsignaturas import RegistroAsignaturas
from GUI.ActualizarAsignaturas import ActualizarAsignatura
from GUI.eliminarAsignatura import EliminarAsignatura
from GUI.ActualizarDocentes import ActualizarDocente
from GUI.eliminarDocente import EliminarDocente
from GUI.primerasFechas import PrimerasFechas
from GUI.fechasAlternas import FechasAlternas
from GUI.pereiraDomingos import FechasPereira

from logica.Persistence import gene_hours, obtener_fecha
from logica.Persistence import obtener_fechas_p
from logica.Persistence import obtener_f_induct
from logica.Persistence import obtenerDatosProfe

class VentanaPrincipal(QtWidgets.QMainWindow):
    def setup_Ui(self, Form):
        Form.setObjectName("Form")
        Form.resize(1267, 854)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1411, 121))
        self.frame.setStyleSheet("background-color: rgb(128, 195, 161);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(520, 10, 381, 101))
        self.label.setStyleSheet("font: 75 8pt \"Segoe Print\";")
        self.label.setObjectName("label")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 280, 1411, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(11)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("background-color: rgb(128, 195, 161);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.groupBox = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 311, 381))
        self.groupBox.setStyleSheet("font: 75 14pt \"Segoe Print\";\n"
                                    "color: rgb(0, 0, 0);")
        self.groupBox.setObjectName("groupBox")

        self.btnRegistrarDocentes = QtWidgets.QPushButton(self.groupBox)
        self.btnRegistrarDocentes.setGeometry(QtCore.QRect(40, 40, 241, 31))
        self.btnRegistrarDocentes.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "background-color: rgb(0, 51, 51);\n"
                                                "")
        self.btnRegistrarDocentes.setObjectName("btnRegistrarDocentes")

        self.btnRegistrarFechas = QtWidgets.QPushButton(self.groupBox)
        self.btnRegistrarFechas.setGeometry(QtCore.QRect(40, 122, 241, 31))
        self.btnRegistrarFechas.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "background-color: rgb(0, 51, 51);\n"
                                              "")
        self.btnRegistrarFechas.setObjectName("btnRegistrarFechas")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 160, 271, 191))
        self.groupBox_3.setStyleSheet("font: 75 14pt \"Segoe Print\";")
        self.groupBox_3.setObjectName("groupBox_3")
        self.btnGenerarHorArmen = QtWidgets.QPushButton(self.groupBox_3)
        self.btnGenerarHorArmen.setGeometry(QtCore.QRect(20, 110, 241, 31))
        self.btnGenerarHorArmen.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "background-color: rgb(0, 51, 51);\n"
                                              "\n"
                                              "")
        self.btnGenerarHorArmen.setObjectName("btnGenerarHorArmen")
        self.btnGenerarHorPer = QtWidgets.QPushButton(self.groupBox_3)
        self.btnGenerarHorPer.setGeometry(QtCore.QRect(20, 150, 241, 31))
        self.btnGenerarHorPer.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "background-color: rgb(0, 51, 51);\n"
                                            "\n"
                                            "")
        self.btnGenerarHorPer.setObjectName("btnGenerarHorPer")
        self.btnGenerarHorBuga = QtWidgets.QPushButton(self.groupBox_3)
        self.btnGenerarHorBuga.setGeometry(QtCore.QRect(20, 70, 241, 31))
        self.btnGenerarHorBuga.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "background-color: rgb(0, 51, 51);\n"
                                             "\n"
                                             "")
        self.btnGenerarHorBuga.setObjectName("btnGenerarHorBuga")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 11pt \"Segoe Print\";")
        self.label_4.setObjectName("label_4")
        self.spinSemestre = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinSemestre.setGeometry(QtCore.QRect(190, 40, 71, 22))
        self.spinSemestre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "color: rgb(0, 0, 0);")
        self.spinSemestre.setMinimum(1)
        self.spinSemestre.setMaximum(6)
        self.spinSemestre.setProperty("value", 1)
        self.spinSemestre.setObjectName("spinSemestre")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_4.setGeometry(QtCore.QRect(370, 10, 861, 381))
        self.groupBox_4.setStyleSheet("font: 75 14pt \"Segoe Print\";\n"
                                      "color: rgb(0, 0, 0);")
        self.groupBox_4.setObjectName("groupBox_4")
        self.tablaHorario = QtWidgets.QTableWidget(self.groupBox_4)
        self.tablaHorario.setGeometry(QtCore.QRect(30, 30, 731, 331))
        self.tablaHorario.setSizeIncrement(QtCore.QSize(15, 8))
        self.tablaHorario.setBaseSize(QtCore.QSize(22, 18))
        self.tablaHorario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 75 9pt \"Segoe Print\";\n"
                                        "color: rgb(0, 0, 0);")
        self.tablaHorario.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tablaHorario.setLineWidth(2)
        self.tablaHorario.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tablaHorario.setIconSize(QtCore.QSize(19, 6))
        self.tablaHorario.setShowGrid(True)
        self.tablaHorario.setGridStyle(QtCore.Qt.SolidLine)
        self.tablaHorario.setWordWrap(True)
        self.tablaHorario.setCornerButtonEnabled(True)
        self.tablaHorario.setObjectName("tablaHorario")
        self.tablaHorario.setColumnCount(3)
        self.tablaHorario.setRowCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaHorario.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaHorario.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaHorario.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(9, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(10, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(11, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaHorario.setItem(11, 2, item)

        self.tablaHorario.horizontalHeader().setDefaultSectionSize(256)
        self.tablaHorario.horizontalHeader().setMinimumSectionSize(50)
        self.tablaHorario.verticalHeader().setDefaultSectionSize(55)
        self.btnImprimir = QtWidgets.QPushButton(self.groupBox_4)
        self.btnImprimir.setGeometry(QtCore.QRect(770, 170, 81, 41))
        self.btnImprimir.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(0, 51, 51);\n"
                                       "\n""")

        self.btnImprimir.setObjectName("btnImprimir")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 120, 1411, 151))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 10, 1171, 141))
        self.groupBox_2.setStyleSheet("\n"
                                      "font: 75 12pt \"Segoe Print\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.tablaInfoAcademica = QtWidgets.QTableWidget(self.groupBox_2)
        self.tablaInfoAcademica.setGeometry(QtCore.QRect(60, 30, 1061, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(19)
        sizePolicy.setHeightForWidth(self.tablaInfoAcademica.sizePolicy().hasHeightForWidth())
        self.tablaInfoAcademica.setSizePolicy(sizePolicy)
        self.tablaInfoAcademica.setStyleSheet("")
        self.tablaInfoAcademica.setObjectName("tablaInfoAcademica")
        self.tablaInfoAcademica.setColumnCount(5)
        self.tablaInfoAcademica.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaInfoAcademica.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.tablaInfoAcademica.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaInfoAcademica.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaInfoAcademica.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaInfoAcademica.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaInfoAcademica.setItem(3, 4, item)
        self.tablaInfoAcademica.horizontalHeader().setDefaultSectionSize(207)
        self.tablaInfoAcademica.horizontalHeader().setMinimumSectionSize(46)
        self.tablaInfoAcademica.verticalHeader().setDefaultSectionSize(26)
        Form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1267, 21))
        self.menubar.setObjectName("menubar")
        self.menuOpciones = QtWidgets.QMenu(self.menubar)
        self.menuOpciones.setObjectName("menuOpciones")
        self.menuAsignaturas = QtWidgets.QMenu(self.menubar)
        self.menuAsignaturas.setObjectName("menuAsignaturas")
        self.menuDocentes = QtWidgets.QMenu(self.menubar)
        self.menuDocentes.setObjectName("menuDocentes")
        Form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)
        self.actionRegistrar_espacios_fisicos = QtWidgets.QAction(Form)
        self.actionRegistrar_espacios_fisicos.setWhatsThis("")
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionRegistrar_espacios_fisicos.setFont(font)
        self.actionRegistrar_espacios_fisicos.setAutoRepeat(False)
        self.actionRegistrar_espacios_fisicos.setIconVisibleInMenu(False)
        self.actionRegistrar_espacios_fisicos.setObjectName("actionRegistrar_espacios_fisicos")
        self.actionRegistrar_docentes = QtWidgets.QAction(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionRegistrar_docentes.setFont(font)
        self.actionRegistrar_docentes.setObjectName("actionRegistrar_docentes")
        self.actionRegistro_intensidad_horaria = QtWidgets.QAction(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionRegistro_intensidad_horaria.setFont(font)
        self.actionRegistro_intensidad_horaria.setObjectName("actionRegistro_intensidad_horaria")
        self.actionGenerar_reportes = QtWidgets.QAction(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionGenerar_reportes.setFont(font)
        self.actionGenerar_reportes.setObjectName("actionGenerar_reportes")
        self.actionRegistrar_Asignaturas = QtWidgets.QAction(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionRegistrar_Asignaturas.setFont(font)
        self.actionRegistrar_Asignaturas.setObjectName("actionRegistrar_Asignaturas")
        self.actionRegistrar_Asignaturas_2 = QtWidgets.QAction(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionRegistrar_Asignaturas_2.setFont(font)
        self.actionRegistrar_Asignaturas_2.setObjectName("actionRegistrar_Asignaturas_2")
        self.actionModificar_Asignaturas = QtWidgets.QAction(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionModificar_Asignaturas.setFont(font)
        self.actionModificar_Asignaturas.setObjectName("actionModificar_Asignaturas")
        self.actionEliminar_Asignaturas = QtWidgets.QAction(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionEliminar_Asignaturas.setFont(font)
        self.actionEliminar_Asignaturas.setObjectName("actionEliminar_Asignaturas")
        self.actionVer_fechas_alternas = QtWidgets.QAction(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionVer_fechas_alternas.setFont(font)
        self.actionVer_fechas_alternas.setObjectName("actionVer_fechas_alternas")

        self.actionVer_fechas_pereira = QtWidgets.QAction(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionVer_fechas_pereira.setFont(font)
        self.actionVer_fechas_pereira.setObjectName("actionVer_fechas_pereira")

        self.actionActualizar_Docente = QtWidgets.QAction(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionActualizar_Docente.setFont(font)
        self.actionActualizar_Docente.setObjectName("actionActualizar_Docente")
        self.actionEliminar_docente = QtWidgets.QAction(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionEliminar_docente.setFont(font)
        self.actionEliminar_docente.setObjectName("actionEliminar_docente")
        self.menuOpciones.addSeparator()
        self.menuOpciones.addAction(self.actionGenerar_reportes)
        self.menuOpciones.addAction(self.actionVer_fechas_alternas)
        self.menuOpciones.addAction(self.actionVer_fechas_pereira)
        self.menuAsignaturas.addAction(self.actionRegistrar_Asignaturas_2)
        self.menuAsignaturas.addAction(self.actionModificar_Asignaturas)
        self.menuAsignaturas.addAction(self.actionEliminar_Asignaturas)
        self.menuDocentes.addAction(self.actionActualizar_Docente)
        self.menuDocentes.addAction(self.actionEliminar_docente)
        self.menubar.addAction(self.menuOpciones.menuAction())
        self.menubar.addAction(self.menuAsignaturas.menuAction())
        self.menubar.addAction(self.menuDocentes.menuAction())
        self.retranslateUi(Form)
        self.btnRegistrarDocentes.clicked.connect(self.ventanaRegistroDocente)
        self.btnRegistrarFechas.clicked.connect(self.ventanaRegistroFecha)
        self.actionRegistrar_Asignaturas_2.triggered.connect(self.ventanaRegAsi)
        self.actionModificar_Asignaturas.triggered.connect(self.ventanaModAsig)
        self.actionEliminar_Asignaturas.triggered.connect(self.ventanaElimAsig)
        self.actionActualizar_Docente.triggered.connect(self.ventanaActDoc)
        self.actionEliminar_docente.triggered.connect(self.ventanaElimDoc)
        self.actionGenerar_reportes.triggered.connect(self.ventanaPrimerasFecha)
        self.actionVer_fechas_alternas.triggered.connect(self.ventanaFechasAlternas)
        self.actionVer_fechas_pereira.triggered.connect(self.ventanaFechasPereira)
        self.btnGenerarHorArmen.clicked.connect(self.pruebaHorario)
        self.btnGenerarHorBuga.clicked.connect(self.pruebaHorario2)
        self.btnGenerarHorPer.clicked.connect(self.pruebaHorario3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def ventanaFechasPereira(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = FechasPereira()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def ventanaRegistroDocente(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = RegistroDocentes()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def ventanaRegistroFecha(self):

        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
        self.close()

    def ventanaRegAsi(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = RegistroAsignaturas()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def ventanaModAsig(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = ActualizarAsignatura()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def ventanaElimAsig(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = EliminarAsignatura()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def ventanaActDoc(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = ActualizarDocente()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def ventanaElimDoc(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = EliminarDocente()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def ventanaPrimerasFecha(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = PrimerasFechas()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def ventanaFechasAlternas(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = FechasAlternas()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def setearTabla(self):
        i = 0
        j = 0
        while j < 3:
            while i < 12:
                item = self.tablaHorario.item(i, j)
                item.setText("")
                i = i + 1
            j = j + 1
            i = 0

    def llenartabla(self, semester, city):
        s: list = obtenerDatosProfe(semester, city)
        #item1 = self.tablaInfoAcademica.item(0, 1)
        #item1.setText("hh")
        a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
        rows: int = 0
        col: int = 0
        for i in s:
            for j in i:
                print(j, "contenidoo")
                print(rows, col)
                item = self.tablaInfoAcademica.item(rows, col)
                item.setText(str(j))

                if col < 4:
                    print(rows, col)
                    col = col+1
                else:
                    rows = rows+1
                    col = 0



    def pruebaHorario(self):
        self.setearTabla()
        semester: int = int(self.spinSemestre.text())
        print("este es el semestre", semester)
        hours: list = gene_hours(semester, "Armenia")
        self.llenartabla(semester, "Armenia")
        rows = 1
        i = 0
        if semester == 1:
            i = 4
            dateInduc: list = obtener_f_induct("inductorio")
            item = self.tablaHorario.item(0, 0)
            item.setText((dateInduc[0])[1])
            item = self.tablaHorario.item(2, 0)
            item.setText((dateInduc[1])[1])
        else:
            i = 0
        n = 1
        o = 1
        print("recibido en metodo prueba horario")
        print(hours)
        date: list = obtener_fechas_p("Primeras fechas", "Encuentros tutoriales")
        print(date, "arreglo date")
        for d in date:
            print("entrooooo date", d[3])
            if d[3] != n:
                i = 0
            if d[3] == 1:
                item = self.tablaHorario.item(i, 0)
                item.setText(d[1])
            elif d[3] == 2:
                n = 2
                item = self.tablaHorario.item(i, 1)
                item.setText(d[1])
            elif d[3] == 3:
                n = 3
                item = self.tablaHorario.item(i, 2)
                item.setText(d[1])
            i = i + 2
        for h in hours:
            if h[1] != o:
                rows = 1
            if h[1] == 1:
                item = self.tablaHorario.item(rows, 0)
                item.setText(h[0])
            elif h[1] == 2:
                o = 2
                item = self.tablaHorario.item(rows, 1)
                item.setText(h[0])
            elif h[1] == 3:
                o = 3
                item = self.tablaHorario.item(rows, 2)
                item.setText(h[0])
            rows = rows + 2
            print(rows)

    def pruebaHorario2(self):
        self.setearTabla()
        semester: int = int(self.spinSemestre.text())
        hours: list = gene_hours(semester, "Armenia")
        self.llenartabla(semester, "Buga")
        rows = 1
        i = 0
        if semester == 1:
            i = 4
            dateInduc: list = obtener_f_induct("inductorio")
            item = self.tablaHorario.item(0, 0)
            item.setText((dateInduc[0])[1])
            item = self.tablaHorario.item(2, 0)
            item.setText((dateInduc[1])[1])
        else:
            i = 0
        n = 1
        o = 1
        print("recibido en metodo prueba horario")
        print(hours)
        date: list = obtener_fechas_p("Fechas alternas", "Encuentros tutoriales")
        print(date, "arreglo date")
        for d in date:
            print("entrooooo date", d[3])
            if d[3] != n:
                i = 0
            if d[3] == 1:
                item = self.tablaHorario.item(i, 0)
                item.setText(d[1])
            elif d[3] == 2:
                n = 2
                item = self.tablaHorario.item(i, 1)
                item.setText(d[1])
            elif d[3] == 3:
                n = 3
                item = self.tablaHorario.item(i, 2)
                item.setText(d[1])
            i = i + 2
        for h in hours:
            if h[1] != o:
                rows = 1
            if h[1] == 1:
                item = self.tablaHorario.item(rows, 0)
                item.setText(h[0])
            elif h[1] == 2:
                o = 2
                item = self.tablaHorario.item(rows, 1)
                item.setText(h[0])
            elif h[1] == 3:
                o = 3
                item = self.tablaHorario.item(rows, 2)
                item.setText(h[0])
            rows = rows + 2
            print(rows)

    def pruebaHorario3(self):
        self.setearTabla()
        semester: int = int(self.spinSemestre.text())
        hours: list = gene_hours(semester, "Armenia")
        self.llenartabla(semester, "Pereira")
        rows = 1
        i = 0
        if semester == 1:
            i = 4
            dateInduc: list = obtener_f_induct("inductorio")
            item = self.tablaHorario.item(0, 0)
            item.setText((dateInduc[0])[1])
            item = self.tablaHorario.item(2, 0)
            item.setText((dateInduc[1])[1])
        else:
            i = 0
        n = 1
        o = 1
        date: list = obtener_fechas_p("Fechas alternas", "Encuentros tutoriales")
        for d in date:
            if d[3] != n:
                i = 0
            if d[3] == 1:
                item = self.tablaHorario.item(i, 0)
                item.setText(d[1])
            elif d[3] == 2:
                n = 2
                item = self.tablaHorario.item(i, 1)
                item.setText(d[1])
            elif d[3] == 3:
                n = 3
                item = self.tablaHorario.item(i, 2)
                item.setText(d[1])
            i = i + 2
        for h in hours:
            if h[1] != o:
                rows = 1
            if h[1] == 1:
                item = self.tablaHorario.item(rows, 0)
                item.setText(h[0])
            elif h[1] == 2:
                o = 2
                item = self.tablaHorario.item(rows, 1)
                item.setText(h[0])
            elif h[1] == 3:
                o = 3
                item = self.tablaHorario.item(rows, 2)
                item.setText(h[0])
            rows = rows + 2

    def mostrarMensaje(self, titulo: str, texto: str, texto_informativo: str, tipo_mensaje: QMessageBox,
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

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#000000;\">¡Bienvenido a SS MEWIN!</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#000000;\">Programador de horarios</span></p></body></html>"))
        self.groupBox.setTitle(_translate("Form", "Menú de opciones"))
        self.btnRegistrarDocentes.setText(_translate("Form", "Registrar Docentes"))
        self.btnRegistrarFechas.setText(_translate("Form", "Registrar fechas"))
        self.groupBox_3.setTitle(_translate("Form", "Generar horario"))
        self.btnGenerarHorArmen.setText(_translate("Form", "Generar horario Armenia"))
        self.btnGenerarHorPer.setText(_translate("Form", "Generar horario Pereira"))
        self.btnGenerarHorBuga.setText(_translate("Form", "Generar horario Buga"))
        self.label_4.setText(_translate("Form", "Semestre a generar:"))
        self.groupBox_4.setTitle(_translate("Form", "Información de horario"))
        self.btnGenerarHorArmen.clicked.connect(self.pruebaHorario)
        item = self.tablaHorario.horizontalHeaderItem(0)
        item.setText(_translate("Form", "BLOQUE A"))
        item = self.tablaHorario.horizontalHeaderItem(1)
        item.setText(_translate("Form", "BLOQUE B"))
        item = self.tablaHorario.horizontalHeaderItem(2)
        item.setText(_translate("Form", "BLOQUE C"))
        __sortingEnabled = self.tablaHorario.isSortingEnabled()
        self.tablaHorario.setSortingEnabled(False)
        item = self.tablaHorario.item(0, 0)
        item.setText(_translate("Form", "Fecha 1"))
        item = self.tablaHorario.item(0, 1)
        item.setText(_translate("Form", "Fecha 2"))
        item = self.tablaHorario.item(0, 2)
        item.setText(_translate("Form", "Fecha 3"))
        item = self.tablaHorario.item(2, 0)
        item.setText(_translate("Form", "Fecha 4"))
        item = self.tablaHorario.item(2, 1)
        item.setText(_translate("Form", "Fecha 5"))
        item = self.tablaHorario.item(2, 2)
        item.setText(_translate("Form", "Fecha 6"))
        item = self.tablaHorario.item(4, 0)
        item.setText(_translate("Form", "Fecha 7"))
        item = self.tablaHorario.item(4, 1)
        item.setText(_translate("Form", "Fecha 8"))
        item = self.tablaHorario.item(4, 2)
        item.setText(_translate("Form", "Fecha 9"))
        item = self.tablaHorario.item(6, 0)
        item.setText(_translate("Form", "Fecha 10"))
        item = self.tablaHorario.item(6, 1)
        item.setText(_translate("Form", "Fecha 11"))
        item = self.tablaHorario.item(6, 2)
        item.setText(_translate("Form", "Fecha 12"))
        item = self.tablaHorario.item(8, 0)
        item.setText(_translate("Form", "Fecha 13"))
        item = self.tablaHorario.item(8, 1)
        item.setText(_translate("Form", "Fecha 14"))
        item = self.tablaHorario.item(8, 2)
        item.setText(_translate("Form", "Fecha 15"))
        item = self.tablaHorario.item(10, 0)
        item.setText(_translate("Form", "Fecha 16"))
        item = self.tablaHorario.item(10, 1)
        item.setText(_translate("Form", "Fecha 17"))
        item = self.tablaHorario.item(10, 2)
        item.setText(_translate("Form", "Fecha 18"))
        self.tablaHorario.setSortingEnabled(__sortingEnabled)
        self.btnImprimir.setText(_translate("Form", "Imprimir"))
        self.groupBox_2.setTitle(_translate("Form", "Información "))
        item = self.tablaInfoAcademica.horizontalHeaderItem(0)
        item.setText(_translate("Form", "CÓDIGO"))
        item = self.tablaInfoAcademica.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ACTIVIDAD ACADÉMICA"))
        item = self.tablaInfoAcademica.horizontalHeaderItem(2)
        item.setText(_translate("Form", "REQUISITO"))
        item = self.tablaInfoAcademica.horizontalHeaderItem(3)
        item.setText(_translate("Form", "TUTOR"))
        item = self.tablaInfoAcademica.horizontalHeaderItem(4)
        item.setText(_translate("Form", "TELÉFONO"))
        self.menuOpciones.setTitle(_translate("Form", "Reportes"))
        self.menuAsignaturas.setTitle(_translate("Form", "Asignaturas"))
        self.menuDocentes.setTitle(_translate("Form", "Docentes"))
        self.actionRegistrar_espacios_fisicos.setText(_translate("Form", "Registrar espacios fisicos"))
        self.actionRegistrar_docentes.setText(_translate("Form", "Registrar docentes"))
        self.actionRegistro_intensidad_horaria.setText(_translate("Form", "Registrar intensidad horaria"))
        self.actionGenerar_reportes.setText(_translate("Form", "Ver primeras fechas"))
        self.actionRegistrar_Asignaturas.setText(_translate("Form", "Registrar Asignaturas"))
        self.actionRegistrar_Asignaturas_2.setText(_translate("Form", "Registrar asignaturas"))
        self.actionModificar_Asignaturas.setText(_translate("Form", "Modificar asignaturas"))
        self.actionEliminar_Asignaturas.setText(_translate("Form", "Eliminar asignaturas"))
        self.actionVer_fechas_alternas.setText(_translate("Form", "Ver fechas alternas"))
        self.actionVer_fechas_pereira.setText(_translate("Form", "Ver fechas pereira domingos"))
        self.actionActualizar_Docente.setText(_translate("Form", "Actualizar docente"))
        self.actionEliminar_docente.setText(_translate("Form", "Eliminar docente"))
