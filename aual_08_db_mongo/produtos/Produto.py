from tkinter import *
from tkinter import ttk, messagebox
import pymongo


class Produtos:

    def __init__(self):

        self.tela = Tk()
        self.tela.title("CRUD Produtos MongoDB")
        self.tela.geometry("900x600")
        self.tela.configure(bg="#f0f0f0")

        # CONEXÃO MONGO
        self.conexao = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.conexao["produtos"]
        self.collection = self.db["produtos"]

        self.criar_componentes()

    def criar_componentes(self):

        Label(
            self.tela,
            text="Cadastro de Produtos",
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#333"
        ).pack(pady=20)

        frame = Frame(self.tela, bg="#f0f0f0")
        frame.pack()

        # CÓDIGO
        Label(frame, text="Código:", bg="#f0f0f0").grid(row=0, column=0, pady=5)
        self.txt_codigo = Entry(frame, width=20)
        self.txt_codigo.grid(row=0, column=1)

        # NOME
        Label(frame, text="Nome:", bg="#f0f0f0").grid(row=1, column=0, pady=5)
        self.txt_nome = Entry(frame, width=40)
        self.txt_nome.grid(row=1, column=1)

        # QUANTIDADE
        Label(frame, text="Quantidade:", bg="#f0f0f0").grid(row=2, column=0, pady=5)
        self.txt_quantidade = Entry(frame, width=20)
        self.txt_quantidade.grid(row=2, column=1)

        # PREÇO
        Label(frame, text="Preço:", bg="#f0f0f0").grid(row=3, column=0, pady=5)
        self.txt_preco = Entry(frame, width=20)
        self.txt_preco.grid(row=3, column=1)

        # BOTÕES
        frame_botoes = Frame(self.tela, bg="#f0f0f0")
        frame_botoes.pack(pady=20)

        Button(
            frame_botoes,
            text="Cadastrar",
            width=15,
            bg="#4CAF50",
            fg="white",
            command=self.salvar
        ).grid(row=0, column=0, padx=10)

        Button(
            frame_botoes,
            text="Consultar",
            width=15,
            bg="#2196F3",
            fg="white",
            command=self.consultar
        ).grid(row=0, column=1, padx=10)

        Button(
            frame_botoes,
            text="Alterar",
            width=15,
            bg="#FFC107",
            command=self.atualizar
        ).grid(row=0, column=2, padx=10)

        Button(
            frame_botoes,
            text="Excluir",
            width=15,
            bg="#F44336",
            fg="white",
            command=self.excluir
        ).grid(row=0, column=3, padx=10)

        # TABELA
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

        self.tabela.pack(pady=20)

        self.listar_produtos()

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

            messagebox.showinfo("Sucesso", "Produto cadastrado!")

            self.limpar()
            self.listar_produtos()

        except Exception as erro:
            messagebox.showerror("Erro", f"Erro ao salvar:\n{erro}")

    def consultar(self):

        codigo = self.txt_codigo.get()

        resultado = self.collection.find_one({"codigo": codigo})

        if resultado:

            self.limpar()

            self.txt_codigo.insert(END, resultado["codigo"])
            self.txt_nome.insert(END, resultado["nome"])
            self.txt_quantidade.insert(END, resultado["quantidade"])
            self.txt_preco.insert(END, resultado["preco"])

        else:
            messagebox.showwarning("Aviso", "Produto não encontrado!")

    def atualizar(self):

        try:

            codigo = self.txt_codigo.get()

            quantidade = int(self.txt_quantidade.get())
            preco = float(self.txt_preco.get())

            total = quantidade * preco

            self.collection.update_one(
                {"codigo": codigo},
                {
                    "$set": {
                        "nome": self.txt_nome.get(),
                        "quantidade": quantidade,
                        "preco": preco,
                        "total": total
                    }
                }
            )

            messagebox.showinfo("Sucesso", "Produto atualizado!")

            self.limpar()
            self.listar_produtos()

        except Exception as erro:
            messagebox.showerror("Erro", str(erro))

    def excluir(self):

        codigo = self.txt_codigo.get()

        self.collection.delete_one({"codigo": codigo})

        messagebox.showinfo("Sucesso", "Produto excluído!")

        self.limpar()
        self.listar_produtos()

    def listar_produtos(self):

        for item in self.tabela.get_children():
            self.tabela.delete(item)

        produtos = self.collection.find()

        for produto in produtos:

            self.tabela.insert(
                "",
                END,
                values=(
                    produto["codigo"],
                    produto["nome"],
                    produto["quantidade"],
                    produto["preco"],
                    produto["total"]
                )
            )

    def limpar(self):

        self.txt_codigo.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_quantidade.delete(0, END)
        self.txt_preco.delete(0, END)

    def executar(self):
        self.tela.mainloop()


