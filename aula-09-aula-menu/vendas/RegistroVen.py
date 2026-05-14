from tkinter import *
from tkinter import ttk, messagebox
import pymongo


class RegistroVendas:

    def __init__(self):

        self.tela = Tk()

        self.tela.title("Registro de Vendas")

        self.tela.configure(bg="#f0f8ff")

        self.largura = 1000
        self.altura = 730

        self.centralizar_tela()

        self.conectar_banco()

        self.criar_componentes()

        self.carregar_produtos()

        self.tela.mainloop()

    # ==========================================
    # CENTRALIZAR
    # ==========================================

    def centralizar_tela(self):

        largura_screen = self.tela.winfo_screenwidth()

        altura_screen = self.tela.winfo_screenheight()

        posx = int(largura_screen / 2 - self.largura / 2)

        posy = int(altura_screen / 2 - self.altura / 2)

        self.tela.geometry(
            f"{self.largura}x{self.altura}+{posx}+{posy}"
        )

        self.tela.resizable(False, False)

    # ==========================================
    # BANCO
    # ==========================================

    def conectar_banco(self):

        self.cliente = pymongo.MongoClient(
            "mongodb://localhost:27017/"
        )

        self.db = self.cliente["empresa"]

        self.collection_vendas = self.db["vendas"]

        self.collection_produtos = self.db["produtos"]

        self.collection_clientes = self.db["clientes"]

    # ==========================================
    # COMPONENTES
    # ==========================================

    def criar_componentes(self):

        Label(
            self.tela,
            text="Registro de Vendas",
            font=("Arial", 24, "bold"),
            bg="#f0f8ff",
            fg="#1565c0"
        ).place(x=330, y=20)

        # ======================================
        # LABELS
        # ======================================

        Label(
            self.tela,
            text="ID Venda:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=100, y=90)

        Label(
            self.tela,
            text="ID Produto:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=100, y=140)

        Label(
            self.tela,
            text="Produto:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=100, y=190)

        Label(
            self.tela,
            text="Preço:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=520, y=190)

        Label(
            self.tela,
            text="ID Cliente:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=100, y=240)

        Label(
            self.tela,
            text="Cliente:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=100, y=290)

        Label(
            self.tela,
            text="Quantidade:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=100, y=340)

        Label(
            self.tela,
            text="Valor Total:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=520, y=340)

        # ======================================
        # CAMPOS
        # ======================================

        self.txt_id_venda = Entry(
            self.tela,
            width=20,
            font=("Arial", 11)
        )

        self.txt_id_produto = Entry(
            self.tela,
            width=20,
            font=("Arial", 11)
        )

        self.txt_produto = Entry(
            self.tela,
            width=35,
            font=("Arial", 11),
            state="readonly"
        )

        self.txt_preco = Entry(
            self.tela,
            width=20,
            font=("Arial", 11),
            state="readonly"
        )

        self.txt_id_cliente = Entry(
            self.tela,
            width=20,
            font=("Arial", 11)
        )

        self.txt_cliente = Entry(
            self.tela,
            width=35,
            font=("Arial", 11),
            state="readonly"
        )

        self.txt_quantidade = Entry(
            self.tela,
            width=20,
            font=("Arial", 11)
        )

        self.txt_total = Entry(
            self.tela,
            width=20,
            font=("Arial", 11),
            state="readonly"
        )

        # ======================================
        # POSIÇÕES
        # ======================================

        self.txt_id_venda.place(x=230, y=90)

        self.txt_id_produto.place(x=230, y=140)

        self.txt_produto.place(x=230, y=190)

        self.txt_preco.place(x=620, y=190)

        self.txt_id_cliente.place(x=230, y=240)

        self.txt_cliente.place(x=230, y=290)

        self.txt_quantidade.place(x=230, y=340)

        self.txt_total.place(x=620, y=340)

        # ======================================
        # EVENTOS
        # ======================================

        self.txt_id_produto.bind(
            "<FocusOut>",
            self.buscar_produto
        )

        self.txt_id_cliente.bind(
            "<FocusOut>",
            self.buscar_cliente
        )

        self.txt_quantidade.bind(
            "<KeyRelease>",
            self.calcular_total
        )

        # ======================================
        # BOTÕES
        # ======================================

        Button(
            self.tela,
            text="Salvar",
            width=15,
            bg="#2e7d32",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.salvar
        ).place(x=180, y=410)

        Button(
            self.tela,
            text="Consultar",
            width=15,
            bg="#1565c0",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.consultar
        ).place(x=380, y=410)

        Button(
            self.tela,
            text="Excluir",
            width=15,
            bg="#c62828",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.excluir
        ).place(x=580, y=410)

        # ======================================
        # TABELA PRODUTOS
        # ======================================

        Label(
            self.tela,
            text="Produtos Cadastrados",
            font=("Arial", 14, "bold"),
            bg="#f0f8ff",
            fg="#1565c0"
        ).place(x=360, y=480)

        self.tabela = ttk.Treeview(
            self.tela,
            columns=("id", "produto", "preco"),
            show="headings",
            height=8
        )

        self.tabela.heading("id", text="ID")

        self.tabela.heading("produto", text="Produto")

        self.tabela.heading("preco", text="Preço")

        self.tabela.column("id", width=100)

        self.tabela.column("produto", width=500)

        self.tabela.column("preco", width=150)

        self.tabela.place(x=120, y=520)

    # ==========================================
    # CARREGAR PRODUTOS
    # ==========================================

    def carregar_produtos(self):

        for item in self.tabela.get_children():

            self.tabela.delete(item)

        produtos = self.collection_produtos.find()

        for produto in produtos:

            self.tabela.insert(
                "",
                END,
                values=(
                    produto["codigo"],
                    produto["nome"],
                    produto["preco"]
                )
            )

    # ==========================================
    # BUSCAR PRODUTO
    # ==========================================

    def buscar_produto(self, event=None):

        codigo = self.txt_id_produto.get()

        produto = self.collection_produtos.find_one(
            {"codigo": codigo}
        )

        self.txt_produto.config(state="normal")

        self.txt_preco.config(state="normal")

        self.txt_produto.delete(0, END)

        self.txt_preco.delete(0, END)

        if produto:

            self.txt_produto.insert(
                0,
                produto["nome"]
            )

            self.txt_preco.insert(
                0,
                produto["preco"]
            )

        self.txt_produto.config(state="readonly")

        self.txt_preco.config(state="readonly")

        self.calcular_total()

    # ==========================================
    # BUSCAR CLIENTE
    # ==========================================

    def buscar_cliente(self, event=None):

        codigo = self.txt_id_cliente.get()

        cliente = self.collection_clientes.find_one(
            {"codigo": codigo}
        )

        self.txt_cliente.config(state="normal")

        self.txt_cliente.delete(0, END)

        if cliente:

            self.txt_cliente.insert(
                0,
                cliente["nome"]
            )

        self.txt_cliente.config(state="readonly")

    # ==========================================
    # CALCULAR TOTAL
    # ==========================================

    def calcular_total(self, event=None):

        try:

            qtd = float(
                self.txt_quantidade.get()
            )

            preco = float(
                self.txt_preco.get()
            )

            total = qtd * preco

            self.txt_total.config(state="normal")

            self.txt_total.delete(0, END)

            self.txt_total.insert(
                0,
                f"{total:.2f}"
            )

            self.txt_total.config(state="readonly")

        except:

            self.txt_total.config(state="normal")

            self.txt_total.delete(0, END)

            self.txt_total.config(state="readonly")

    # ==========================================
    # DADOS
    # ==========================================

    def dados(self):

        return {

            "id_venda": self.txt_id_venda.get(),

            "id_produto": self.txt_id_produto.get(),

            "produto": self.txt_produto.get(),

            "id_cliente": self.txt_id_cliente.get(),

            "cliente": self.txt_cliente.get(),

            "preco": self.txt_preco.get(),

            "quantidade": self.txt_quantidade.get(),

            "total": self.txt_total.get()
        }

    # ==========================================
    # SALVAR
    # ==========================================

    def salvar(self):

        self.collection_vendas.insert_one(
            self.dados()
        )

        messagebox.showinfo(
            "Sucesso",
            "Venda salva!"
        )

    # ==========================================
    # CONSULTAR
    # ==========================================

    def consultar(self):

        codigo = self.txt_id_venda.get()

        venda = self.collection_vendas.find_one(
            {"id_venda": codigo}
        )

        if venda:

            self.txt_id_produto.delete(0, END)

            self.txt_id_cliente.delete(0, END)

            self.txt_quantidade.delete(0, END)

            self.txt_id_produto.insert(
                0,
                venda["id_produto"]
            )

            self.txt_id_cliente.insert(
                0,
                venda["id_cliente"]
            )

            self.txt_quantidade.insert(
                0,
                venda["quantidade"]
            )

            self.buscar_produto()

            self.buscar_cliente()

        else:

            messagebox.showwarning(
                "Aviso",
                "Venda não encontrada!"
            )

    # ==========================================
    # EXCLUIR
    # ==========================================

    def excluir(self):

        codigo = self.txt_id_venda.get()

        self.collection_vendas.delete_one(
            {"id_venda": codigo}
        )

        messagebox.showinfo(
            "Sucesso",
            "Venda excluída!"
        )


# ==========================================
# EXECUTAR
# ==========================================

if __name__ == "__main__":

    RegistroVendas()