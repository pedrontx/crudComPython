# Importando o sqlite 
import sqlite3 as lite

# Criando a conexão com o banco de dados 
conexao = lite.connect('dados.db')

# Criando tabela 
with conexao:
    cur = conexao.cursor()
    cur.execute('create table Formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia_em DATE, estado TEXT, assunto TEXT)')
 