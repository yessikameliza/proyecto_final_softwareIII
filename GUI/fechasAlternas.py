# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\fechasAlternas.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from logica.Persistence import obtener_fecha


class FechasAlternas(object):
    def setup_ui(self, form):
        form.setObjectName("Form")
        form.resize(906, 405)
        form.setStyleSheet("background-color: rgb(128, 195, 161)")
        self.label_6 = QtWidgets.QLabel(form)
        self.label_6.setGeometry(QtCore.QRect(690, 90, 200, 30))
        self.label_6.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                   "color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.tablewidgetfechasalternas = QtWidgets.QTableWidget(form)
        self.tablewidgetfechasalternas.setGeometry(QtCore.QRect(30, 120, 851, 211))
        self.tablewidgetfechasalternas.setStyleSheet("font: 9pt \"Segoe Print\";\n"
                                                     "color: rgb(0, 0, 0);\n"
                                                     "background-color: rgb(255, 255, 255);")
        self.tablewidgetfechasalternas.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tablewidgetfechasalternas.setObjectName("tableWidgetFechasAlternas")
        self.tablewidgetfechasalternas.setColumnCount(6)
        self.tablewidgetfechasalternas.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(4, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidgetfechasalternas.setItem(5, 5, item)
        self.tablewidgetfechasalternas.horizontalHeader().setDefaultSectionSize(137)
        self.label_4 = QtWidgets.QLabel(form)
        self.label_4.setGeometry(QtCore.QRect(420, 90, 200, 30))
        self.label_4.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                   "color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(form)
        self.label_5.setGeometry(QtCore.QRect(370, 20, 261, 41))
        self.label_5.setStyleSheet("font: 75 20pt \"Segoe Print\";\n"
                                   "color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.btnver = QtWidgets.QPushButton(form)
        self.btnver.setGeometry(QtCore.QRect(380, 350, 181, 41))
        self.btnver.setStyleSheet("font: 11pt \"Segoe Print\";\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color: rgb(0, 51, 51);\n"
                                  "")
        self.btnver.setObjectName("btnVer")
        self.label_3 = QtWidgets.QLabel(form)
        self.label_3.setGeometry(QtCore.QRect(140, 90, 200, 30))
        self.label_3.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        self.retranslate_ui(form)
        self.btnver.clicked.connect(self.mostrar)
        QtCore.QMetaObject.connectSlotsByName(form)

    def mostrar(self):
        self.tabla1()

    def tabla1(self):
        res = obtener_fecha("Fechas alternas")
        print(res, "prueba")
        col: int = 0
        rows: int = 0
        for it in res:
            print(it, "fechas ver")
            item = self.tablewidgetfechasalternas.item(rows, col)
            item.setText(it)
            print("rows", rows, "col ", col)
            if 5 == rows:
                col = col + 1
                rows = -1
            rows = rows + 1

    def retranslate_ui(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">BLOQUE C</span></p></body></html>"))
        item = self.tablewidgetfechasalternas.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tablewidgetfechasalternas.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tablewidgetfechasalternas.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tablewidgetfechasalternas.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.tablewidgetfechasalternas.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.tablewidgetfechasalternas.verticalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.tablewidgetfechasalternas.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Encuentros Tutoriales"))
        item = self.tablewidgetfechasalternas.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Habilitaciones"))
        item = self.tablewidgetfechasalternas.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Encuentros Tutoriales"))
        item = self.tablewidgetfechasalternas.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Habilitaciones"))
        item = self.tablewidgetfechasalternas.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Encuentros Tutoriales"))
        item = self.tablewidgetfechasalternas.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Habilitaciones"))
        __sortingenabled = self.tablewidgetfechasalternas.isSortingEnabled()
        self.tablewidgetfechasalternas.setSortingEnabled(False)
        item = self.tablewidgetfechasalternas.item(0, 0)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(0, 1)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(0, 2)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(0, 3)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(0, 4)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(0, 5)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(1, 0)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(1, 1)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(1, 2)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(1, 3)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(1, 4)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(1, 5)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(2, 0)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(2, 1)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(2, 2)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(2, 3)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(2, 4)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(2, 5)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(3, 0)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(3, 1)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(3, 2)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(3, 3)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(3, 4)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(3, 5)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(4, 0)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(4, 1)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(4, 2)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(4, 3)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(4, 4)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(4, 5)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(5, 0)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(5, 1)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(5, 2)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(5, 3)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(5, 4)
        item.setText(_translate("Form", "0"))
        item = self.tablewidgetfechasalternas.item(5, 5)
        item.setText(_translate("Form", "0"))
        self.tablewidgetfechasalternas.setSortingEnabled(__sortingenabled)
        self.label_4.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">BLOQUE B</span></p></body></html>"))
        self.label_5.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">Fechas alternas</span></p></body></html>"))
        self.btnver.setText(_translate("Form", "VER"))
        self.label_3.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">BLOQUE A</span></p></body></html>"))
