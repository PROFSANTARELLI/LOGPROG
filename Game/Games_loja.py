import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Conexão com banco
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="aluno",
        password="toor",
        database="loja_games_teste_2"
    )

conexao = conectar()
cursor = conexao.cursor()

# Funções
def cadastrar_game():
    nome = entry_nome.get()
    genero = entry_genero.get()
    preco = entry_preco.get()
    estoque = entry_estoque.get()

    if nome and genero and preco and estoque:
        comando = "INSERT INTO games (nome, genero, preco, estoque) VALUES (%s, %s, %s, %s)"
        cursor.execute(comando, (nome, genero, preco, estoque))
        conexao.commit()
        listar_games()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Game cadastrado!")
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos.")

def listar_games():
    for i in tree.get_children():
        tree.delete(i)
    cursor.execute("SELECT * FROM games")
    for row in cursor.fetchall():
        tree.insert('', 'end', values=row)

def deletar_game():
    item = tree.selection()
    if item:
        game_id = tree.item(item)['values'][0]
        cursor.execute("DELETE FROM games WHERE id = %s", (game_id,))
        conexao.commit()
        listar_games()
        messagebox.showinfo("Sucesso", "Game deletado!")

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_genero.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_estoque.delete(0, tk.END)

# Interface
janela = tk.Tk()
janela.title("Loja de Games")
janela.geometry("700x500")

tk.Label(janela, text="Nome").grid(row=0, column=0)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

tk.Label(janela, text="Gênero").grid(row=1, column=0)
entry_genero = tk.Entry(janela)
entry_genero.grid(row=1, column=1)

tk.Label(janela, text="Preço").grid(row=2, column=0)
entry_preco = tk.Entry(janela)
entry_preco.grid(row=2, column=1)

tk.Label(janela, text="Estoque").grid(row=3, column=0)
entry_estoque = tk.Entry(janela)
entry_estoque.grid(row=3, column=1)

tk.Button(janela, text="Cadastrar", command=cadastrar_game).grid(row=4, column=0, pady=10)
tk.Button(janela, text="Excluir", command=deletar_game).grid(row=4, column=1)

tree = ttk.Treeview(janela, columns=('ID', 'Nome', 'Gênero', 'Preço', 'Estoque'), show='headings')
for col in tree['columns']:
    tree.heading(col, text=col)
tree.grid(row=5, column=0, columnspan=4)

listar_games()

janela.mainloop()