# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PI\Ui\Cadastro_atualizado.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Principal(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1032, 591)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(29, 30, 941, 491))
        self.widget.setStyleSheet("\n"
"\n"
"QPushButton#pushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(236, 141, 26, 219), stop: 1 rgba(160, 96, 18, 180));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
"background-color: rgba(0,0,0,0);\n"
"color: rgba(85,98,112,255);\n"
"}\n"
"\n"
"\n"
"QPushButton#pushButton_2:hover,#pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover {\n"
"color: rgba(131,96,53,255);\n"
"}\n"
"\n"
"\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
"padding-left: 5px;\n"
"padding-top:5px;\n"
"background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 71, 135, 219), stop: 1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color: rgba(150, 123, 111, 255)\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(290, 30, 621, 430))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255,255);\n"
"border-bottom-right-radius:50px;\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(520, 60, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 150)")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(420, 120, 190, 40))
        self.lineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(620, 120, 190, 40))
        self.lineEdit_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(39, 30, 371, 430))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:50px;\n"
"")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\PI\Img\image_cadastro.png"))
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(420, 180, 190, 40))
        self.lineEdit_3.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(620, 240, 190, 40))
        self.lineEdit_4.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(420, 240, 190, 40))
        self.lineEdit_5.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setGeometry(QtCore.QRect(620, 180, 190, 40))
        self.lineEdit_6.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(540, 310, 181, 16))
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(480, 350, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(620, 350, 111, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 390, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #000000, stop: 0.5 #808080, stop: 1 #FFFFFF);\n"
"color: black;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 390, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #000000, stop: 0.5 #808080, stop: 1 #FFFFFF);\n"
"color: black;\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "CADASTRO "))
        self.lineEdit.setPlaceholderText(_translate("Form", "Nome"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "CPF"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "E-mail"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "PIN"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "Confirme o PIN"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "Telefone"))
        self.label_2.setText(_translate("Form", "Informe o tipo de usuário:"))
        self.radioButton.setText(_translate("Form", "Padrão"))
        self.radioButton_2.setText(_translate("Form", "Administrador"))
        self.pushButton_2.setText(_translate("Form", "Cancelar"))
        self.pushButton_3.setText(_translate("Form", "Cadastrar"))

