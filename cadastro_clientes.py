import tkinter as tk
from tkinter import messagebox
from conexao import conectar

def cadastrar_cliente():
    nome = entry_nome.get().strip()
    telefone = entry_telefone.get().strip()
    if nome:
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO clientes (nome, telefone) VALUES (%s, %s)", (nome, telefone))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Cliente cadastrado!")
            entry_nome.delete(0, tk.END)
            entry_telefone.delete(0, tk.END)
            listar_clientes()
        except Exception as e:
            messagebox.showerror("Erro", str(e))
    else:
        messagebox.showwarning("Atenção", "O campo nome é obrigatório.")

def listar_clientes():
    lista.delete(0, tk.END)
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    for cliente in cursor.fetchall():
        lista.insert(tk.END, f"{cliente[0]} | {cliente[1]} | Tel: {cliente[2]}")
    conn.close()

janela = tk.Tk()
janela.title("Cadastro de Clientes")

tk.Label(janela, text="Nome").grid(row=0, column=0)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

tk.Label(janela, text="Telefone").grid(row=1, column=0)
entry_telefone = tk.Entry(janela)
entry_telefone.grid(row=1, column=1)

tk.Button(janela, text="Cadastrar Cliente", command=cadastrar_cliente).grid(row=2, column=0, columnspan=2)

lista = tk.Listbox(janela, width=50)
lista.grid(row=3, column=0, columnspan=2)

listar_clientes()
janela.mainloop()
