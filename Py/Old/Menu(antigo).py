import sys
import typing #Verificar o que aparece no QtDesigner

from PyQt5.QtGui import QIcon #Biblioteca para usar ícones
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication, QMainWindow #Biblioteca para mostrar pop-ups

from PyQt5 import QtWidgets, QtCore

from Principal import *
from login_atualizado import Ui_login

class login_atualizado(QWidget, Ui_login):
    def __init__(self)->None:
        super(login_atualizado, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.setObjectName("Form")
        # self.resize(1032, 591)
        # self.widget = QtWidgets.QWidget(self)
        # self.widget.setGeometry(QtCore.QRect(29, 30, 941, 491))

        # self.pushButton3.clicked.connect(self.logar)
        # self.pushButton2.clicked.connect(self.fechar)

    def logar(self):
        codigo = self.lineEdit.text()
        pin = self.lineEdit_4.text()

        if codigo == "Pedro" and pin == "Pedro":
            self.carrega = TelaPrincipal() #Instancia a classe TelaExemplo
            self.carrega.show() #Chama a tela através da instância
            self.close() #Fechar tela de login
        else:
            self.alerta()

    def alerta(self):
        msg = QMessageBox()
        msg.setWindowTitle('Atenção!')
        msg.setText('Usuário / senha incorretos!')
        msg.setIcon(QMessageBox.Warning) #NoIcon, Question, Information, Critical
        msg.setWindowIcon(QIcon('C:\QtDesign\Img\warning1.png'))
        msg.exec()

    

class TelaPrincipal(QWidget, Ui_Principal):
    def __init__(self) -> None:
        super(TelaPrincipal, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("PresenTI")

if __name__=="__main__":
    app = QApplication(sys.argv)
    tela_login = login_atualizado()
    tela_login.show()
    app.exec()
