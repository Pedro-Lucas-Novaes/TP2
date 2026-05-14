from tkinter import *
from tkinter import messagebox
import pymongo


class Produto:

    def __init__(self):

        self.tela = Tk()

        self.tela.title("Produto")

        self.tela.configure(bg="#f0f8ff")

        self.largura = 700
        self.altura = 500

        self.centralizar_tela()

        self.conectar_banco()

        self.criar_labels()

        self.criar_campos()

        self.criar_botoes()

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

        self.collection = self.db["produto"]

    def criar_labels(self):

        Label(
            self.tela,
            text="Produto",
            font=("Arial", 24, "bold"),
            bg="#f0f8ff",
            fg="#1565c0"
        ).place(x=280, y=20)

        Label(
            self.tela,
            text="Código:",
            bg="#f0f8ff",
            font=("Arial", 12)
        ).place(x=120, y=100)

        Label(
            self.tela,
            text="Nome Produto:",
            bg="#f0f8ff",
            font=("Arial", 12)
        ).place(x=120, y=150)

        Label(
            self.tela,
            text="Quantidade:",
            bg="#f0f8ff",
            font=("Arial", 12)
        ).place(x=120, y=200)

        Label(
            self.tela,
            text="Preço:",
            bg="#f0f8ff",
            font=("Arial", 12)
        ).place(x=120, y=250)

        Label(
            self.tela,
            text="Total:",
            bg="#f0f8ff",
            font=("Arial", 12)
        ).place(x=120, y=300)

    def criar_campos(self):

        self.txt_codigo = Entry(
            self.tela,
            width=35,
            font=("Arial", 11)
        )

        self.txt_nome = Entry(
            self.tela,
            width=35,
            font=("Arial", 11)
        )

        self.txt_quantidade = Entry(
            self.tela,
            width=35,
            font=("Arial", 11)
        )

        self.txt_preco = Entry(
            self.tela,
            width=35,
            font=("Arial", 11)
        )

        self.txt_total = Entry(
            self.tela,
            width=35,
            font=("Arial", 11),
            state="readonly"
        )

        # POSIÇÕES

        self.txt_codigo.place(x=260, y=100)

        self.txt_nome.place(x=260, y=150)

        self.txt_quantidade.place(x=260, y=200)

        self.txt_preco.place(x=260, y=250)

        self.txt_total.place(x=260, y=300)

        # EVENTOS

        self.txt_quantidade.bind(
            "<KeyRelease>",
            self.calcular_total
        )

        self.txt_preco.bind(
            "<KeyRelease>",
            self.calcular_total
        )

    def criar_botoes(self):

        self.foto_salvar = PhotoImage(
            file=r"icones\salvar.png"
        )

        self.foto_consultar = PhotoImage(
            file=r"icones\consultar.png"
        )

        Button(
            self.tela,
            text="Cadastrar Produto",
            image=self.foto_salvar,
            compound=TOP,
            width=130,
            height=100,
            command=self.cadastrarProduto
        ).place(x=180, y=370)

        Button(
            self.tela,
            text="Consultar Produto",
            image=self.foto_consultar,
            compound=TOP,
            width=130,
            height=100,
            command=self.consultarProduto
        ).place(x=390, y=370)

    def calcular_total(self, event=None):

        quantidade = self.txt_quantidade.get()

        preco = self.txt_preco.get()

        try:

            total = float(quantidade) * float(preco)

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

    def validar_campos(self):

        if self.txt_codigo.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite o código!"
            )

            self.txt_codigo.focus()

            return False

        elif self.txt_nome.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite o nome do produto!"
            )

            self.txt_nome.focus()

            return False

        elif self.txt_quantidade.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite a quantidade!"
            )

            self.txt_quantidade.focus()

            return False

        elif self.txt_preco.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite o preço!"
            )

            self.txt_preco.focus()

            return False

        return True

    def dados(self):

        return {

            "codigo": self.txt_codigo.get(),

            "nomeProduto": self.txt_nome.get(),

            "quantidade": self.txt_quantidade.get(),

            "preco": self.txt_preco.get(),

            "total": self.txt_total.get()
        }

    def limpar_campos(self):

        self.txt_codigo.delete(0, END)

        self.txt_nome.delete(0, END)

        self.txt_quantidade.delete(0, END)

        self.txt_preco.delete(0, END)

        self.txt_total.config(state="normal")

        self.txt_total.delete(0, END)

        self.txt_total.config(state="readonly")

    def cadastrarProduto(self):

        if self.validar_campos():

            existe = self.collection.find_one(
                {"codigo": self.txt_codigo.get()}
            )

            if existe:

                messagebox.showwarning(
                    "Aviso",
                    "Código já cadastrado!"
                )

                return

            self.collection.insert_one(
                self.dados()
            )

            messagebox.showinfo(
                "Sucesso",
                "Produto cadastrado!"
            )

            self.limpar_campos()

    def consultarProduto(self):

        codigo = self.txt_codigo.get()

        if codigo == "":

            messagebox.showwarning(
                "Aviso",
                "Digite o código!"
            )

            return

        resultado = self.collection.find_one(
            {"codigo": codigo}
        )

        if resultado:

            self.limpar_campos()

            self.txt_codigo.insert(
                0,
                resultado["codigo"]
            )

            self.txt_nome.insert(
                0,
                resultado["nomeProduto"]
            )

            self.txt_quantidade.insert(
                0,
                resultado["quantidade"]
            )

            self.txt_preco.insert(
                0,
                resultado["preco"]
            )

            self.txt_total.config(state="normal")

            self.txt_total.insert(
                0,
                resultado["total"]
            )

            self.txt_total.config(state="readonly")

        else:

            messagebox.showwarning(
                "Aviso",
                "Produto não encontrado!"
            )

if __name__ == "__main__":

    Produto()