# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\registroFechas.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from logica.Persistence import register_Date
from logica.Persistence import delete_Date
from PyQt5.QtWidgets import QMessageBox


class Ui_Form(object):
    message_box: QMessageBox

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1379, 743)
        Form.setStyleSheet("background-color: rgb(0, 51, 51)")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(60, 120, 1211, 571))
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 9pt \"Segoe Print\";\n"
                                    "")
        self.groupBox.setObjectName("groupBox")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_3.setGeometry(QtCore.QRect(120, 390, 851, 161))
        self.tableWidget_3.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(255, 255, 255);")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(6)
        self.tableWidget_3.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(4, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(5, 5, item)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(136)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 110, 111, 21))
        self.label_6.setStyleSheet("font: 75 11pt \"Segoe Print\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 130, 91, 21))
        self.label_7.setStyleSheet("font: 75 11pt \"Segoe Print\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 300, 91, 21))
        self.label_8.setStyleSheet("font: 75 11pt \"Segoe Print\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(20, 320, 91, 21))
        self.label_9.setStyleSheet("font: 75 11pt \"Segoe Print\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(120, 50, 851, 161))
        self.tableWidget.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       "background-color: rgb(255, 255, 255);")
        self.tableWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(137)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(250, 20, 121, 16))
        self.label.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                 "color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(500, 20, 121, 16))
        self.label_2.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(740, 20, 121, 16))
        self.label_3.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(20, 450, 91, 21))
        self.label_10.setStyleSheet("font: 75 11pt \"Segoe Print\";\n"
                                    "color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(20, 470, 91, 21))
        self.label_11.setStyleSheet("font: 75 11pt \"Segoe Print\";\n"
                                    "color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(990, 130, 191, 301))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 70, 171, 51))
        self.pushButton.setStyleSheet("background-color: rgb(0, 204, 102);\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 210, 171, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 204, 102);\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 140, 171, 51))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 204, 102);\n"
                                        "")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(480, 70, 251, 41))
        self.label_4.setStyleSheet("font: 75 20pt \"Segoe Print\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(380, 30, 501, 41))
        self.label_5.setStyleSheet("font: 75 20pt \"Segoe Print\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        self.tableWidget_2.setGeometry(QtCore.QRect(180, 340, 851, 161))
        self.tableWidget_2.setStyleSheet("font: 9pt \"Segoe Print\";\n"
                                         "color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(255, 255, 255);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(5, 5, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(137)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.registrarFechas)
        self.pushButton_3.clicked.connect(self.eliminarFechas)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def registrarFechas(self):
        self.tabla1(0)
        self.tabla1(1)
        self.tabla1(2)
        self.tabla1(3)
        self.tabla1(4)
        self.tabla1(5)
        self.tabla2(0)
        self.tabla2(1)
        self.tabla2(2)
        self.tabla2(3)
        self.tabla2(4)
        self.tabla2(5)
        self.tabla3(0)
        self.tabla3(1)
        self.tabla3(2)
        self.tabla3(3)
        self.tabla3(4)
        self.tabla3(5)
        self.mostrarMensaje("Información", "¡Fechas registradas exitosamente!", "", QMessageBox.Warning, False)

    def tabla1(self, column):

        for row in range(self.tableWidget.rowCount()):
            text = self.tableWidget.item(row, column).text()

            print(column, "colun")
            if column == 0 or column == 2 or column == 4:
                register_Date(text, "Encuentros tutoriales", "Primeras fechas")
            else:
                register_Date(text, "Habilitaciones", "Primeras fechas")

    def tabla2(self, column):

        for row2 in range(self.tableWidget_2.rowCount()):
            text2 = self.tableWidget_2.item(row2, column).text()
            if column == 0 or column == 2 or column == 4:
                register_Date(text2, "Encuentros tutoriales", "Fechas alternas")
            else:
                register_Date(text2, "Habilitaciones", "Fechas alternas")

    def tabla3(self, column):
        for row3 in range(self.tableWidget_3.rowCount()):
            text3 = self.tableWidget_3.item(row3, column).text()

            if column == 0 or column == 2 or column == 4:
                 register_Date(text3, "Encuentros tutoriales", "Pereira domingos")
            else:
                 register_Date(text3, "Habilitaciones", "Pereira domingos")

    def eliminarFechas(self):
        delete_Date()
        self.tableWidget.clear()
        self.tableWidget_2.clear()
        self.tableWidget_3.clear()
        self.mostrarMensaje("Información", "¡Fechas eliminadas!", "", QMessageBox.Warning, False)

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
        self.groupBox.setTitle(_translate("Form", "FECHAS"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget_3.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget_3.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget_3.verticalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Encuentros Tutoriales"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Habilitaciones"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Encuentros Tutoriales"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Habilitaciones"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Encuentros Tutoriales"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Habilitaciones"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        item = self.tableWidget_3.item(0, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(0, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(0, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(0, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(0, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(0, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(1, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(1, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(1, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(1, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(1, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(1, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(2, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(2, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(2, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(2, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(2, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(2, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(3, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(3, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(3, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(3, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(3, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(3, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(4, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(4, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(4, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(4, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(4, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(4, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(5, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(5, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(5, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(5, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(5, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_3.item(5, 5)
        item.setText(_translate("Form", "0"))
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(_translate("Form", "PRIMERAS"))
        self.label_7.setText(_translate("Form", "FECHAS"))
        self.label_8.setText(_translate("Form", "FECHAS"))
        self.label_9.setText(_translate("Form", "ALTERNAS"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Encuentros Tutoriales"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Habilitaciones"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Encuentros Tutoriales"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Habilitaciones"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Encuentros Tutoriales"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Habilitaciones"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(1, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(2, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(2, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(3, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(3, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(4, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(4, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(4, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(5, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(5, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(5, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget.item(5, 5)
        item.setText(_translate("Form", "0"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Form", "BLOQUE A"))
        self.label_2.setText(_translate("Form", "BLOQUE B"))
        self.label_3.setText(_translate("Form", "BLOQUE C"))
        self.label_10.setText(_translate("Form", "PEREIRA"))
        self.label_11.setText(_translate("Form", "DOMINGOS"))
        self.groupBox_2.setTitle(_translate("Form", "OPCIONES"))
        self.pushButton.setText(_translate("Form", "REGISTRAR FECHAS"))
        self.pushButton_2.setText(_translate("Form", "ELIMINAR FECHAS"))
        self.pushButton_3.setText(_translate("Form", "ACTUALIZAR FECHAS"))
        self.label_4.setText(_translate("Form", "Registro de fechas"))
        self.label_5.setText(_translate("Form", "Programación encuentros tutoriales"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Encuentros Tutoriales"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Habilitaciones"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Encuentros Tutoriales"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Habilitaciones"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Encuentros Tutoriales"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Habilitaciones"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(0, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(0, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(0, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(0, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(0, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(1, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(1, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(1, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(1, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(1, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(1, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(2, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(2, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(2, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(2, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(2, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(2, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(3, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(3, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(3, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(3, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(3, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(3, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(4, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(4, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(4, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(4, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(4, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(4, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(5, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(5, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(5, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(5, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(5, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidget_2.item(5, 5)
        item.setText(_translate("Form", "0"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
