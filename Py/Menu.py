import sys
import typing  # Verificar o que aparece no QtDesigner
import sqlite3
import datetime

from PyQt5.QtGui import QIcon  # Biblioteca para usar ícones
# Biblioteca para mostrar pop-ups
from PyQt5.QtWidgets import *

from PyQt5 import QtWidgets, QtCore, QtGui

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from login_Import import Ui_login
from cadastro_usuario_Import import *
from Banco_de_dados import *
from cadastro_evento_Import import *
from menu_atualizado import *
from selecao_evento_atualizado import *
from consultas_atualizado import *
from consulta_evento_atualizado import *
from consulta_usuario_atualizado import *
from checkin_evento_atualizado import *

codigo: str


class login_atualizado(QWidget, Ui_login):  # Tela de login
    def __init__(self) -> None:
        super(login_atualizado, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.lineEdit_4.setMaxLength(6)
        # self.setObjectName("Form")
        # self.resize(1032, 591)
        # self.widget = QtWidgets.QWidget(self)
        # self.widget.setGeometry(QtCore.QRect(29, 30, 941, 491))

        self.pushButton_3.clicked.connect(self.logar)
        self.pushButton_2.clicked.connect(self.close)

    def logar(self):
        global codigo
        codigo = self.lineEdit.text()
        pin = self.lineEdit_4.text()
        if codigo and pin:
            conexao = sqlite3.connect('PresenTI.db')
            cursor = conexao.cursor()
            cursor.execute(
                "SELECT PIN FROM Usuarios WHERE id_usuario='{}'".format(codigo))
            pin_db = cursor.fetchall()
            cursor.execute(
                "SELECT tipo_usuario FROM Usuarios WHERE id_usuario='{}'".format(codigo))
            tp_user_db = cursor.fetchall()
            if pin == str(pin_db[0][0]):
                if tp_user_db[0][0] == 0:
                    self.carrega = TelaMenu()  # Instancia a classe do menu principal
                    self.carrega.show()  # Chama a tela através da instância
                    self.close()  # Fechar tela de login
                elif tp_user_db[0][0] == 1:
                    self.carrega = TelaSelecaoEventos()
                    self.carrega.show()
                    self.close()
            else:
                self.alerta()
        else:
            self.alerta_campos_vazios()

    def alerta(self):
        msg = QMessageBox()
        msg.setWindowTitle('Atenção!')
        msg.setText('Código e/ou PIN incorreto(s)!')
        # NoIcon, Question, Information, Critical
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('C:\QtDesign\Img\warning1.png'))
        msg.exec()

    def alerta_campos_vazios(self):
        msg = QMessageBox()
        msg.setWindowTitle('Atenção!')
        msg.setText('Código e/ou PIN não preenchido(s)!')
        # NoIcon, Question, Information, Critical
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('C:\QtDesign\Img\warning1.png'))
        msg.exec()


