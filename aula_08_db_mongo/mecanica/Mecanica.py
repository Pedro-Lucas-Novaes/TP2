from tkinter import *
from tkinter import ttk, messagebox
import pymongo


class Mecanica:

    def __init__(self):

        # =========================
        # JANELA
        # =========================
        self.tela = Tk()
        self.tela.title("CRUD Oficina Mecânica")
        self.tela.geometry("1100x750")
        self.tela.configure(bg="#f0f0f0")

        # =========================
        # CONEXÃO MONGO
        # =========================
        self.conexao = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.conexao["oficina"]
        self.collection = self.db["servicos"]

        # =========================
        # ÍCONES
        # =========================
        self.foto_salvar = PhotoImage(file="icones/salvar.png")
        self.foto_consultar = PhotoImage(file="icones/consultar.png")
        self.foto_alterar = PhotoImage(file="icones/alterar.png")
        self.foto_excluir = PhotoImage(file="icones/excluir.png")
        self.foto_limpar = PhotoImage(file="icones/sair.png")

        self.criar_componentes()

    # ==================================================
    # INTERFACE
    # ==================================================
    def criar_componentes(self):

        Label(
            self.tela,
            text="Sistema Oficina Mecânica",
            font=("Arial", 24, "bold"),
            bg="#f0f0f0"
        ).pack(pady=15)

        frame = Frame(self.tela, bg="#f0f0f0")
        frame.pack()

        # CLIENTE
        Label(frame, text="Cliente:", bg="#f0f0f0").grid(row=0, column=0, pady=5)
        self.txt_cliente = Entry(frame, width=30)
        self.txt_cliente.grid(row=0, column=1)

        # TELEFONE
        Label(frame, text="Telefone:", bg="#f0f0f0").grid(row=1, column=0, pady=5)
        self.txt_telefone = Entry(frame, width=30)
        self.txt_telefone.grid(row=1, column=1)

        # PLACA
        Label(frame, text="Placa:", bg="#f0f0f0").grid(row=2, column=0, pady=5)
        self.txt_placa = Entry(frame, width=30)
        self.txt_placa.grid(row=2, column=1)

        # MODELO
        Label(frame, text="Modelo:", bg="#f0f0f0").grid(row=3, column=0, pady=5)
        self.txt_modelo = Entry(frame, width=30)
        self.txt_modelo.grid(row=3, column=1)

        # SERVIÇO
        Label(frame, text="Serviço:", bg="#f0f0f0").grid(row=4, column=0, pady=5)
        self.txt_servico = Entry(frame, width=30)
        self.txt_servico.grid(row=4, column=1)

        # VALOR
        Label(frame, text="Valor:", bg="#f0f0f0").grid(row=5, column=0, pady=5)
        self.txt_valor = Entry(frame, width=30)
        self.txt_valor.grid(row=5, column=1)

        # STATUS
        Label(frame, text="Status:", bg="#f0f0f0").grid(row=6, column=0, pady=5)
        self.txt_status = Entry(frame, width=30)
        self.txt_status.grid(row=6, column=1)

        # ==================================================
        # BOTÕES COM ÍCONES
        # ==================================================
        frame_btn = Frame(self.tela, bg="#f0f0f0")
        frame_btn.pack(pady=10)

        Button(frame_btn, text="Cadastrar", image=self.foto_salvar,
               compound=TOP, bg="#4CAF50", fg="white",
               width=110, height=90, command=self.salvar).grid(row=0, column=0, padx=8)

        Button(frame_btn, text="Consultar", image=self.foto_consultar,
               compound=TOP, bg="#2196F3", fg="white",
               width=110, height=90, command=self.consultar).grid(row=0, column=1, padx=8)

        Button(frame_btn, text="Alterar", image=self.foto_alterar,
               compound=TOP, bg="#FFC107", fg="black",
               width=110, height=90, command=self.atualizar).grid(row=0, column=2, padx=8)

        Button(frame_btn, text="Excluir", image=self.foto_excluir,
               compound=TOP, bg="#F44336", fg="white",
               width=110, height=90, command=self.excluir).grid(row=0, column=3, padx=8)

        Button(frame_btn, text="Sair", image=self.foto_limpar,
               compound=TOP, bg="#9E9E9E", fg="white",
               width=110, height=90, command=self.sair).grid(row=0, column=4, padx=8)

        # ==================================================
        # TABELA
        # ==================================================
        self.tabela = ttk.Treeview(
            self.tela,
            columns=("cliente", "placa", "modelo", "servico", "valor", "status"),
            show="headings",
            height=12
        )

        self.tabela.heading("cliente", text="Cliente")
        self.tabela.heading("placa", text="Placa")
        self.tabela.heading("modelo", text="Modelo")
        self.tabela.heading("servico", text="Serviço")
        self.tabela.heading("valor", text="Valor")
        self.tabela.heading("status", text="Status")

        self.tabela.pack(pady=20)

        self.listar()

    # ==================================================
    # CREATE
    # ==================================================
    def salvar(self):

        try:
            dados = {
                "cliente": self.txt_cliente.get(),
                "telefone": self.txt_telefone.get(),
                "placa": self.txt_placa.get(),
                "modelo": self.txt_modelo.get(),
                "servico": self.txt_servico.get(),
                "valor": float(self.txt_valor.get()),
                "status": self.txt_status.get()
            }

            self.collection.insert_one(dados)

            messagebox.showinfo("Sucesso", "Cadastro realizado!")
            self.listar()
            self.limpar()

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # ==================================================
    # READ
    # ==================================================
    def listar(self):

        for i in self.tabela.get_children():
            self.tabela.delete(i)

        for s in self.collection.find():

            self.tabela.insert("", END, values=(
                s.get("cliente"),
                s.get("placa"),
                s.get("modelo"),
                s.get("servico"),
                s.get("valor"),
                s.get("status")
            ))

    # ==================================================
    # CONSULTAR
    # ==================================================
    def consultar(self):

        placa = self.txt_placa.get()

        resultado = self.collection.find_one({"placa": placa})

        if resultado:

            self.limpar()

            self.txt_cliente.insert(0, resultado["cliente"])
            self.txt_telefone.insert(0, resultado["telefone"])
            self.txt_placa.insert(0, resultado["placa"])
            self.txt_modelo.insert(0, resultado["modelo"])
            self.txt_servico.insert(0, resultado["servico"])
            self.txt_valor.insert(0, resultado["valor"])
            self.txt_status.insert(0, resultado["status"])

        else:
            messagebox.showwarning("Aviso", "Não encontrado!")

    # ==================================================
    # UPDATE
    # ==================================================
    def atualizar(self):

        try:
            placa = self.txt_placa.get()

            self.collection.update_one(
                {"placa": placa},
                {"$set": {
                    "cliente": self.txt_cliente.get(),
                    "telefone": self.txt_telefone.get(),
                    "modelo": self.txt_modelo.get(),
                    "servico": self.txt_servico.get(),
                    "valor": float(self.txt_valor.get()),
                    "status": self.txt_status.get()
                }}
            )

            messagebox.showinfo("Sucesso", "Atualizado!")
            self.listar()

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # ==================================================
    # DELETE
    # ==================================================
    def excluir(self):

        placa = self.txt_placa.get()

        self.collection.delete_one({"placa": placa})

        messagebox.showinfo("Sucesso", "Excluído!")
        self.listar()
        self.limpar()

    # ==================================================
    # LIMPAR CAMPOS
    # ==================================================
    def limpar(self):

        self.txt_cliente.delete(0, END)
        self.txt_telefone.delete(0, END)
        self.txt_placa.delete(0, END)
        self.txt_modelo.delete(0, END)
        self.txt_servico.delete(0, END)
        self.txt_valor.delete(0, END)
        self.txt_status.delete(0, END)

    # ==================================================
    # SAIR DO SISTEMA
    # ==================================================
    def sair(self):

        if messagebox.askyesno("Confirmação", "Deseja realmente sair?"):
            self.tela.destroy()

    # ==================================================
    # EXECUTAR
    # ==================================================
    def executar(self):
        self.tela.mainloop()