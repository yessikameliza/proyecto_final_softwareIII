
from PyQt5.QtWidgets import QApplication, QMainWindow

from GUI.login import Login
if __name__ == "__main__":
    app = QApplication([])
    hola = QMainWindow()
    main_window = Login()
    main_window.setupUi(hola)
    hola.show()
    app.exec_()

