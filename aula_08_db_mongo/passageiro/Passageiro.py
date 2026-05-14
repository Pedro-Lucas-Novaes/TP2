from tkinter import *
from tkinter import ttk, messagebox
import pymongo


class Passagem:

    def __init__(self):

        self.tela = Tk()
        self.tela.title("CRUD Passagens")
        self.tela.geometry("1150x700")
        self.tela.configure(bg="#f2f2f2")

        self.conexao = pymongo.MongoClient("mongodb://localhost:27017/")

        self.db = self.conexao["passagens"]

        self.collection = self.db["passageiros"]

        self.criar_componentes()

    def criar_componentes(self):

        # TÍTULO
        Label(
            self.tela,
            text="Cadastro de Passagens",
            font=("Arial", 26, "bold"),
            bg="#f2f2f2",
            fg="#003366"
        ).pack(pady=20)

        # FRAME FORMULÁRIO
        frame = Frame(self.tela, bg="#f2f2f2")
        frame.pack(pady=10)

        # NOME
        Label(
            frame,
            text="Nome Passageiro:",
            font=("Arial", 11),
            bg="#f2f2f2"
        ).grid(row=0, column=0, pady=8, sticky=W)

        self.txt_nome = Entry(frame, width=40, font=("Arial", 11))
        self.txt_nome.grid(row=0, column=1)

        # TELEFONE
        Label(
            frame,
            text="Telefone:",
            font=("Arial", 11),
            bg="#f2f2f2"
        ).grid(row=1, column=0, pady=8, sticky=W)

        self.txt_telefone = Entry(frame, width=30, font=("Arial", 11))
        self.txt_telefone.grid(row=1, column=1)

        # RG
        Label(
            frame,
            text="RG:",
            font=("Arial", 11),
            bg="#f2f2f2"
        ).grid(row=2, column=0, pady=8, sticky=W)

        self.txt_rg = Entry(frame, width=30, font=("Arial", 11))
        self.txt_rg.grid(row=2, column=1)

        # LOCAL
        Label(
            frame,
            text="Destino:",
            font=("Arial", 11),
            bg="#f2f2f2"
        ).grid(row=3, column=0, pady=8, sticky=W)

        self.txt_local = Entry(frame, width=40, font=("Arial", 11))
        self.txt_local.grid(row=3, column=1)

        # DATA
        Label(
            frame,
            text="Data:",
            font=("Arial", 11),
            bg="#f2f2f2"
        ).grid(row=4, column=0, pady=8, sticky=W)

        self.txt_data = Entry(frame, width=20, font=("Arial", 11))
        self.txt_data.grid(row=4, column=1)

        # HORÁRIO
        Label(
            frame,
            text="Horário:",
            font=("Arial", 11),
            bg="#f2f2f2"
        ).grid(row=5, column=0, pady=8, sticky=W)

        self.txt_horario = Entry(frame, width=20, font=("Arial", 11))
        self.txt_horario.grid(row=5, column=1)

        # POLTRONA
        Label(
            frame,
            text="Poltrona:",
            font=("Arial", 11),
            bg="#f2f2f2"
        ).grid(row=6, column=0, pady=8, sticky=W)

        self.txt_poltrona = Entry(frame, width=20, font=("Arial", 11))
        self.txt_poltrona.grid(row=6, column=1)

        self.foto_salvar = PhotoImage(file="icones/salvar.png")
        self.foto_consultar = PhotoImage(file="icones/consultar.png")
        self.foto_alterar = PhotoImage(file="icones/alterar.png")
        self.foto_excluir = PhotoImage(file="icones/excluir.png")
        self.foto_sair = PhotoImage(file="icones/sair.png")

        frame_botoes = Frame(self.tela, bg="#f2f2f2")
        frame_botoes.pack(pady=20)

        # CADASTRAR
        self.btn_salvar = Button(
            frame_botoes,
            text="Cadastrar",
            image=self.foto_salvar,
            compound=TOP,
            width=110,
            height=90,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            relief=FLAT,
            bd=0,
            activebackground="#388E3C",
            command=self.salvar
        )

        self.btn_salvar.grid(row=0, column=0, padx=10)

        # CONSULTAR
        self.btn_consultar = Button(
            frame_botoes,
            text="Consultar",
            image=self.foto_consultar,
            compound=TOP,
            width=110,
            height=90,
            bg="#2196F3",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            relief=FLAT,
            bd=0,
            activebackground="#1976D2",
            command=self.consultar
        )

        self.btn_consultar.grid(row=0, column=1, padx=10)

        # ALTERAR
        self.btn_alterar = Button(
            frame_botoes,
            text="Alterar",
            image=self.foto_alterar,
            compound=TOP,
            width=110,
            height=90,
            bg="#FFC107",
            fg="black",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            relief=FLAT,
            bd=0,
            activebackground="#FFA000",
            command=self.atualizar
        )

        self.btn_alterar.grid(row=0, column=2, padx=10)

        # EXCLUIR
        self.btn_excluir = Button(
            frame_botoes,
            text="Excluir",
            image=self.foto_excluir,
            compound=TOP,
            width=110,
            height=90,
            bg="#F44336",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            relief=FLAT,
            bd=0,
            activebackground="#D32F2F",
            command=self.excluir
        )

        self.btn_excluir.grid(row=0, column=3, padx=10)

        # SAIR
        self.btn_sair = Button(
            frame_botoes,
            text="Sair",
            image=self.foto_sair,
            compound=TOP,
            width=110,
            height=90,
            bg="#616161",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            relief=FLAT,
            bd=0,
            activebackground="#424242",
            command=self.tela.destroy
        )

        self.btn_sair.grid(row=0, column=4, padx=10)

        self.tabela = ttk.Treeview(
            self.tela,
            columns=(
                "nome",
                "telefone",
                "rg",
                "destino",
                "data",
                "horario",
                "poltrona"
            ),
            show="headings",
            height=10
        )

        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("telefone", text="Telefone")
        self.tabela.heading("rg", text="RG")
        self.tabela.heading("destino", text="Destino")
        self.tabela.heading("data", text="Data")
        self.tabela.heading("horario", text="Horário")
        self.tabela.heading("poltrona", text="Poltrona")

        self.tabela.column("nome", width=180)
        self.tabela.column("telefone", width=120)
        self.tabela.column("rg", width=100)
        self.tabela.column("destino", width=150)
        self.tabela.column("data", width=100)
        self.tabela.column("horario", width=100)
        self.tabela.column("poltrona", width=100)

        self.tabela.pack(pady=20)

        self.listar_passagens()

    def salvar(self):

        try:

            passageiro = {

                "nome": self.txt_nome.get(),
                "telefone": self.txt_telefone.get(),
                "rg": self.txt_rg.get(),
                "destino": self.txt_local.get(),
                "data": self.txt_data.get(),
                "horario": self.txt_horario.get(),
                "poltrona": self.txt_poltrona.get()
            }

            self.collection.insert_one(passageiro)

            messagebox.showinfo(
                "Sucesso",
                "Passagem cadastrada com sucesso!"
            )

            self.limpar()

            self.listar_passagens()

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

    def consultar(self):

        rg = self.txt_rg.get()

        resultado = self.collection.find_one({"rg": rg})

        if resultado:

            self.limpar()

            self.txt_nome.insert(END, resultado["nome"])
            self.txt_telefone.insert(END, resultado["telefone"])
            self.txt_rg.insert(END, resultado["rg"])
            self.txt_local.insert(END, resultado["destino"])
            self.txt_data.insert(END, resultado["data"])
            self.txt_horario.insert(END, resultado["horario"])
            self.txt_poltrona.insert(END, resultado["poltrona"])

        else:

            messagebox.showwarning(
                "Aviso",
                "Passagem não encontrada!"
            )

    def atualizar(self):

        rg = self.txt_rg.get()

        self.collection.update_one(

            {"rg": rg},

            {"$set": {

                "nome": self.txt_nome.get(),
                "telefone": self.txt_telefone.get(),
                "destino": self.txt_local.get(),
                "data": self.txt_data.get(),
                "horario": self.txt_horario.get(),
                "poltrona": self.txt_poltrona.get()

            }}
        )

        messagebox.showinfo(
            "Sucesso",
            "Passagem atualizada!"
        )

        self.limpar()

        self.listar_passagens()

    def excluir(self):

        rg = self.txt_rg.get()

        self.collection.delete_one({"rg": rg})

        messagebox.showinfo(
            "Sucesso",
            "Passagem excluída!"
        )

        self.limpar()

        self.listar_passagens()

    def listar_passagens(self):

        for item in self.tabela.get_children():
            self.tabela.delete(item)

        passageiros = self.collection.find()

        for passageiro in passageiros:

            self.tabela.insert(
                "",
                END,
                values=(

                    passageiro.get("nome", ""),
                    passageiro.get("telefone", ""),
                    passageiro.get("rg", ""),
                    passageiro.get("destino", ""),
                    passageiro.get("data", ""),
                    passageiro.get("horario", ""),
                    passageiro.get("poltrona", "")
                )
            )

    def limpar(self):

        self.txt_nome.delete(0, END)
        self.txt_telefone.delete(0, END)
        self.txt_rg.delete(0, END)
        self.txt_local.delete(0, END)
        self.txt_data.delete(0, END)
        self.txt_horario.delete(0, END)
        self.txt_poltrona.delete(0, END)

    def executar(self):
        self.tela.mainloop()


