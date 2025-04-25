import tkinter as tk
from tkinter import messagebox
from conexao import conectar

def inserir():
    nome = entry_nome.get()
    idade = entry_idade.get()
    curso = entry_curso.get()

    if nome and idade and curso:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)", (nome, idade, curso))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Aluno cadastrado!")
        listar()
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos!")

def listar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    conn.close()

    lista.delete(0, tk.END)
    for aluno in alunos:
        lista.insert(tk.END, f"{aluno[0]} | {aluno[1]} | {aluno[2]} anos | {aluno[3]}")

def deletar():
    selecionado = lista.get(tk.ACTIVE)
    if selecionado:
        aluno_id = selecionado.split(" | ")[0]
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM alunos WHERE id = %s", (aluno_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Aluno excluído!")
        listar()
    else:
        messagebox.showwarning("Erro", "Selecione um aluno na lista.")

# Interface
janela = tk.Tk()
janela.title("Cadastro de Alunos")

tk.Label(janela, text="Nome").grid(row=0, column=0)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

tk.Label(janela, text="Idade").grid(row=1, column=0)
entry_idade = tk.Entry(janela)
entry_idade.grid(row=1, column=1)

tk.Label(janela, text="Curso").grid(row=2, column=0)
entry_curso = tk.Entry(janela)
entry_curso.grid(row=2, column=1)

tk.Button(janela, text="Cadastrar", command=inserir).grid(row=3, column=0, columnspan=2)
tk.Button(janela, text="Deletar Selecionado", command=deletar).grid(row=4, column=0, columnspan=2)

lista = tk.Listbox(janela, width=50)
lista.grid(row=5, column=0, columnspan=2)

listar()

janela.mainloop()