class TelaUsuarios(QWidget, Ui_Principal):  # Cadastro de usuários
    def __init__(self) -> None:
        super(TelaUsuarios, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cadastro de usuários")
        self.lineEdit_2.setInputMask("000.000.000-00")
        self.lineEdit_6.setInputMask("(00)0-0000-0000")
        self.lineEdit_4.setMaxLength(6)
        self.lineEdit_5.setMaxLength(6)
        self.radioButton.setChecked(True)  # Puxa setado como usuário padrão
        self.pushButton_3.clicked.connect(self.cadastrar_usuario)
        self.pushButton_2.clicked.connect(self.chama_menu)

    def chama_menu(self):
        self.menu = TelaMenu()  # Instancia a classe Principal
        self.menu.show()  # Chama a tela através da instância
        self.close()

    # função para cadastrar o usuario

    def cadastrar_usuario(self):
        Nome = self.lineEdit.text()
        Cpf = self.lineEdit_2.text()
        telefone = self.lineEdit_6.text()
        Email = self.lineEdit_3.text()
        PIN = self.lineEdit_4.text()
        PIN_2 = self.lineEdit_5.text()

        if Nome and Cpf and telefone and Email and PIN and PIN_2:
            if len(Cpf) != 14:
                self.alerta_cpf()
            elif len(telefone) != 15:
                self.alerta_celular()
            else:
                if len(PIN) == 6:
                    try:
                        pin_int = int(PIN)
                        if PIN == PIN_2:
                            if self.radioButton.isChecked():
                                tipo_usuario = "1"
                            elif self.radioButton_2.isChecked():
                                tipo_usuario = "0"
                            elif Nome and Cpf and telefone and Email and PIN_2 and PIN:
                                self.alerta_tp_user()

                            conexao = sqlite3.connect('PresenTI.db')
                            cursor = conexao.cursor()
                            cursor.execute("INSERT INTO Usuarios (Nome, Cpf, telefone, Email, PIN, tipo_usuario) VALUES (?, ?, ?, ?, ?, ?)", (
                                Nome, Cpf, telefone, Email, PIN, tipo_usuario))
                            conexao.commit()
                            conexao.close()
                            self.sucesso()
                        else:
                            self.alerta_PINs_Dif()
                    except:
                        self.alerta_PIN_numero()
                else:
                    self.alerta_PIN_tamanho()
        else:
            self.alerta_preencher_campos()

    def sucesso(self):
        conexao = sqlite3.connect('PresenTI.db')
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT id_usuario FROM Usuarios WHERE id_usuario = (SELECT MAX(id_usuario) FROM Usuarios)")
        id_user = cursor.fetchall()
        messagebox.showinfo(
            "Sucesso", f"Usuário {id_user[0][0]} cadastrado com sucesso!")

    def alerta_preencher_campos(self):
        msg = QMessageBox()
        msg.setWindowTitle('Atenção!')
        msg.setText('Favor preencher todos os campos.')
        # NoIcon, Question, Information, Critical
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('C:\QtDesign\Img\warning1.png'))
        msg.exec()

    def alerta_celular(self):
        msg = QMessageBox()
        msg.setWindowTitle('Atenção!')
        msg.setText('Favor preencher o telefone no formato "(12)3-4567-8901".')
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('C:\QtDesign\Img\warning1.png'))
        msg.exec()

    def alerta_cpf(self):
        msg = QMessageBox()
        msg.setWindowTitle('Atenção!')
        msg.setText('Favor preencher o CPF no formato "123.456.789-10".')
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('C:\QtDesign\Img\warning1.png'))
        msg.exec()

    def alerta_PINs_Dif(self):
        msg = QMessageBox()
        msg.setWindowTitle('Atenção!')
        msg.setText('Os PINs não são iguais!')
        # NoIcon, Question, Information, Critical
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('C:\QtDesign\Img\warning1.png'))
        msg.exec()

    def alerta_PIN_tamanho(self):
        msg = QMessageBox()
        msg.setWindowTitle('Atenção!')
        msg.setText('O PIN deve ter 6 dígitos.')
        # NoIcon, Question, Information, Critical
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('C:\QtDesign\Img\warning1.png'))
        msg.exec()

    def alerta_PIN_numero(self):
        msg = QMessageBox()
        msg.setWindowTitle('Atenção!')
        msg.setText('O PIN deve conter somente números.')
        # NoIcon, Question, Information, Critical
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('C:\QtDesign\Img\warning1.png'))
        msg.exec()

    def alerta_tp_user(self):
        msg = QMessageBox()
        msg.setWindowTitle('Atenção!')
        msg.setText('Selecione o tipo de usuário!')
        # NoIcon, Question, Information, Critical
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('C:\QtDesign\Img\warning1.png'))
        msg.exec()

# Cadastro de eventos
class TelaEventos(QMainWindow, Ui_MainWindow):  
    def __init__(self) -> None:
        super(TelaEventos, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cadastrar evento")
        self.pushButton_3.clicked.connect(self.cadastrar_evento)
        self.pushButton_2.clicked.connect(self.chama_menu)

    # função para cadastrar o evento
    def cadastrar_evento(self):
        Nome_evento = self.lineEdit.text()
        Desc_evento = self.lineEdit_3.text()
        Hora_inicio = self.dateTimeEdit.text()
        Hora_fim = self.dateTimeEdit_2.text()

        if Nome_evento and Desc_evento and Hora_inicio and Hora_fim:
            conexao = sqlite3.connect('PresenTI.db')
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO Evento (Nome_evento, Descricao, Hora_inicio, Hora_fim) VALUES (?, ?, ?, ?)",
                           (Nome_evento, Desc_evento, Hora_inicio, Hora_fim))
            conexao.commit()
            conexao.close()
            self.sucesso()
        else:
            self.alerta_preencher_campos()

    def sucesso(self):
        conexao = sqlite3.connect('PresenTI.db')
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT id_evento FROM Evento WHERE id_evento = (SELECT MAX(id_evento) FROM Evento)")
        id_user = cursor.fetchall()
        messagebox.showinfo(
            "Sucesso", f"Evento {id_user[0][0]} cadastrado com sucesso!")

    def alerta_preencher_campos(self):
        msg = QMessageBox()
        msg.setWindowTitle('Atenção!')
        msg.setText('Favor preencher todos os campos.')
        # NoIcon, Question, Information, Critical
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('C:\QtDesign\Img\warning1.png'))
        msg.exec()

    def chama_menu(self):
        self.menu = TelaMenu()  # Instancia a classe Principal
        self.menu.show()  # Chama a tela através da instância
        self.close()


