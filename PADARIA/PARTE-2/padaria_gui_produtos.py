import tkinter as tk
from tkinter import messagebox
from conexao import conectar

def listar_produtos():
    lista.delete(0, tk.END)
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    for produto in cursor.fetchall():
        lista.insert(tk.END, f"{produto[0]} | {produto[1]} | R$ {produto[2]:.2f}")
    conn.close()

def cadastrar_produto():
    nome = entry_nome.get().strip()
    preco = entry_preco.get().strip()
    if nome and preco.replace('.', '', 1).isdigit():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (nome, preco) VALUES (%s, %s)", (nome, preco))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Produto cadastrado.")
        entry_nome.delete(0, tk.END)
        entry_preco.delete(0, tk.END)
        listar_produtos()
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos corretamente.")

def deletar_produto():
    item = lista.get(tk.ACTIVE)
    if item:
        id_produto = item.split(" | ")[0]
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Produto excluído.")
        listar_produtos()

def atualizar_produto():
    item = lista.get(tk.ACTIVE)
    if item:
        id_produto = item.split(" | ")[0]
        nome = entry_nome.get().strip()
        preco = entry_preco.get().strip()
        if nome and preco.replace('.', '', 1).isdigit():
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("UPDATE produtos SET nome=%s, preco=%s WHERE id=%s", (nome, preco, id_produto))
            conn.commit()
            conn.close()
            messagebox.showinfo("Atualizado", "Produto atualizado com sucesso.")
            listar_produtos()
        else:
            messagebox.showwarning("Atenção", "Preencha os campos corretamente.")

# Interface
janela = tk.Tk()
janela.title("Gerenciamento de Produtos")

tk.Label(janela, text="Nome do Produto").grid(row=0, column=0)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

tk.Label(janela, text="Preço").grid(row=1, column=0)
entry_preco = tk.Entry(janela)
entry_preco.grid(row=1, column=1)

tk.Button(janela, text="Cadastrar", command=cadastrar_produto).grid(row=2, column=0)
tk.Button(janela, text="Atualizar", command=atualizar_produto).grid(row=2, column=1)
tk.Button(janela, text="Deletar", command=deletar_produto).grid(row=3, column=0, columnspan=2)

lista = tk.Listbox(janela, width=50)
lista.grid(row=4, column=0, columnspan=2)

listar_produtos()
janela.mainloop()
