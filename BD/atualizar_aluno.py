from conexao import conectar

conn = conectar()
cursor = conn.cursor()

id_aluno = int(input("Digite o ID do aluno que deseja atualizar: "))
novo_nome = input("Novo nome: ")
nova_idade = int(input("Nova idade: "))
novo_curso = input("Novo curso: ")

query = "UPDATE alunos SET nome=%s, idade=%s, curso=%s WHERE id=%s"
cursor.execute(query, (novo_nome, nova_idade, novo_curso, id_aluno))
conn.commit()

print("Aluno atualizado com sucesso!")
conn.close()
