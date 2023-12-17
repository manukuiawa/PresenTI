import sys
import typing #Verificar o que aparece no QtDesigner
import sqlite3
import datetime

from PyQt5.QtGui import QIcon #Biblioteca para usar ícones
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication, QMainWindow #Biblioteca para mostrar pop-ups

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

from menu_atualizado import *
from Menu import *
from Banco_de_dados import *

# class login_Usuario(QWidget, Ui_Menu):
#     def __init__(self)->None:
#         super(login_Usuario, self).__init__()
#         self.setupUi(self)
#         self.pushButton_5.clicked.connect(self.chama_usuarios)
#         self.pushButton_4.clicked.connect(self.chama_evento)
#         self.pushButton_2.clicked.connect(self.gerar_relatorio)
    
    
#     def chama_evento(self):
#         self.evento = TelaEvento()
#         self.evento.show()
#         self.close()
    
#     def chama_usuarios(self):
#         self.evento = TelaPrincipal() #Instancia a classe Principal
#         self.evento.show() #Chama a tela através da instância
#         self.close()

    # def gerar_relatorio(self):
    #     conexao = sqlite3.connect('PresenTI.db')
    #     cursor =  conexao.cursor()
    #     cursor.execute("SELECT * FROM Usuarios")
    #     Usuarios = cursor.fetchall()
    #     conexao.close()

    #     c = canvas.Canvas("relatorio_usuarios.pdf", pagesize=letter)
    #     c.setFont("Helvetica", 12)
    #     c.drawString(50, 750, "Relatório de Usuarios")

    #     linha = 730
    #     for usuario in Usuarios:
    #         linha -= 20 
    #         c.drawString(50, linha, f"Nome: {usuario[1]}")
    #         c.drawString(200, linha, f"Cpf: {usuario[2]}")
    #         c.drawString(350, linha, f"telefone: {usuario[3]}")  
    #         c.drawString(500, linha, f"Email: {usuario[4]}")
    #         c.drawString(700, linha, f"PIN_2: {usuario[5]}")
    #         c.drawString(800, linha, f"PIN: {usuario[6]}")
    #         c.drawString(900, linha, f"tipo_usuario: {usuario[7]}")
        
    #     c.save()

#     def gerar_relatorio(self):
#         conexao = sqlite3.connect('PresenTI.db')
#         cursor = conexao.cursor()
#         cursor.execute("SELECT * FROM Usuarios")
#         Usuarios = cursor.fetchall()
#         conexao.close()

#         c = canvas.Canvas("relatorio_usuarios.pdf", pagesize=letter)
#         c.setFont("Helvetica-Bold", 16)
#         c.drawCentredString(300, 750, "Relatório de Usuários")

#         titulo_tabela = ["Nome", "Cpf", "telefone", "Email", "PIN_2", "PIN", "tipo_usuario"]
#         dados_tabela = [titulo_tabela] + [[usuario[1], usuario[2], usuario[3], usuario[4], usuario[5], usuario[6], usuario[7]] for usuario in Usuarios]

#         tabela = Table(dados_tabela, colWidths=[1.1*inch]*len(titulo_tabela), repeatRows=1)
#         tabela.setStyle(TableStyle([
#             ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#             ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#             ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
#             ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#             ('FONTSIZE', (0, 0), (-1, 0), 12),
#             ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#             ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#             ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
#             ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
#             ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
#             ('FONTSIZE', (0, 1), (-1, -1), 12),
#             ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
#             ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Adiciona linhas à tabela
#         ]))

#         tabela.wrapOn(c, letter[0]-100, letter[1]-200) 
#         tabela.drawOn(c, (letter[0]-tabela._width)/2, letter[1]-150-tabela._height)

#         c.save()
       
# if __name__=="__main__":
#     app = QApplication(sys.argv)
#     tela_login =login_Usuario()
#     tela_login.show()
#     app.exec()