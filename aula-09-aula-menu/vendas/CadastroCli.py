from tkinter import *
from tkinter import ttk, messagebox
import pymongo


class Cliente:

    def __init__(self):

        self.tela = Tk()

        self.tela.title("Cliente")

        self.tela.configure(bg="#f0f8ff")

        self.largura = 700
        self.altura = 500

        self.centralizar_tela()

        self.conectar_banco()

        self.criar_componentes()

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

        self.collection = self.db["clientes"]

    def criar_componentes(self):

        self.criar_labels()

        self.criar_campos()

        self.criar_botoes()

    def criar_labels(self):

        Label(
            self.tela,
            text="Cliente",
            font=("Arial", 24, "bold"),
            bg="#f0f8ff",
            fg="#1565c0"
        ).place(x=280, y=20)

        Label(
            self.tela,
            text="Código:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=120, y=100)

        Label(
            self.tela,
            text="Nome Cliente:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=120, y=150)

        Label(
            self.tela,
            text="CPF:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=120, y=200)

        Label(
            self.tela,
            text="Telefone:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=120, y=250)

        Label(
            self.tela,
            text="Endereço:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=120, y=300)

    def criar_campos(self):

        self.txt_codigo = Entry(
            self.tela,
            width=30,
            font=("Arial", 11)
        )

        self.txt_nome = Entry(
            self.tela,
            width=45,
            font=("Arial", 11)
        )

        self.txt_cpf = Entry(
            self.tela,
            width=30,
            font=("Arial", 11)
        )

        self.txt_telefone = Entry(
            self.tela,
            width=30,
            font=("Arial", 11)
        )

        self.txt_endereco = Entry(
            self.tela,
            width=45,
            font=("Arial", 11)
        )

        # POSIÇÕES

        self.txt_codigo.place(x=250, y=100)

        self.txt_nome.place(x=250, y=150)

        self.txt_cpf.place(x=250, y=200)

        self.txt_telefone.place(x=250, y=250)

        self.txt_endereco.place(x=250, y=300)

    def criar_botoes(self):

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
            command=self.cadastrarCliente
        ).place(x=70, y=380)

        Button(
            self.tela,
            text="Alterar",
            image=self.foto_alterar,
            compound=TOP,
            width=90,
            height=90,
            command=self.alterar
        ).place(x=190, y=380)

        Button(
            self.tela,
            text="Consultar",
            image=self.foto_consultar,
            compound=TOP,
            width=90,
            height=90,
            command=self.mostrarCliente
        ).place(x=310, y=380)

        Button(
            self.tela,
            text="Excluir",
            image=self.foto_excluir,
            compound=TOP,
            width=90,
            height=90,
            command=self.excluir
        ).place(x=430, y=380)

        Button(
            self.tela,
            text="Sair",
            image=self.foto_sair,
            compound=TOP,
            width=90,
            height=90,
            command=self.tela.destroy
        ).place(x=550, y=380)

    def limpar_campos(self):

        self.txt_codigo.delete(0, END)

        self.txt_nome.delete(0, END)

        self.txt_cpf.delete(0, END)

        self.txt_telefone.delete(0, END)

        self.txt_endereco.delete(0, END)

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
                "Digite o nome do cliente!"
            )

            self.txt_nome.focus()

            return False

        elif self.txt_cpf.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite o CPF!"
            )

            self.txt_cpf.focus()

            return False

        elif self.txt_telefone.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite o telefone!"
            )

            self.txt_telefone.focus()

            return False

        elif self.txt_endereco.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite o endereço!"
            )

            self.txt_endereco.focus()

            return False

        return True

    def dados(self):

        return {

            "codigo": self.txt_codigo.get(),

            "nomeCliente": self.txt_nome.get(),

            "cpf": self.txt_cpf.get(),

            "telefone": self.txt_telefone.get(),

            "endereco": self.txt_endereco.get()
        }

    def cadastrarCliente(self):

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
                "Cliente cadastrado!"
            )

            self.limpar_campos()

    def mostrarCliente(self):

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
                resultado["nomeCliente"]
            )

            self.txt_cpf.insert(
                0,
                resultado["cpf"]
            )

            self.txt_telefone.insert(
                0,
                resultado["telefone"]
            )

            self.txt_endereco.insert(
                0,
                resultado["endereco"]
            )

        else:

            messagebox.showwarning(
                "Aviso",
                "Cliente não encontrado!"
            )

    def alterar(self):

        if self.validar_campos():

            codigo = self.txt_codigo.get()

            resultado = self.collection.find_one(
                {"codigo": codigo}
            )

            if resultado:

                self.collection.update_one(

                    {"codigo": codigo},

                    {
                        "$set": self.dados()
                    }
                )

                messagebox.showinfo(
                    "Sucesso",
                    "Cliente alterado!"
                )

                self.limpar_campos()

            else:

                messagebox.showwarning(
                    "Aviso",
                    "Cliente não encontrado!"
                )

    def excluir(self):

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

            self.collection.delete_one(
                {"codigo": codigo}
            )

            messagebox.showinfo(
                "Sucesso",
                "Cliente excluído!"
            )

            self.limpar_campos()

        else:

            messagebox.showwarning(
                "Aviso",
                "Cliente não encontrado!"
            )


if __name__ == "__main__":

    Cliente()