import sys
import typing #Verificar o que aparece no QtDesigner

from PyQt5.QtGui import QIcon #Biblioteca para usar ícones
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication, QMainWindow #Biblioteca para mostrar pop-ups

from PyQt5 import QtWidgets, QtCore

from cadastro_evento_Import import *

class Main_Master_evento(QMainWindow, Ui_MainWindow):
    def __init__(self)->None:
        super(Main_Master_evento, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # self.pushButton_3.clicked.connect(self.logar)
        self.pushButton_2.clicked.connect(self.close)

        self.close()

        

if __name__=="__main__":
    app = QApplication(sys.argv)
    tela_login = Main_Master_evento()
    tela_login.show()
    app.exec()

