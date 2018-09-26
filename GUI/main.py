# coding: utf-8
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI.ventanaPrincipal import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication([])
    hola = QMainWindow()
    main_window = Ui_MainWindow()
    main_window.setupUi(hola)
    hola.show()
    app.exec_()

