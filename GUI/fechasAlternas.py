# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\fechasAlternas.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from logica.Persistence import obtener_fecha
class FechasAlternas(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(906, 405)
        Form.setStyleSheet("background-color: rgb(128, 195, 161)")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(690, 90, 200, 30))
        self.label_6.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
"color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.tableWidgetFechasAlternas = QtWidgets.QTableWidget(Form)
        self.tableWidgetFechasAlternas.setGeometry(QtCore.QRect(30, 120, 851, 211))
        self.tableWidgetFechasAlternas.setStyleSheet("font: 9pt \"Segoe Print\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidgetFechasAlternas.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableWidgetFechasAlternas.setObjectName("tableWidgetFechasAlternas")
        self.tableWidgetFechasAlternas.setColumnCount(6)
        self.tableWidgetFechasAlternas.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(4, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFechasAlternas.setItem(5, 5, item)
        self.tableWidgetFechasAlternas.horizontalHeader().setDefaultSectionSize(137)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(420, 90, 200, 30))
        self.label_4.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
"color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(370, 20, 261, 41))
        self.label_5.setStyleSheet("font: 75 20pt \"Segoe Print\";\n"
"color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.btnVer = QtWidgets.QPushButton(Form)
        self.btnVer.setGeometry(QtCore.QRect(380, 350, 181, 41))
        self.btnVer.setStyleSheet("font: 11pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 51, 51);\n"
"")
        self.btnVer.setObjectName("btnVer")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 90, 200, 30))
        self.label_3.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        self.btnVer.clicked.connect(self.mostrar)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def mostrar(self):
        self.tabla1()

    def tabla1(self):
        res = obtener_fecha("Fechas alternas")
        col: int = 0
        rows: int = 0
        for it in res:
            print(it, "fechas ver")
            item = self.tableWidgetFechasAlternas.item(rows, col)
            item.setText(it)
            print("rows", rows, "col ", col)
            if 5 == rows:
                col = col + 1
                rows = -1
            rows = rows + 1

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">BLOQUE C</span></p></body></html>"))
        item = self.tableWidgetFechasAlternas.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidgetFechasAlternas.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidgetFechasAlternas.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableWidgetFechasAlternas.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.tableWidgetFechasAlternas.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.tableWidgetFechasAlternas.verticalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.tableWidgetFechasAlternas.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Encuentros Tutoriales"))
        item = self.tableWidgetFechasAlternas.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Habilitaciones"))
        item = self.tableWidgetFechasAlternas.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Encuentros Tutoriales"))
        item = self.tableWidgetFechasAlternas.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Habilitaciones"))
        item = self.tableWidgetFechasAlternas.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Encuentros Tutoriales"))
        item = self.tableWidgetFechasAlternas.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Habilitaciones"))
        __sortingEnabled = self.tableWidgetFechasAlternas.isSortingEnabled()
        self.tableWidgetFechasAlternas.setSortingEnabled(False)
        item = self.tableWidgetFechasAlternas.item(0, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(0, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(0, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(0, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(0, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(0, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(1, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(1, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(1, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(1, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(1, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(1, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(2, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(2, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(2, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(2, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(2, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(2, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(3, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(3, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(3, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(3, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(3, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(3, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(4, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(4, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(4, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(4, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(4, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(4, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(5, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(5, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(5, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(5, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(5, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetFechasAlternas.item(5, 5)
        item.setText(_translate("Form", "0"))
        self.tableWidgetFechasAlternas.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">BLOQUE B</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">Fechas alternas</span></p></body></html>"))
        self.btnVer.setText(_translate("Form", "VER"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">BLOQUE A</span></p></body></html>"))

