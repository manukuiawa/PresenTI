import sqlite3
from tkinter import Tk, Label, Entry, Button, Listbox, Scrollbar, messagebox


def conectar_banco():  #Cadastro de usuario
    conexao = sqlite3.connect('PresenTI.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Usuarios (
                    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nome TEXT NOT NULL,
                    Cpf TEXT NOT NULL,
                    telefone VARCHAR(100) NOT NULL,
                    Email TEXT NOT NULL,
                    PIN_2 INT NOT NULL,
                    PIN INT NOT NULL
                    )''')
    conexao.commit()
    conexao.close()

    
conectar_banco()


def conectar_evento(): #Cadastro do evento
    conexao = sqlite3.connect('PresenTI.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Evento (
                   id_evento INTEGER PRIMARY KEY AUTOINCREMENT,
                   Nome_evento TEXT NOT NULL,
                   Descricao TEXT NOT NULL,
                   Hora_inicio DATETIME NOT NULL,
                   Hora_fim DATETIME NOT NULL
    )''')
    conexao.commit()
    conexao.close()

conectar_evento()



def relacionamento_evento():  #Relacionamento entre evento e usuario
    conexao = sqlite3.connect('PresenTI.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS relacionamento_evento (
                   id_relacionamento INTEGER PRIMARY KEY AUTOINCREMENT,
                   id_evento INTEGER REFERENCES Evento (id_evento), 
                   id_usuario INTEGER REFERENCES Usuarios (id_usuario)
    )''')
    conexao.commit()
    conexao.close()

relacionamento_evento()