class TelaMenu(QWidget, Ui_Menu):  # Menu principal do software
    def __init__(self) -> None:
        super(TelaMenu, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("PresenTI")
        self.pushButton.clicked.connect(self.chama_usuarios)
        self.pushButton_2.clicked.connect(self.chama_eventos)
        self.pushButton_3.clicked.connect(self.menu_consulta)
        self.pushButton_4.clicked.connect(self.gerar_relatorio)
        self.pushButton_5.clicked.connect(self.login)

    def chama_eventos(self):
        self.evento = TelaEventos()
        self.evento.show()
        self.close()

    def menu_consulta(self):
        self.evento = TelaMenuConsulta()
        self.evento.show()
        self.close()

    def chama_usuarios(self):
        self.evento = TelaUsuarios()  # Instancia a classe Principal
        self.evento.show()  # Chama a tela através da instância
        self.close()

    def login(self):
        self.carrega = login_atualizado()
        self.carrega.show()
        self.close()

    def gerar_relatorio(self):
        conexao = sqlite3.connect('PresenTI.db')
        cursor = conexao.cursor()
        # cursor.execute("SELECT * FROM Usuarios")
        # Usuarios = cursor.fetchall()

        cursor.execute("SELECT u.id_usuario, u.Nome, e.Nome_evento , re.hora_login FROM Usuarios AS u INNER JOIN relacionamento_evento AS re ON u.id_usuario = re.id_usuario INNER JOIN Evento AS e ON re.id_evento = e.id_evento WHERE u.tipo_usuario = 1")
        Usuarios = cursor.fetchall()

        conexao.close()

        c = canvas.Canvas("relatorio_freq.pdf", pagesize=letter)
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(300, 750, "Relatório de Frequência")

        # titulo_tabela = ["Nome", "Cpf", "telefone", "Email", "PIN_2", "PIN", "tipo_usuario"]
        # dados_tabela = [titulo_tabela] + [[usuario[1], usuario[2], usuario[3], usuario[4], usuario[5], usuario[6], usuario[7]] for usuario in Usuarios]
        titulo_tabela = ["Código", "Nome", "Evento", "Hora"]
        dados_tabela = [titulo_tabela] + [[usuario[0], usuario[1],
                                           usuario[2], usuario[3]] for usuario in Usuarios]

        tabela = Table(dados_tabela, colWidths=[
                       2*inch]*len(titulo_tabela), repeatRows=1)
        tabela.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
            # Adiciona linhas à tabela
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))

        tabela.wrapOn(c, letter[0]-100, letter[1]-200)
        tabela.drawOn(c, (letter[0]-tabela._width) /
                      2, letter[1]-150-tabela._height)

        c.save()

        messagebox.showinfo("Sucesso", "Relatório gerado com sucesso!")

