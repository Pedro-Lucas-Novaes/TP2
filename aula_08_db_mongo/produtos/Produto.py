from tkinter import *
from tkinter import ttk, messagebox
import pymongo


class Produtos:

    def __init__(self):

        # =========================
        # JANELA
        # =========================

        self.tela = Tk()
        self.tela.title("CRUD Produtos MongoDB")
        self.tela.geometry("1000x700")
        self.tela.configure(bg="#f0f0f0")

        # =========================
        # CONEXÃO MONGO
        # =========================

        self.conexao = pymongo.MongoClient("mongodb://localhost:27017/")

        self.db = self.conexao["produtos"]

        self.collection = self.db["produtos"]

        self.criar_componentes()

    # ==================================================
    # COMPONENTES
    # ==================================================

    def criar_componentes(self):

        # TÍTULO
        Label(
            self.tela,
            text="Cadastro de Produtos",
            font=("Arial", 26, "bold"),
            bg="#f0f0f0",
            fg="#333"
        ).pack(pady=20)

        # FRAME FORMULÁRIO
        frame = Frame(self.tela, bg="#f0f0f0")
        frame.pack()

        # CÓDIGO
        Label(
            frame,
            text="Código:",
            font=("Arial", 11),
            bg="#f0f0f0"
        ).grid(row=0, column=0, pady=8, sticky=W)

        self.txt_codigo = Entry(frame, width=25, font=("Arial", 11))
        self.txt_codigo.grid(row=0, column=1)

        # NOME
        Label(
            frame,
            text="Nome:",
            font=("Arial", 11),
            bg="#f0f0f0"
        ).grid(row=1, column=0, pady=8, sticky=W)

        self.txt_nome = Entry(frame, width=40, font=("Arial", 11))
        self.txt_nome.grid(row=1, column=1)

        # QUANTIDADE
        Label(
            frame,
            text="Quantidade:",
            font=("Arial", 11),
            bg="#f0f0f0"
        ).grid(row=2, column=0, pady=8, sticky=W)

        self.txt_quantidade = Entry(frame, width=25, font=("Arial", 11))
        self.txt_quantidade.grid(row=2, column=1)

        # PREÇO
        Label(
            frame,
            text="Preço:",
            font=("Arial", 11),
            bg="#f0f0f0"
        ).grid(row=3, column=0, pady=8, sticky=W)

        self.txt_preco = Entry(frame, width=25, font=("Arial", 11))
        self.txt_preco.grid(row=3, column=1)

        # TOTAL
        Label(
            frame,
            text="Total:",
            font=("Arial", 11, "bold"),
            bg="#f0f0f0",
            fg="green"
        ).grid(row=4, column=0, pady=8, sticky=W)

        self.txt_total = Entry(
            frame,
            width=25,
            font=("Arial", 11, "bold"),
            state="readonly",
            readonlybackground="white",
            fg="green"
        )

        self.txt_total.grid(row=4, column=1)

        # =========================
        # ÍCONES
        # =========================

        self.foto_salvar = PhotoImage(file="icones/salvar.png")
        self.foto_consultar = PhotoImage(file="icones/consultar.png")
        self.foto_alterar = PhotoImage(file="icones/alterar.png")
        self.foto_excluir = PhotoImage(file="icones/excluir.png")
        self.foto_sair = PhotoImage(file="icones/sair.png")

        # =========================
        # FRAME BOTÕES
        # =========================

        frame_botoes = Frame(self.tela, bg="#f0f0f0")
        frame_botoes.pack(pady=20)

        # BOTÃO CADASTRAR
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

        # BOTÃO CONSULTAR
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

        # BOTÃO ALTERAR
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

        # BOTÃO EXCLUIR
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

        # BOTÃO SAIR
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

        # =========================
        # TABELA
        # =========================

        self.tabela = ttk.Treeview(
            self.tela,
            columns=("codigo", "nome", "quantidade", "preco", "total"),
            show="headings",
            height=10
        )

        self.tabela.heading("codigo", text="Código")
        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("quantidade", text="Quantidade")
        self.tabela.heading("preco", text="Preço")
        self.tabela.heading("total", text="Total")

        self.tabela.column("codigo", width=100)
        self.tabela.column("nome", width=250)
        self.tabela.column("quantidade", width=120)
        self.tabela.column("preco", width=120)
        self.tabela.column("total", width=120)

        self.tabela.pack(pady=20)

        self.listar_produtos()

    # ==================================================
    # MOSTRAR TOTAL
    # ==================================================

    def mostrar_total(self, valor):

        self.txt_total.config(state="normal")
        self.txt_total.delete(0, END)
        self.txt_total.insert(0, f"R$ {valor:.2f}")
        self.txt_total.config(state="readonly")

    # ==================================================
    # SALVAR
    # ==================================================

    def salvar(self):

        try:

            codigo = self.txt_codigo.get()
            nome = self.txt_nome.get()
            quantidade = int(self.txt_quantidade.get())
            preco = float(self.txt_preco.get())

            total = quantidade * preco

            produto = {

                "codigo": codigo,
                "nome": nome,
                "quantidade": quantidade,
                "preco": preco,
                "total": total
            }

            self.collection.insert_one(produto)

            self.mostrar_total(total)

            messagebox.showinfo(
                "Sucesso",
                "Produto cadastrado com sucesso!"
            )

            self.listar_produtos()

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                f"Erro ao salvar:\n{erro}"
            )

    # ==================================================
    # CONSULTAR
    # ==================================================

    def consultar(self):

        codigo = self.txt_codigo.get()

        resultado = self.collection.find_one({"codigo": codigo})

        if resultado:

            self.limpar()

            self.txt_codigo.insert(END, resultado["codigo"])
            self.txt_nome.insert(END, resultado["nome"])
            self.txt_quantidade.insert(END, resultado["quantidade"])
            self.txt_preco.insert(END, resultado["preco"])

            self.mostrar_total(resultado["total"])

        else:

            messagebox.showwarning(
                "Aviso",
                "Produto não encontrado!"
            )

    # ==================================================
    # ALTERAR
    # ==================================================

    def atualizar(self):

        try:

            codigo = self.txt_codigo.get()

            quantidade = int(self.txt_quantidade.get())

            preco = float(self.txt_preco.get())

            total = quantidade * preco

            self.collection.update_one(

                {"codigo": codigo},

                {"$set": {

                    "nome": self.txt_nome.get(),
                    "quantidade": quantidade,
                    "preco": preco,
                    "total": total
                }}
            )

            self.mostrar_total(total)

            messagebox.showinfo(
                "Sucesso",
                "Produto atualizado!"
            )

            self.listar_produtos()

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

    # ==================================================
    # EXCLUIR
    # ==================================================

    def excluir(self):

        codigo = self.txt_codigo.get()

        self.collection.delete_one({"codigo": codigo})

        messagebox.showinfo(
            "Sucesso",
            "Produto excluído!"
        )

        self.limpar()

        self.listar_produtos()

    # ==================================================
    # LISTAR
    # ==================================================

    def listar_produtos(self):

        for item in self.tabela.get_children():
            self.tabela.delete(item)

        produtos = self.collection.find()

        for produto in produtos:

            self.tabela.insert(
                "",
                END,
                values=(

                    produto.get("codigo", ""),
                    produto.get("nome", ""),
                    produto.get("quantidade", ""),
                    produto.get("preco", ""),
                    produto.get("total", "")
                )
            )

    # ==================================================
    # LIMPAR
    # ==================================================

    def limpar(self):

        self.txt_codigo.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_quantidade.delete(0, END)
        self.txt_preco.delete(0, END)

        self.txt_total.config(state="normal")
        self.txt_total.delete(0, END)
        self.txt_total.config(state="readonly")

    # ==================================================
    # EXECUTAR
    # ==================================================

    def executar(self):

        self.tela.mainloop()


# ==================================================
# INICIAR
# ==================================================

