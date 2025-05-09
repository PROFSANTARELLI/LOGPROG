import tkinter as tk
from tkinter import messagebox
from conexao import conectar

def formatar_preco(valor_str):
    try:
        valor = float(valor_str)
        return round(valor, 2)
    except ValueError:
        return None

def cadastrar():
    nome = entry_nome.get().strip()
    preco = formatar_preco(entry_preco.get())
    if nome and preco is not None:
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO produtos (nome, preco) VALUES (%s, %s)", (nome, preco))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Produto cadastrado!")
            entry_nome.delete(0, tk.END)
            entry_preco.delete(0, tk.END)
            listar()
        except Exception as e:
            messagebox.showerror("Erro", str(e))
    else:
        messagebox.showwarning("Campos inválidos", "Preencha todos os campos corretamente.")

def listar():
    lista.delete(0, tk.END)
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos")
        for produto in cursor.fetchall():
            lista.insert(tk.END, f"{produto[0]} | {produto[1]} | R$ {produto[2]:.2f}")
        conn.close()
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def deletar():
    item = lista.get(tk.ACTIVE)
    if item:
        pid = item.split(" | ")[0]
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM produtos WHERE id = %s", (pid,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Removido", "Produto deletado.")
            listar()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

def atualizar():
    item = lista.get(tk.ACTIVE)
    if item:
        pid = item.split(" | ")[0]
        novo_nome = entry_nome.get().strip()
        novo_preco = formatar_preco(entry_preco.get())
        if novo_nome and novo_preco is not None:
            try:
                conn = conectar()
                cursor = conn.cursor()
                cursor.execute("UPDATE produtos SET nome=%s, preco=%s WHERE id=%s", (novo_nome, novo_preco, pid))
                conn.commit()
                conn.close()
                messagebox.showinfo("Atualizado", "Produto alterado.")
                listar()
            except Exception as e:
                messagebox.showerror("Erro", str(e))
        else:
            messagebox.showwarning("Campos inválidos", "Informe nome e preço válidos para atualizar.")

# Interface gráfica
janela = tk.Tk()
janela.title("Sistema de Padaria")

tk.Label(janela, text="Nome do produto").grid(row=0, column=0)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

tk.Label(janela, text="Preço (ex: 9.90)").grid(row=1, column=0)
entry_preco = tk.Entry(janela)
entry_preco.grid(row=1, column=1)

tk.Button(janela, text="Cadastrar", command=cadastrar).grid(row=2, column=0)
tk.Button(janela, text="Atualizar", command=atualizar).grid(row=2, column=1)
tk.Button(janela, text="Deletar", command=deletar).grid(row=3, column=0, columnspan=2)

lista = tk.Listbox(janela, width=50)
lista.grid(row=4, column=0, columnspan=2)

listar()
janela.mainloop()
