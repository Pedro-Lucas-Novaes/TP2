from tkinter import *
from tkinter import ttk, messagebox
import pymongo


class RegistroVendas:

    def __init__(self):

        self.tela = Tk()

        self.tela.title("Registro de Vendas")

        self.tela.configure(bg="#f0f8ff")

        self.largura = 1200
        self.altura = 750

        self.centralizar_tela()

        self.conectar_banco()

        self.criar_componentes()

        self.carregar_produtos()

        self.carregar_vendas()

        self.tela.mainloop()

    def centralizar_tela(self):

        largura_screen = self.tela.winfo_screenwidth()

        altura_screen = self.tela.winfo_screenheight()

        posx = int(largura_screen / 2 - self.largura / 2)

        posy = int(altura_screen / 2 - self.altura / 2)

        self.tela.geometry(
            f"{self.largura}x{self.altura}+{posx}+{posy}"
        )

        self.tela.resizable(False, False)

    def conectar_banco(self):

        self.cliente = pymongo.MongoClient(
            "mongodb://localhost:27017/"
        )

        self.db = self.cliente["empresa"]

        self.collection_vendas = self.db["vendas"]

        self.collection_produtos = self.db["produto"]

        self.collection_clientes = self.db["clientes"]

    def criar_componentes(self):

        Label(
            self.tela,
            text="REGISTRO DE VENDAS",
            font=("Arial", 24, "bold"),
            bg="#f0f8ff",
            fg="#1565c0"
        ).place(x=360, y=20)

        Label(
            self.tela,
            text="ID Venda:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=60, y=100)

        Label(
            self.tela,
            text="ID Produto:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=60, y=150)

        Label(
            self.tela,
            text="Produto:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=60, y=200)

        Label(
            self.tela,
            text="Preço:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=500, y=200)

        Label(
            self.tela,
            text="ID Cliente:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=60, y=250)

        Label(
            self.tela,
            text="Cliente:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=60, y=300)

        Label(
            self.tela,
            text="Quantidade:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=60, y=350)

        Label(
            self.tela,
            text="Valor Total:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=500, y=350)

        Label(
            self.tela,
            text="Buscar Venda:",
            bg="#f0f8ff",
            font=("Arial", 11, "bold")
        ).place(x=850, y=100)

        self.txt_id_venda = Entry(
            self.tela,
            width=25,
            font=("Arial", 11)
        )

        self.txt_id_produto = Entry(
            self.tela,
            width=25,
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
            width=25,
            font=("Arial", 11),
            state="readonly"
        )

        self.txt_id_cliente = Entry(
            self.tela,
            width=25,
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
            width=25,
            font=("Arial", 11)
        )

        self.txt_total = Entry(
            self.tela,
            width=25,
            font=("Arial", 11),
            state="readonly"
        )

        self.txt_buscar = Entry(
            self.tela,
            width=20,
            font=("Arial", 11)
        )

        self.txt_id_venda.place(x=180, y=100)

        self.txt_id_produto.place(x=180, y=150)

        self.txt_produto.place(x=180, y=200)

        self.txt_preco.place(x=620, y=200)

        self.txt_id_cliente.place(x=180, y=250)

        self.txt_cliente.place(x=180, y=300)

        self.txt_quantidade.place(x=180, y=350)

        self.txt_total.place(x=620, y=350)

        self.txt_buscar.place(x=980, y=100)

        self.txt_id_produto.bind(
            "<FocusOut>",
            self.buscar_produto
        )

        self.txt_id_cliente.bind(
            "<FocusOut>",
            self.buscar_cliente
        )

        self.foto_salvar = PhotoImage(
            file=r"icones\salvar.png"
        )

        self.foto_alterar = PhotoImage(
            file=r"icones\alterar.png"
        )

        self.foto_consultar = PhotoImage(
            file=r"icones\consultar.png"
        )

        self.foto_excluir = PhotoImage(
            file=r"icones\excluir.png"
        )

        self.foto_sair = PhotoImage(
            file=r"icones\sair.png"
        )

        Button(
            self.tela,
            text="Salvar",
            image=self.foto_salvar,
            compound=TOP,
            width=90,
            height=90,
            command=self.salvar
        ).place(x=120, y=420)

        Button(
            self.tela,
            text="Alterar",
            image=self.foto_alterar,
            compound=TOP,
            width=90,
            height=90,
            command=self.alterar
        ).place(x=260, y=420)

        Button(
            self.tela,
            text="Consultar",
            image=self.foto_consultar,
            compound=TOP,
            width=90,
            height=90,
            command=self.consultar
        ).place(x=400, y=420)

        Button(
            self.tela,
            text="Excluir",
            image=self.foto_excluir,
            compound=TOP,
            width=90,
            height=90,
            command=self.excluir
        ).place(x=540, y=420)

        Button(
            self.tela,
            text="Sair",
            image=self.foto_sair,
            compound=TOP,
            width=90,
            height=90,
            command=self.tela.destroy
        ).place(x=680, y=420)

        Label(
            self.tela,
            text="VENDAS CADASTRADAS",
            font=("Arial", 15, "bold"),
            bg="#f0f8ff",
            fg="#1565c0"
        ).place(x=430, y=540)

        self.tabela = ttk.Treeview(
            self.tela,
            columns=(
                "id",
                "cliente",
                "produto",
                "quantidade",
                "preco",
                "total"
            ),
            show="headings",
            height=8
        )

        self.tabela.heading("id", text="ID")

        self.tabela.heading("cliente", text="Cliente")

        self.tabela.heading("produto", text="Produto")

        self.tabela.heading("quantidade", text="Quantidade")

        self.tabela.heading("preco", text="Preço")

        self.tabela.heading("total", text="Total")

        self.tabela.column("id", width=80)

        self.tabela.column("cliente", width=220)

        self.tabela.column("produto", width=220)

        self.tabela.column("quantidade", width=100)

        self.tabela.column("preco", width=100)

        self.tabela.column("total", width=100)

        self.tabela.place(x=80, y=580)

    def carregar_vendas(self):

        for item in self.tabela.get_children():

            self.tabela.delete(item)

        vendas = self.collection_vendas.find()

        for venda in vendas:

            self.tabela.insert(
                "",
                END,
                values=(

                    venda.get("id_venda", ""),

                    venda.get("cliente", ""),

                    venda.get("produto", ""),

                    venda.get("quantidade", ""),

                    venda.get("preco", ""),

                    venda.get("total", "")
                )
            )

    def carregar_produtos(self):

        pass

    def buscar_produto(self, event=None):

        codigo = self.txt_id_produto.get()

        produto = self.collection_produtos.find_one(
        {"codigo": codigo}
    )

        self.txt_produto.config(state="normal")

        self.txt_preco.config(state="normal")

        self.txt_quantidade.delete(0, END)

        self.txt_total.config(state="normal")

        self.txt_produto.delete(0, END)

        self.txt_preco.delete(0, END)

        self.txt_total.delete(0, END)

        if produto:

        # Nome produto
            self.txt_produto.insert(
            0,
            produto["nomeProduto"]
        )

        # Preço
        self.txt_preco.insert(
            0,
            produto["preco"]
        )

        # Quantidade cadastrada
        self.txt_quantidade.insert(
            0,
            produto["quantidade"]
        )

        # Total já calculado no cadastro produto
        self.txt_total.insert(
            0,
            produto["total"]
        )

        self.txt_produto.config(state="readonly")

        self.txt_preco.config(state="readonly")

        self.txt_total.config(state="readonly")

        self.calcular_total()

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
                cliente["nomeCliente"]
            )

        self.txt_cliente.config(state="readonly")

    def limpar_campos(self):

        self.txt_id_venda.delete(0, END)

        self.txt_id_produto.delete(0, END)

        self.txt_produto.config(state="normal")
        self.txt_produto.delete(0, END)
        self.txt_produto.config(state="readonly")

        self.txt_preco.config(state="normal")
        self.txt_preco.delete(0, END)
        self.txt_preco.config(state="readonly")

        self.txt_id_cliente.delete(0, END)

        self.txt_cliente.config(state="normal")
        self.txt_cliente.delete(0, END)
        self.txt_cliente.config(state="readonly")

        self.txt_quantidade.delete(0, END)

        self.txt_total.config(state="normal")
        self.txt_total.delete(0, END)
        self.txt_total.config(state="readonly")

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

    def salvar(self):

        existe = self.collection_vendas.find_one(
            {"id_venda": self.txt_id_venda.get()}
        )

        if existe:

            messagebox.showwarning(
                "Aviso",
                "ID da venda já cadastrado!"
            )

            return

        self.collection_vendas.insert_one(
            self.dados()
        )

        self.carregar_vendas()

        self.limpar_campos()

        messagebox.showinfo(
            "Sucesso",
            "Venda cadastrada!"
        )

    def consultar(self):

        codigo = self.txt_buscar.get()

        venda = self.collection_vendas.find_one(
            {"id_venda": codigo}
        )

        if venda:

            self.limpar_campos()

            self.txt_id_venda.insert(
                0,
                venda["id_venda"]
            )

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

            self.calcular_total()

        else:

            messagebox.showwarning(
                "Aviso",
                "Venda não encontrada!"
            )

    def alterar(self):

        codigo = self.txt_id_venda.get()

        venda = self.collection_vendas.find_one(
            {"id_venda": codigo}
        )

        if venda:

            self.collection_vendas.update_one(

                {"id_venda": codigo},

                {
                    "$set": self.dados()
                }
            )

            self.carregar_vendas()

            self.limpar_campos()

            messagebox.showinfo(
                "Sucesso",
                "Venda alterada!"
            )

        else:

            messagebox.showwarning(
                "Aviso",
                "Venda não encontrada!"
            )

    def excluir(self):

        codigo = self.txt_id_venda.get()

        venda = self.collection_vendas.find_one(
            {"id_venda": codigo}
        )

        if venda:

            self.collection_vendas.delete_one(
                {"id_venda": codigo}
            )

            self.carregar_vendas()

            self.limpar_campos()

            messagebox.showinfo(
                "Sucesso",
                "Venda excluída!"
            )

        else:

            messagebox.showwarning(
                "Aviso",
                "Venda não encontrada!"
            )

if __name__ == "__main__":

    RegistroVendas()