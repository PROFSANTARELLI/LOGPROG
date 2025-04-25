import sqlite3

# Conectar ou criar banco
conn = sqlite3.connect("aula.db")
cursor = conn.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER,
    curso TEXT
)
""")

# Inserir dados
nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
curso = input("Digite o curso do aluno: ")

cursor.execute("INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)", (nome, idade, curso))
conn.commit()

# Consultar dados
cursor.execute("SELECT * FROM alunos")
for linha in cursor.fetchall():
    print(linha)

conn.close()
