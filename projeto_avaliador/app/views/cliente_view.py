import tkinter as tk
from tkinter import messagebox
from app.controllers.cliente_controller import ClienteController

class ClienteView:
    def __init__(self, master):
        self.controller = ClienteController()
        self.master = master
        self.master.title("Cadastro de Clientes")

        self.nome_label = tk.Label(master, text="Nome:")
        self.nome_label.pack()
        self.nome_entry = tk.Entry(master)
        self.nome_entry.pack()

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(master)
        self.email_entry.pack()

        self.salvar_btn = tk.Button(master, text="Salvar", command=self.salvar_cliente)
        self.salvar_btn.pack()

        self.visualizar_btn = tk.Button(master, text="Ver Clientes", command=self.ver_clientes)
        self.visualizar_btn.pack()

    def salvar_cliente(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()
        self.controller.adicionar_cliente(nome, email)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

    def ver_clientes(self):
        clientes = self.controller.obter_clientes()
        for cliente in clientes:
            print(cliente)
