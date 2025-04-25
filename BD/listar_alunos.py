from conexao import conectar

conn = conectar()
cursor = conn.cursor()

cursor.execute("SELECT * FROM alunos")
alunos = cursor.fetchall()

print("\nLista de Alunos:")
for aluno in alunos:
    print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]} | Curso: {aluno[3]}")

conn.close()
