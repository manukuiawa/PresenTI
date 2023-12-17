import sys
import typing #Verificar o que aparece no QtDesigner
import sqlite3
import datetime

from PyQt5.QtGui import QIcon #Biblioteca para usar ícones
from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication, QMainWindow

from PyQt5 import QtWidgets, QtCore, QtGui

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

def gerar_relatorio():
    conexao = sqlite3.connect('alunos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    conexao.close()

    c = canvas.Canvas("relatorio_alunos.pdf", pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(300, 750, "Relatório de Alunos")

    titulo_tabela = ["Nome", "Sobrenome", "Idade"]
    dados_tabela = [titulo_tabela] + [[aluno[1], aluno[2], aluno[3]] for aluno in alunos]

    tabela = Table(dados_tabela, colWidths=120, rowHeights=30, repeatRows=1)
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
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Adiciona linhas à tabela
    ]))

    tabela.wrapOn(c, 400, 200)
    tabela.drawOn(c, (c._pagesize[0]-tabela._width)/2, c._pagesize[1]-100-tabela._height)

    c.save()
    QMessageBox.showinfo("Sucesso", "Relatório gerado com sucesso!")