import tkinter as tk
import subprocess

def abrir_produtos():
    subprocess.Popen(["python", "padaria_gui_produtos.py"])

def abrir_estoque():
    subprocess.Popen(["python", "controle_estoque.py"])

def abrir_clientes():
    subprocess.Popen(["python", "cadastro_clientes.py"])

janela = tk.Tk()
janela.title("Sistema de Padaria - Menu Principal")

tk.Label(janela, text="Bem-vindo ao Sistema de Padaria", font=("Arial", 14)).pack(pady=10)

tk.Button(janela, text="Gerenciar Produtos", width=30, command=abrir_produtos).pack(pady=5)
tk.Button(janela, text="Controle de Estoque", width=30, command=abrir_estoque).pack(pady=5)
tk.Button(janela, text="Cadastro de Clientes", width=30, command=abrir_clientes).pack(pady=5)

janela.mainloop()