# Tela de menu de consultas
class TelaMenuConsulta(QWidget, Ui_Menu_Consulta):
    def __init__(self) -> None:
        super(TelaMenuConsulta, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Consultas")
        self.pushButton_6.clicked.connect(self.consulta_evento)
        self.pushButton_3.clicked.connect(self.consulta_usuario)
        self.pushButton_4.clicked.connect(self.consulta_checkin)
        self.pushButton_5.clicked.connect(self.chama_menu)

    def consulta_evento(self):
        self.carrega = TelaConsultaEvento()
        self.carrega.show()
        self.close()

    def consulta_usuario(self):
        self.carrega = TelaConsultaUsuario()
        self.carrega.show()
        self.close()

    def consulta_checkin(self):
        self.carrega = TelaConsultaCheckin()
        self.carrega.show()
        self.close()

    def chama_menu(self):
        self.carrega = TelaMenu()
        self.carrega.show()
        self.close()

# Tela de consulta / alteração de eventos
class TelaConsultaEvento(QMainWindow, Ui_Consulta_Evento):
    def __init__(self) -> None:
        super(TelaConsultaEvento, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Consulta de Eventos")
        self.atualizar_lista_eventos()
        self.tableWidget.cellClicked.connect(self.get_linha_selecionada)
        self.pushButton_3.clicked.connect(self.atualizar)
        self.pushButton_2.clicked.connect(self.deletar)
        self.pushButton_4.clicked.connect(self.chama_menu)

    def atualizar_lista_eventos(self):
        conexao = sqlite3.connect('PresenTI.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Evento")
        eventos = cursor.fetchall()
        cursor.execute("SELECT COUNT(*) FROM Evento")
        contador = cursor.fetchall()
        conexao.close()
        self.tableWidget.setHorizontalHeaderLabels(
            ['id_evento', 'Evento', 'Descrição', 'Hora início', 'Hora término'])
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(contador[0][0])
        x = 0
        y = 0
        while x < contador[0][0]:
            y = 0
            while y < 5:
                self.tableWidget.setItem(
                    x, y, QTableWidgetItem(str(eventos[x][y])))
                y += 1
            x += 1
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def get_linha_selecionada(self, linha, coluna):
        conexao = sqlite3.connect('PresenTI.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Evento")
        eventos = cursor.fetchall()
        conexao.close()
        self.lineEdit.setText(eventos[linha][1])
        self.lineEdit_3.setText(eventos[linha][2])
        self.lineEdit_2.setText(eventos[linha][3])
        self.lineEdit_4.setText(eventos[linha][4])
        self.id_evento = eventos[linha][0]

    def atualizar(self):
        self.id_evento
        Nome_evento = self.lineEdit.text()
        Desc_evento = self.lineEdit_3.text()
        Hora_inicio = self.lineEdit_2.text()
        Hora_fim = self.lineEdit_4.text()
        if Nome_evento and Desc_evento and Hora_inicio and Hora_fim:
            conexao = sqlite3.connect('PresenTI.db')
            cursor = conexao.cursor()
            cursor.execute(
                "UPDATE Evento SET Nome_evento = ?, Descricao = ?, Hora_inicio = ?, Hora_fim = ? WHERE id_evento = ?", (Nome_evento, Desc_evento, Hora_inicio, Hora_fim, self.id_evento))
            conexao.commit()
            conexao.close()
            self.atualizar_lista_eventos()
        else:
            self.alerta_preencher_campos()

    def alerta_preencher_campos(self):
        msg = QMessageBox()
        msg.setWindowTitle('Atenção!')
        msg.setText('Favor preencher todos os campos.')
        # NoIcon, Question, Information, Critical
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('C:\QtDesign\Img\warning1.png'))
        msg.exec()

    def deletar(self):
        self.id_evento
        confirmar_exclusao = messagebox.askquestion("Confirmação", "Tem certeza que deseja excluir o registro?")
        if confirmar_exclusao == 'yes':
            conexao = sqlite3.connect('PresenTI.db')
            cursor = conexao.cursor()
            cursor.execute(
                "DELETE FROM Evento WHERE id_evento = ?", (self.id_evento,))
            conexao.commit()
            conexao.close()
            self.atualizar_lista_eventos()

    def chama_menu(self):
        self.carrega = TelaMenu()
        self.carrega.show()
        self.close()

# Tela de consulta / alteração de usuários
class TelaConsultaUsuario(QMainWindow, Ui_Consulta_Usuario):
    def __init__(self) -> None:
        super(TelaConsultaUsuario, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Consulta de Usuários")
        self.lineEdit_4.setMaxLength(6)
        self.atualizar_lista_usuarios()
        self.tableWidget.cellClicked.connect(self.get_linha_selecionada)
        self.pushButton_3.clicked.connect(self.atualizar)
        self.pushButton_2.clicked.connect(self.deletar)
        self.pushButton_4.clicked.connect(self.chama_menu)

    def atualizar_lista_usuarios(self):
        conexao = sqlite3.connect('PresenTI.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT id_usuario, Nome, Cpf, telefone, Email FROM Usuarios")
        usuarios = cursor.fetchall()
        cursor.execute("SELECT COUNT(*) FROM Usuarios")
        contador = cursor.fetchall()
        conexao.close()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(contador[0][0])
        x = 0
        y = 0
        while x < contador[0][0]:
            y = 0
            while y < 5:
                self.tableWidget.setItem(
                    x, y, QTableWidgetItem(str(usuarios[x][y])))
                y += 1
            x += 1
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def get_linha_selecionada(self, linha, coluna):
        conexao = sqlite3.connect('PresenTI.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT id_usuario, Nome, telefone, Email, PIN FROM Usuarios")
        usuarios = cursor.fetchall()
        conexao.close()
        self.lineEdit.setText(usuarios[linha][1])
        self.lineEdit_3.setText(usuarios[linha][2])
        self.lineEdit_2.setText(usuarios[linha][3])
        self.id_usuario = usuarios[linha][0]

    def atualizar(self):
        self.id_usuario        
        Nome_usuario = self.lineEdit.text()
        Telefone = self.lineEdit_3.text()
        Email = self.lineEdit_2.text()
        PIN = self.lineEdit_4.text()
        if Nome_usuario and Telefone and Email and PIN:
            if len(Telefone) != 15:
                self.alerta_celular()
            else:
                if len(PIN) == 6:
                    try:
                        pin_int = int(PIN)
                        conexao = sqlite3.connect('PresenTI.db')
                        cursor = conexao.cursor()
                        cursor.execute("UPDATE Usuarios SET Nome = ?, telefone = ?, Email = ?, PIN = ? WHERE id_usuario = ?", (Nome_usuario, Telefone, Email, PIN, self.id_usuario))
                        conexao.commit()
                        conexao.close()
                        self.atualizar_lista_usuarios()
                    except:
                        self.alerta_PIN_numero()
                else:
                    self.alerta_PIN_tamanho()
        else:
            self.alerta_preencher_campos()

    def alerta_preencher_campos(self):
        msg = QMessageBox()
        msg.setWindowTitle('Atenção!')
        msg.setText('Favor preencher todos os campos.')
        # NoIcon, Question, Information, Critical
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('C:\QtDesign\Img\warning1.png'))
        msg.exec()

    def alerta_celular(self):
        msg = QMessageBox()
        msg.setWindowTitle('Atenção!')
        msg.setText('Favor preencher o telefone no formato "(12)3-4567-8901".')
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('C:\QtDesign\Img\warning1.png'))
        msg.exec()

    def alerta_PIN_tamanho(self):
        msg = QMessageBox()
        msg.setWindowTitle('Atenção!')
        msg.setText('O PIN deve ter 6 dígitos.')
        # NoIcon, Question, Information, Critical
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('C:\QtDesign\Img\warning1.png'))
        msg.exec()

    def alerta_PIN_numero(self):
        msg = QMessageBox()
        msg.setWindowTitle('Atenção!')
        msg.setText('O PIN deve conter somente números.')
        # NoIcon, Question, Information, Critical
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('C:\QtDesign\Img\warning1.png'))
        msg.exec()
        

    def deletar(self):
        self.id_usuario
        confirmar_exclusao = messagebox.askquestion("Confirmação", "Tem certeza que deseja excluir o registro?")
        if confirmar_exclusao == 'yes':
            conexao = sqlite3.connect('PresenTI.db')
            cursor = conexao.cursor()
            cursor.execute(
                "DELETE FROM Usuarios WHERE id_usuario = ?", (self.id_usuario,))
            conexao.commit()
            conexao.close()
            self.atualizar_lista_usuarios()

    def chama_menu(self):
        self.carrega = TelaMenu()
        self.carrega.show()
        self.close()


# Tela de consulta / alteração de checkin
class TelaConsultaCheckin(QMainWindow, Ui_Consulta_Checkin):
    def __init__(self) -> None:
        super(TelaConsultaCheckin, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Consulta de Check-ins")
        self.atualizar_lista_logs()
        self.tableWidget.cellClicked.connect(self.get_linha_selecionada)
        self.pushButton_3.clicked.connect(self.atualizar)
        self.pushButton_2.clicked.connect(self.deletar)
        self.pushButton_4.clicked.connect(self.chama_menu)

    def atualizar_lista_logs(self):
        conexao = sqlite3.connect('PresenTI.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM relacionamento_evento")
        logs = cursor.fetchall()
        cursor.execute("SELECT COUNT(*) FROM relacionamento_evento")
        contador = cursor.fetchall()
        conexao.close()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(contador[0][0])
        x = 0
        y = 0
        while x < contador[0][0]:
            y = 0
            while y < 4:
                self.tableWidget.setItem(
                    x, y, QTableWidgetItem(str(logs[x][y])))
                y += 1
            x += 1
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def get_linha_selecionada(self, linha, coluna):
        conexao = sqlite3.connect('PresenTI.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT id_relacionamento, hora_login FROM relacionamento_evento")
        logs = cursor.fetchall()
        conexao.close()
        self.lineEdit_2.setText(logs[linha][1])
        self.id_log = logs[linha][0]

    def atualizar(self):
        self.id_log
        Hora_login = self.lineEdit_2.text()
        if Hora_login:
            conexao = sqlite3.connect('PresenTI.db')
            cursor = conexao.cursor()
            cursor.execute(
                "UPDATE relacionamento_evento SET hora_login = ? WHERE id_relacionamento = ?", (Hora_login, self.id_log))
            conexao.commit()
            conexao.close()
            self.atualizar_lista_logs()
        else:
            self.alerta_preencher_campos()

    def alerta_preencher_campos(self):
        msg = QMessageBox()
        msg.setWindowTitle('Atenção!')
        msg.setText('Favor preencher todos os campos.')
        # NoIcon, Question, Information, Critical
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('C:\QtDesign\Img\warning1.png'))
        msg.exec()


    def deletar(self):
        self.id_log
        confirmar_exclusao = messagebox.askquestion("Confirmação", "Tem certeza que deseja excluir o registro?")
        if confirmar_exclusao == 'yes':
            conexao = sqlite3.connect('PresenTI.db')
            cursor = conexao.cursor()
            cursor.execute(
                "DELETE FROM relacionamento_evento WHERE id_relacionamento = ?", (self.id_log,))
            conexao.commit()
            conexao.close()
            self.atualizar_lista_logs()

    def chama_menu(self):
        self.carrega = TelaMenu()
        self.carrega.show()
        self.close()

# Check-in ou check-out do evento


class TelaSelecaoEventos(QWidget, Ui_SelecaoEvento):
    def __init__(self) -> None:
        super(TelaSelecaoEventos, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Check-in / Check-out do evento")
        conexao = sqlite3.connect('PresenTI.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT COUNT(*) FROM Evento")
        contador = cursor.fetchall()
        cursor.execute("SELECT Nome_evento FROM Evento")
        lista_evento = cursor.fetchall()
        c = int(contador[0][0])
        i = 0
        while (i < c):
            self.comboBox.addItem(lista_evento[i][0])
            i += 1
        self.pushButton_3.clicked.connect(self.checkin)
        self.pushButton_2.clicked.connect(self.login)

    # Função para o check-in ou check-out
    def checkin(self):
        conexao = sqlite3.connect('PresenTI.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT id_evento FROM Evento")
        id_evento = cursor.fetchall()
        selecionado = self.comboBox.currentIndex()
        Evento = id_evento[selecionado][0]
        User = codigo
        data_sem_microsegundos = datetime.datetime.now().replace(microsecond=0)
        Agora = data_sem_microsegundos

        if Evento and User and Agora:
            conexao = sqlite3.connect('PresenTI.db')
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO relacionamento_evento (id_evento, id_usuario, hora_login) VALUES (?, ?, ?)", (Evento, User, Agora))
            conexao.commit()
            conexao.close()
            messagebox.showinfo("Sucesso", "Presença registrada com sucesso!")
            self.login()
        else:
            self.alerta_preencher_campos()

    def alerta_preencher_campos(self):
        msg = QMessageBox()
        msg.setWindowTitle('Atenção!')
        msg.setText('Favor preencher todos os campos.')
        # NoIcon, Question, Information, Critical
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('C:\QtDesign\Img\warning1.png'))
        msg.exec()

    def login(self):
        self.carrega = login_atualizado()
        self.carrega.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_login = login_atualizado()
    tela_login.show()
    app.exec()
