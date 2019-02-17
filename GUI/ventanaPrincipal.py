# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\ventanaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from GUI.registroFechas import RegistroFechas
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
from logica.Persistence import obtener_datos_profe


class VentanaPrincipal(QtWidgets.QMainWindow):

    def setup_ui(self, form):
        form.setObjectName("Form")
        form.resize(1267, 854)
        form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(form)
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
        sizepolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizepolicy.setHorizontalStretch(10)
        sizepolicy.setVerticalStretch(11)
        sizepolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizepolicy)
        self.frame_3.setStyleSheet("background-color: rgb(128, 195, 161);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.groupbox = QtWidgets.QGroupBox(self.frame_3)
        self.groupbox.setGeometry(QtCore.QRect(20, 10, 311, 381))
        self.groupbox.setStyleSheet("font: 75 14pt \"Segoe Print\";\n"
                                    "color: rgb(0, 0, 0);")
        self.groupbox.setObjectName("groupBox")

        self.btnregistrardocentes = QtWidgets.QPushButton(self.groupbox)
        self.btnregistrardocentes.setGeometry(QtCore.QRect(40, 40, 241, 31))
        self.btnregistrardocentes.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "background-color: rgb(0, 51, 51);\n"
                                                "")
        self.btnregistrardocentes.setObjectName("btnRegistrarDocentes")

        self.btnregistrarfechas = QtWidgets.QPushButton(self.groupbox)
        self.btnregistrarfechas.setGeometry(QtCore.QRect(40, 122, 241, 31))
        self.btnregistrarfechas.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "background-color: rgb(0, 51, 51);\n"
                                              "")
        self.btnregistrarfechas.setObjectName("btnRegistrarFechas")
        self.groupbox_3 = QtWidgets.QGroupBox(self.groupbox)
        self.groupbox_3.setGeometry(QtCore.QRect(20, 160, 271, 191))
        self.groupbox_3.setStyleSheet("font: 75 14pt \"Segoe Print\";")
        self.groupbox_3.setObjectName("groupBox_3")
        self.btngenerarhorarmen = QtWidgets.QPushButton(self.groupbox_3)
        self.btngenerarhorarmen.setGeometry(QtCore.QRect(20, 110, 241, 31))
        self.btngenerarhorarmen.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "background-color: rgb(0, 51, 51);\n"
                                              "\n"
                                              "")
        self.btngenerarhorarmen.setObjectName("btnGenerarHorArmen")
        self.btngenerarhorper = QtWidgets.QPushButton(self.groupbox_3)
        self.btngenerarhorper.setGeometry(QtCore.QRect(20, 150, 241, 31))
        self.btngenerarhorper.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "background-color: rgb(0, 51, 51);\n"
                                            "\n"
                                            "")
        self.btngenerarhorper.setObjectName("btnGenerarHorPer")
        self.btngenerarhorbuga = QtWidgets.QPushButton(self.groupbox_3)
        self.btngenerarhorbuga.setGeometry(QtCore.QRect(20, 70, 241, 31))
        self.btngenerarhorbuga.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "background-color: rgb(0, 51, 51);\n"
                                             "\n"
                                             "")
        self.btngenerarhorbuga.setObjectName("btnGenerarHorBuga")
        self.label_4 = QtWidgets.QLabel(self.groupbox_3)
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
        self.spinsemestre = QtWidgets.QSpinBox(self.groupbox_3)
        self.spinsemestre.setGeometry(QtCore.QRect(190, 40, 71, 22))
        self.spinsemestre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "color: rgb(0, 0, 0);")
        self.spinsemestre.setMinimum(1)
        self.spinsemestre.setMaximum(6)
        self.spinsemestre.setProperty("value", 1)
        self.spinsemestre.setObjectName("spinSemestre")
        self.groupbox_4 = QtWidgets.QGroupBox(self.frame_3)
        self.groupbox_4.setGeometry(QtCore.QRect(370, 10, 861, 381))
        self.groupbox_4.setStyleSheet("font: 75 14pt \"Segoe Print\";\n"
                                      "color: rgb(0, 0, 0);")
        self.groupbox_4.setObjectName("groupBox_4")
        self.tablahorario = QtWidgets.QTableWidget(self.groupbox_4)
        self.tablahorario.setGeometry(QtCore.QRect(30, 30, 731, 331))
        self.tablahorario.setSizeIncrement(QtCore.QSize(15, 8))
        self.tablahorario.setBaseSize(QtCore.QSize(22, 18))
        self.tablahorario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 75 9pt \"Segoe Print\";\n"
                                        "color: rgb(0, 0, 0);")
        self.tablahorario.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tablahorario.setLineWidth(2)
        self.tablahorario.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tablahorario.setIconSize(QtCore.QSize(19, 6))
        self.tablahorario.setShowGrid(True)
        self.tablahorario.setGridStyle(QtCore.Qt.SolidLine)
        self.tablahorario.setWordWrap(True)
        self.tablahorario.setCornerButtonEnabled(True)
        self.tablahorario.setObjectName("tablaHorario")
        self.tablahorario.setColumnCount(3)
        self.tablahorario.setRowCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablahorario.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablahorario.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablahorario.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(9, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(10, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(11, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablahorario.setItem(11, 2, item)

        self.tablahorario.horizontalHeader().setDefaultSectionSize(256)
        self.tablahorario.horizontalHeader().setMinimumSectionSize(50)
        self.tablahorario.verticalHeader().setDefaultSectionSize(55)
        self.btnimprimir = QtWidgets.QPushButton(self.groupbox_4)
        self.btnimprimir.setGeometry(QtCore.QRect(770, 170, 81, 41))
        self.btnimprimir.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(0, 51, 51);\n"
                                       "\n""")

        self.btnimprimir.setObjectName("btnImprimir")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 120, 1411, 151))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.groupbox_2 = QtWidgets.QGroupBox(self.frame_2)
        self.groupbox_2.setGeometry(QtCore.QRect(60, 10, 1171, 141))
        self.groupbox_2.setStyleSheet("\n"
                                      "font: 75 12pt \"Segoe Print\";")
        self.groupbox_2.setObjectName("groupBox_2")
        self.tablainfoacademica = QtWidgets.QTableWidget(self.groupbox_2)
        self.tablainfoacademica.setGeometry(QtCore.QRect(60, 30, 1061, 101))
        sizepolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizepolicy.setHorizontalStretch(40)
        sizepolicy.setVerticalStretch(19)
        sizepolicy.setHeightForWidth(self.tablainfoacademica.sizePolicy().hasHeightForWidth())
        self.tablainfoacademica.setSizePolicy(sizepolicy)
        self.tablainfoacademica.setStyleSheet("")
        self.tablainfoacademica.setObjectName("tablaInfoAcademica")
        self.tablainfoacademica.setColumnCount(5)
        self.tablainfoacademica.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablainfoacademica.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.tablainfoacademica.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablainfoacademica.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablainfoacademica.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablainfoacademica.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablainfoacademica.setItem(3, 4, item)
        self.tablainfoacademica.horizontalHeader().setDefaultSectionSize(207)
        self.tablainfoacademica.horizontalHeader().setMinimumSectionSize(46)
        self.tablainfoacademica.verticalHeader().setDefaultSectionSize(26)
        form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1267, 21))
        self.menubar.setObjectName("menubar")
        self.menuopciones = QtWidgets.QMenu(self.menubar)
        self.menuopciones.setObjectName("menuOpciones")
        self.menuasignaturas = QtWidgets.QMenu(self.menubar)
        self.menuasignaturas.setObjectName("menuAsignaturas")
        self.menudocentes = QtWidgets.QMenu(self.menubar)
        self.menudocentes.setObjectName("menuDocentes")
        form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(form)
        self.statusbar.setObjectName("statusbar")
        form.setStatusBar(self.statusbar)
        self.actionRegistrar_espacios_fisicos = QtWidgets.QAction(form)
        self.actionRegistrar_espacios_fisicos.setWhatsThis("")
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionRegistrar_espacios_fisicos.setFont(font)
        self.actionRegistrar_espacios_fisicos.setAutoRepeat(False)
        self.actionRegistrar_espacios_fisicos.setIconVisibleInMenu(False)
        self.actionRegistrar_espacios_fisicos.setObjectName("actionRegistrar_espacios_fisicos")
        self.actionRegistrar_docentes = QtWidgets.QAction(form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionRegistrar_docentes.setFont(font)
        self.actionRegistrar_docentes.setObjectName("actionRegistrar_docentes")
        self.actionRegistro_intensidad_horaria = QtWidgets.QAction(form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionRegistro_intensidad_horaria.setFont(font)
        self.actionRegistro_intensidad_horaria.setObjectName("actionRegistro_intensidad_horaria")
        self.actionGenerar_reportes = QtWidgets.QAction(form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionGenerar_reportes.setFont(font)
        self.actionGenerar_reportes.setObjectName("actionGenerar_reportes")
        self.actionRegistrar_Asignaturas = QtWidgets.QAction(form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionRegistrar_Asignaturas.setFont(font)
        self.actionRegistrar_Asignaturas.setObjectName("actionRegistrar_Asignaturas")
        self.actionRegistrar_Asignaturas_2 = QtWidgets.QAction(form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionRegistrar_Asignaturas_2.setFont(font)
        self.actionRegistrar_Asignaturas_2.setObjectName("actionRegistrar_Asignaturas_2")
        self.actionModificar_Asignaturas = QtWidgets.QAction(form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionModificar_Asignaturas.setFont(font)
        self.actionModificar_Asignaturas.setObjectName("actionModificar_Asignaturas")
        self.actionEliminar_Asignaturas = QtWidgets.QAction(form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionEliminar_Asignaturas.setFont(font)
        self.actionEliminar_Asignaturas.setObjectName("actionEliminar_Asignaturas")
        self.actionVer_fechas_alternas = QtWidgets.QAction(form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionVer_fechas_alternas.setFont(font)
        self.actionVer_fechas_alternas.setObjectName("actionVer_fechas_alternas")

        self.actionVer_fechas_pereira = QtWidgets.QAction(form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionVer_fechas_pereira.setFont(font)
        self.actionVer_fechas_pereira.setObjectName("actionVer_fechas_pereira")

        self.actionActualizar_Docente = QtWidgets.QAction(form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionActualizar_Docente.setFont(font)
        self.actionActualizar_Docente.setObjectName("actionActualizar_Docente")
        self.actionEliminar_docente = QtWidgets.QAction(form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.actionEliminar_docente.setFont(font)
        self.actionEliminar_docente.setObjectName("actionEliminar_docente")
        self.menuopciones.addSeparator()
        self.menuopciones.addAction(self.actionGenerar_reportes)
        self.menuopciones.addAction(self.actionVer_fechas_alternas)
        self.menuopciones.addAction(self.actionVer_fechas_pereira)
        self.menuasignaturas.addAction(self.actionRegistrar_Asignaturas_2)
        self.menuasignaturas.addAction(self.actionModificar_Asignaturas)
        self.menuasignaturas.addAction(self.actionEliminar_Asignaturas)
        self.menudocentes.addAction(self.actionActualizar_Docente)
        self.menudocentes.addAction(self.actionEliminar_docente)
        self.menubar.addAction(self.menuopciones.menuAction())
        self.menubar.addAction(self.menuasignaturas.menuAction())
        self.menubar.addAction(self.menudocentes.menuAction())
        self.retranslate_ui(form)
        self.btnregistrardocentes.clicked.connect(self.ventana_registro_docente)
        self.btnregistrarfechas.clicked.connect(self.ventana_registro_fecha)
        self.actionRegistrar_Asignaturas_2.triggered.connect(self.ventana_reg_asi)
        self.actionModificar_Asignaturas.triggered.connect(self.ventana_mod_asig)
        self.actionEliminar_Asignaturas.triggered.connect(self.ventana_elim_asig)
        self.actionActualizar_Docente.triggered.connect(self.ventana_act_doc)
        self.actionEliminar_docente.triggered.connect(self.ventana_elim_doc)
        self.actionGenerar_reportes.triggered.connect(self.ventana_primeras_fecha)
        self.actionVer_fechas_alternas.triggered.connect(self.ventana_fechas_alternas)
        self.actionVer_fechas_pereira.triggered.connect(self.ventana_fechas_pereira)
        self.btngenerarhorarmen.clicked.connect(self.prueba_horario)
        self.btngenerarhorbuga.clicked.connect(self.prueba_horario2)
        self.btngenerarhorper.clicked.connect(self.prueba_horario3)
        QtCore.QMetaObject.connectSlotsByName(form)

    def ventana_fechas_pereira(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = FechasPereira()
        self.ui.setup_ui(self.ventana)
        self.ventana.show()

    def ventana_registro_docente(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = RegistroDocentes()
        self.ui.setup_ui(self.ventana)
        self.ventana.show()


    def ventana_registro_fecha(self):

        self.ventana = QtWidgets.QMainWindow()
        self.ui = RegistroFechas()
        self.ui.setup_ui(self.ventana)
        self.ventana.show()
        self.close()

    def ventana_reg_asi(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = RegistroAsignaturas()
        self.ui.setup_ui(self.ventana)
        self.ventana.show()

    def ventana_mod_asig(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = ActualizarAsignatura()
        self.ui.setup_ui(self.ventana)
        self.ventana.show()

    def ventana_elim_asig(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = EliminarAsignatura()
        self.ui.setup_ui(self.ventana)
        self.ventana.show()

    def ventana_act_doc(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = ActualizarDocente()
        self.ui.setup_ui(self.ventana)
        self.ventana.show()

    def ventana_elim_doc(self):
         self.ventana = QtWidgets.QMainWindow()
         self.ui = EliminarDocente()
         self.ui.setup_ui(self.ventana)
         self.ventana.show()


    def ventana_primeras_fecha(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = PrimerasFechas()
        self.ui.setup_ui(self.ventana)
        self.ventana.show()

    def ventana_fechas_alternas(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = FechasAlternas()
        self.ui.setup_ui(self.ventana)
        self.ventana.show()

    def setear_tabla(self):
        i = 0
        j = 0
        while j < 3:
            while i < 12:
                item = self.tablahorario.item(i, j)
                item.setText("")
                i = i + 1
            j = j + 1
            i = 0

    def llenartabla(self, semester, city):
        s: list = obtener_datos_profe(semester, city)
        rows: int = 0
        col: int = 0
        for i in s:
            for j in i:
                print(j, "contenidoo")
                print(rows, col)
                item = self.tablainfoacademica.item(rows, col)
                item.setText(str(j))

                if col < 4:
                    print(rows, col)
                    col = col + 1
                else:
                    rows = rows + 1
                    col = 0

    def prueba_horario(self):
        self.setear_tabla()
        semester: int = int(self.spinsemestre.text())
        print("este es el semestre", semester)
        hours: list = gene_hours(semester, "Armenia")
        print("probando esto")
        self.llenartabla(semester, "Armenia")
        rows = 1
        i = 0
        if semester == 1:
            i = 4
            dateinduc: list = obtener_f_induct("inductorio")
            item = self.tablahorario.item(0, 0)
            item.setText((dateinduc[0])[1])
            item = self.tablahorario.item(2, 0)
            item.setText((dateinduc[1])[1])
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
                item = self.tablahorario.item(i, 0)
                item.setText(d[1])
            elif d[3] == 2:
                n = 2
                item = self.tablahorario.item(i, 1)
                item.setText(d[1])
            elif d[3] == 3:
                n = 3
                item = self.tablahorario.item(i, 2)
                item.setText(d[1])
            i = i + 2
        for h in hours:
            if h[1] != o:
                rows = 1
            if h[1] == 1:
                item = self.tablahorario.item(rows, 0)
                item.setText(h[0])
            elif h[1] == 2:
                o = 2
                item = self.tablahorario.item(rows, 1)
                item.setText(h[0])
            elif h[1] == 3:
                o = 3
                item = self.tablahorario.item(rows, 2)
                item.setText(h[0])
            rows = rows + 2
            print(rows)

    def prueba_horario2(self):
        self.setear_tabla()
        semester: int = int(self.spinsemestre.text())
        hours: list = gene_hours(semester, "Armenia")
        self.llenartabla(semester, "Buga")
        rows = 1
        i = 0
        if semester == 1:
            i = 4
            dateinduc: list = obtener_f_induct("inductorio")
            item = self.tablahorario.item(0, 0)
            item.setText((dateinduc[0])[1])
            item = self.tablahorario.item(2, 0)
            item.setText((dateinduc[1])[1])
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
                item = self.tablahorario.item(i, 0)
                item.setText(d[1])
            elif d[3] == 2:
                n = 2
                item = self.tablahorario.item(i, 1)
                item.setText(d[1])
            elif d[3] == 3:
                n = 3
                item = self.tablahorario.item(i, 2)
                item.setText(d[1])
            i = i + 2
        for h in hours:
            if h[1] != o:
                rows = 1
            if h[1] == 1:
                item = self.tablahorario.item(rows, 0)
                item.setText(h[0])
            elif h[1] == 2:
                o = 2
                item = self.tablahorario.item(rows, 1)
                item.setText(h[0])
            elif h[1] == 3:
                o = 3
                item = self.tablahorario.item(rows, 2)
                item.setText(h[0])
            rows = rows + 2
            print(rows)

    def prueba_horario3(self):
        self.setear_tabla()
        semester: int = int(self.spinsemestre.text())
        hours: list = gene_hours(semester, "Armenia")
        self.llenartabla(semester, "Pereira")
        rows = 1
        i = 0
        if semester == 1:
            i = 4
            dateinduc: list = obtener_f_induct("inductorio")
            item = self.tablahorario.item(0, 0)
            item.setText((dateinduc[0])[1])
            item = self.tablahorario.item(2, 0)
            item.setText((dateinduc[1])[1])
        else:
            i = 0
        n = 1
        o = 1
        date: list = obtener_fechas_p("Fechas alternas", "Encuentros tutoriales")
        for d in date:
            if d[3] != n:
                i = 0
            if d[3] == 1:
                item = self.tablahorario.item(i, 0)
                item.setText(d[1])
            elif d[3] == 2:
                n = 2
                item = self.tablahorario.item(i, 1)
                item.setText(d[1])
            elif d[3] == 3:
                n = 3
                item = self.tablahorario.item(i, 2)
                item.setText(d[1])
            i = i + 2
        for h in hours:
            if h[1] != o:
                rows = 1
            if h[1] == 1:
                item = self.tablahorario.item(rows, 0)
                item.setText(h[0])
            elif h[1] == 2:
                o = 2
                item = self.tablahorario.item(rows, 1)
                item.setText(h[0])
            elif h[1] == 3:
                o = 3
                item = self.tablahorario.item(rows, 2)
                item.setText(h[0])
            rows = rows + 2

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

    def retranslate_ui(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#000000;\">¡Bienvenido a SS MEWIN!</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#000000;\">Programador de horarios</span></p></body></html>"))
        self.groupbox.setTitle(_translate("Form", "Menú de opciones"))
        self.btnregistrardocentes.setText(_translate("Form", "Registrar Docentes"))
        self.btnregistrarfechas.setText(_translate("Form", "Registrar fechas"))
        self.groupbox_3.setTitle(_translate("Form", "Generar horario"))
        self.btngenerarhorarmen.setText(_translate("Form", "Generar horario Armenia"))
        self.btngenerarhorper.setText(_translate("Form", "Generar horario Pereira"))
        self.btngenerarhorbuga.setText(_translate("Form", "Generar horario Buga"))
        self.label_4.setText(_translate("Form", "Semestre a generar:"))
        self.groupbox_4.setTitle(_translate("Form", "Información de horario"))
        item = self.tablahorario.horizontalHeaderItem(0)
        item.setText(_translate("Form", "BLOQUE A"))
        item = self.tablahorario.horizontalHeaderItem(1)
        item.setText(_translate("Form", "BLOQUE B"))
        item = self.tablahorario.horizontalHeaderItem(2)
        item.setText(_translate("Form", "BLOQUE C"))
        __sortingenabled = self.tablahorario.isSortingEnabled()
        self.tablahorario.setSortingEnabled(False)
        item = self.tablahorario.item(0, 0)
        item.setText(_translate("Form", "Fecha 1"))
        item = self.tablahorario.item(0, 1)
        item.setText(_translate("Form", "Fecha 2"))
        item = self.tablahorario.item(0, 2)
        item.setText(_translate("Form", "Fecha 3"))
        item = self.tablahorario.item(2, 0)
        item.setText(_translate("Form", "Fecha 4"))
        item = self.tablahorario.item(2, 1)
        item.setText(_translate("Form", "Fecha 5"))
        item = self.tablahorario.item(2, 2)
        item.setText(_translate("Form", "Fecha 6"))
        item = self.tablahorario.item(4, 0)
        item.setText(_translate("Form", "Fecha 7"))
        item = self.tablahorario.item(4, 1)
        item.setText(_translate("Form", "Fecha 8"))
        item = self.tablahorario.item(4, 2)
        item.setText(_translate("Form", "Fecha 9"))
        item = self.tablahorario.item(6, 0)
        item.setText(_translate("Form", "Fecha 10"))
        item = self.tablahorario.item(6, 1)
        item.setText(_translate("Form", "Fecha 11"))
        item = self.tablahorario.item(6, 2)
        item.setText(_translate("Form", "Fecha 12"))
        item = self.tablahorario.item(8, 0)
        item.setText(_translate("Form", "Fecha 13"))
        item = self.tablahorario.item(8, 1)
        item.setText(_translate("Form", "Fecha 14"))
        item = self.tablahorario.item(8, 2)
        item.setText(_translate("Form", "Fecha 15"))
        item = self.tablahorario.item(10, 0)
        item.setText(_translate("Form", "Fecha 16"))
        item = self.tablahorario.item(10, 1)
        item.setText(_translate("Form", "Fecha 17"))
        item = self.tablahorario.item(10, 2)
        item.setText(_translate("Form", "Fecha 18"))
        self.tablahorario.setSortingEnabled(__sortingenabled)
        self.btnimprimir.setText(_translate("Form", "Imprimir"))
        self.groupbox_2.setTitle(_translate("Form", "Información "))
        item = self.tablainfoacademica.horizontalHeaderItem(0)
        item.setText(_translate("Form", "CÓDIGO"))
        item = self.tablainfoacademica.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ACTIVIDAD ACADÉMICA"))
        item = self.tablainfoacademica.horizontalHeaderItem(2)
        item.setText(_translate("Form", "REQUISITO"))
        item = self.tablainfoacademica.horizontalHeaderItem(3)
        item.setText(_translate("Form", "TUTOR"))
        item = self.tablainfoacademica.horizontalHeaderItem(4)
        item.setText(_translate("Form", "TELÉFONO"))
        self.menuopciones.setTitle(_translate("Form", "Reportes"))
        self.menuasignaturas.setTitle(_translate("Form", "Asignaturas"))
        self.menudocentes.setTitle(_translate("Form", "Docentes"))
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
