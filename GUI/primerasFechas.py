# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alexander\Documents\primerasFechas.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from logica.Persistence import obtener_Fecha


class PrimerasFechas(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(926, 440)
        Form.setStyleSheet("background-color: rgb(0, 51, 51)")
        self.tableWidgetPrimerasFechas = QtWidgets.QTableWidget(Form)
        self.tableWidgetPrimerasFechas.setGeometry(QtCore.QRect(40, 130, 851, 211))
        self.tableWidgetPrimerasFechas.setStyleSheet("font: 9pt \"Segoe Print\";\n"
                                                     "color: rgb(0, 0, 0);\n"
                                                     "background-color: rgb(255, 255, 255);")
        self.tableWidgetPrimerasFechas.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableWidgetPrimerasFechas.setObjectName("tableWidgetPrimerasFechas")
        self.tableWidgetPrimerasFechas.setColumnCount(6)
        self.tableWidgetPrimerasFechas.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(4, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPrimerasFechas.setItem(5, 5, item)
        self.tableWidgetPrimerasFechas.horizontalHeader().setDefaultSectionSize(137)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(340, 30, 261, 41))
        self.label_5.setStyleSheet("font: 75 20pt \"Segoe Print\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 100, 121, 16))
        self.label_3.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(430, 100, 121, 16))
        self.label_4.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(710, 100, 121, 16))
        self.label_6.setStyleSheet("font: 75 12pt \"Segoe Print\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.btnVer = QtWidgets.QPushButton(Form)
        self.btnVer.setGeometry(QtCore.QRect(390, 370, 181, 41))
        self.btnVer.setStyleSheet("font: 11pt \"Segoe Print\";\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color: rgb(0, 204, 102);\n"
                                  "")
        self.btnVer.setObjectName("btnVer")

        self.retranslateUi(Form)
        self.btnVer.clicked.connect(self.mostrar)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def mostrar(self):
        self.tabla1()

    def tabla1(self):
        res = obtener_Fecha("Primeras fechas")

        print(res)
        col: int = 0
        rows: int = 0
        for it in res:
            item = self.tableWidgetPrimerasFechas.item(rows, col)
            item.setText(it)
            print("rows", rows, "col ", col)
            if 5 == rows:
                col = col + 1
                rows = -1
            rows = rows + 1


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidgetPrimerasFechas.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidgetPrimerasFechas.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidgetPrimerasFechas.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableWidgetPrimerasFechas.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.tableWidgetPrimerasFechas.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.tableWidgetPrimerasFechas.verticalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.tableWidgetPrimerasFechas.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Encuentros Tutoriales"))
        item = self.tableWidgetPrimerasFechas.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Habilitaciones"))
        item = self.tableWidgetPrimerasFechas.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Encuentros Tutoriales"))
        item = self.tableWidgetPrimerasFechas.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Habilitaciones"))
        item = self.tableWidgetPrimerasFechas.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Encuentros Tutoriales"))
        item = self.tableWidgetPrimerasFechas.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Habilitaciones"))
        __sortingEnabled = self.tableWidgetPrimerasFechas.isSortingEnabled()
        self.tableWidgetPrimerasFechas.setSortingEnabled(False)
        item = self.tableWidgetPrimerasFechas.item(0, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(0, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(0, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(0, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(0, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(0, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(1, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(1, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(1, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(1, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(1, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(1, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(2, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(2, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(2, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(2, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(2, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(2, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(3, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(3, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(3, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(3, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(3, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(3, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(4, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(4, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(4, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(4, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(4, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(4, 5)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(5, 0)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(5, 1)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(5, 2)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(5, 3)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(5, 4)
        item.setText(_translate("Form", "0"))
        item = self.tableWidgetPrimerasFechas.item(5, 5)
        item.setText(_translate("Form", "0"))
        self.tableWidgetPrimerasFechas.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("Form", "Primeras fechas"))
        self.label_3.setText(_translate("Form", "BLOQUE A"))
        self.label_4.setText(_translate("Form", "BLOQUE B"))
        self.label_6.setText(_translate("Form", "BLOQUE C"))
        self.btnVer.setText(_translate("Form", "VER"))
