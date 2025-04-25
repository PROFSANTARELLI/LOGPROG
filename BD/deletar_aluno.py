from conexao import conectar

conn = conectar()
cursor = conn.cursor()

id_aluno = int(input("Digite o ID do aluno que deseja excluir: "))

cursor.execute("DELETE FROM alunos WHERE id = %s", (id_aluno,))
conn.commit()

print("Aluno excluído com sucesso!")
conn.close()
