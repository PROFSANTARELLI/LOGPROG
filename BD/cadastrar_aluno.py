from conexao import conectar

conn = conectar()
cursor = conn.cursor()

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
curso = input("Digite o curso do aluno: ")

query = "INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)"
cursor.execute(query, (nome, idade, curso))
conn.commit()

print("Aluno cadastrado com sucesso!")
conn.close()
