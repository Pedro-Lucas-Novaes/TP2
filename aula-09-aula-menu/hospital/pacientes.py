from tkinter import *
from tkinter import ttk, messagebox
import pymongo


class CadastroPacientes:

    def __init__(self):

        self.tela = Tk()
        self.tela.title("Cadastro de Pacientes")
        self.tela.geometry("850x520")
        self.tela.configure(bg="#f0f8ff")
        self.tela.resizable(False, False)

        self.conectar_banco()


        self.criar_icones()


        self.criar_componentes()

        self.tela.mainloop()

    def conectar_banco(self):

        self.cliente = pymongo.MongoClient(
            "mongodb://localhost:27017/"
        )

        self.db = self.cliente["hospital"]

        self.collection = self.db["pacientes"]

    def criar_icones(self):

        self.foto_salvar = PhotoImage(
            file=r"icones\salvar.png"
        )

        self.foto_alterar = PhotoImage(
            file=r"icones\alterar.png"
        )

        self.foto_excluir = PhotoImage(
            file=r"icones\excluir.png"
        )

        self.foto_consultar = PhotoImage(
            file=r"icones\consultar.png"
        )

        self.foto_sair = PhotoImage(
            file=r"icones\sair.png"
        )

    def criar_componentes(self):

        titulo = Label(
            self.tela,
            text="Cadastro de Pacientes",
            font=("Arial", 24, "bold"),
            bg="#f0f8ff",
            fg="#1565c0"
        )

        titulo.pack(pady=20)

        # FRAME PRINCIPAL

        frame = Frame(
            self.tela,
            bg="#f0f8ff"
        )

        frame.pack(pady=10)

        Label(
            frame,
            text="Código:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).grid(row=0, column=0, sticky=W, pady=5)

        Label(
            frame,
            text="Nome:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).grid(row=1, column=0, sticky=W, pady=5)

        Label(
            frame,
            text="CPF:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).grid(row=2, column=0, sticky=W, pady=5)

        Label(
            frame,
            text="Telefone:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).grid(row=3, column=0, sticky=W, pady=5)

        Label(
            frame,
            text="Sexo:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).grid(row=4, column=0, sticky=W, pady=5)

        Label(
            frame,
            text="Convênio:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).grid(row=5, column=0, sticky=W, pady=5)

        self.txt_codigo = Entry(
            frame,
            width=35,
            font=("Arial", 11)
        )

        self.txt_nome = Entry(
            frame,
            width=35,
            font=("Arial", 11)
        )

        self.txt_cpf = Entry(
            frame,
            width=35,
            font=("Arial", 11)
        )

        self.txt_telefone = Entry(
            frame,
            width=35,
            font=("Arial", 11)
        )

        self.combo_sexo = ttk.Combobox(
            frame,
            values=[
                "Masculino",
                "Feminino",
                "Outro"
            ],
            width=32,
            state="readonly"
        )

        self.txt_convenio = Entry(
            frame,
            width=35,
            font=("Arial", 11)
        )

        self.txt_codigo.grid(
            row=0,
            column=1,
            pady=5,
            padx=10
        )

        self.txt_nome.grid(
            row=1,
            column=1,
            pady=5,
            padx=10
        )

        self.txt_cpf.grid(
            row=2,
            column=1,
            pady=5,
            padx=10
        )

        self.txt_telefone.grid(
            row=3,
            column=1,
            pady=5,
            padx=10
        )

        self.combo_sexo.grid(
            row=4,
            column=1,
            pady=5,
            padx=10
        )

        self.txt_convenio.grid(
            row=5,
            column=1,
            pady=5,
            padx=10
        )

        frame_btn = Frame(
            self.tela,
            bg="#f0f8ff"
        )

        frame_btn.pack(pady=30)

        Button(
            frame_btn,
            text="Salvar",
            image=self.foto_salvar,
            compound=TOP,
            width=90,
            height=90,
            command=self.salvar
        ).grid(row=0, column=0, padx=10)

        Button(
            frame_btn,
            text="Consultar",
            image=self.foto_consultar,
            compound=TOP,
            width=90,
            height=90,
            command=self.consultar
        ).grid(row=0, column=1, padx=10)

        Button(
            frame_btn,
            text="Alterar",
            image=self.foto_alterar,
            compound=TOP,
            width=90,
            height=90,
            command=self.alterar
        ).grid(row=0, column=2, padx=10)

        Button(
            frame_btn,
            text="Excluir",
            image=self.foto_excluir,
            compound=TOP,
            width=90,
            height=90,
            command=self.apagar
        ).grid(row=0, column=3, padx=10)

        Button(
            frame_btn,
            text="Sair",
            image=self.foto_sair,
            compound=TOP,
            width=90,
            height=90,
            command=self.tela.destroy
        ).grid(row=0, column=4, padx=10)

    def limpar_campos(self):

        self.txt_codigo.delete(0, END)
        self.txt_nome.delete(0, END)
        self.txt_cpf.delete(0, END)
        self.txt_telefone.delete(0, END)
        self.combo_sexo.set("")
        self.txt_convenio.delete(0, END)

    def dados(self):

        return {

            "codigo": self.txt_codigo.get(),
            "nome": self.txt_nome.get(),
            "cpf": self.txt_cpf.get(),
            "telefone": self.txt_telefone.get(),
            "sexo": self.combo_sexo.get(),
            "convenio": self.txt_convenio.get()
        }

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
                "Digite o nome!"
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

        elif self.combo_sexo.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Selecione o sexo!"
            )

            self.combo_sexo.focus()

            return False

        elif self.txt_convenio.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite o convênio!"
            )

            self.txt_convenio.focus()

            return False

        return True

    def salvar(self):

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
                "Paciente cadastrado!"
            )

            self.limpar_campos()

    def consultar(self):

        codigo = self.txt_codigo.get()

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
                resultado["nome"]
            )

            self.txt_cpf.insert(
                0,
                resultado["cpf"]
            )

            self.txt_telefone.insert(
                0,
                resultado["telefone"]
            )

            self.combo_sexo.set(
                resultado["sexo"]
            )

            self.txt_convenio.insert(
                0,
                resultado["convenio"]
            )

        else:

            messagebox.showwarning(
                "Aviso",
                "Paciente não encontrado!"
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
                    "Paciente alterado!"
                )

                self.limpar_campos()

            else:

                messagebox.showwarning(
                    "Aviso",
                    "Paciente não encontrado!"
                )

    def apagar(self):

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
                "Paciente excluído!"
            )

            self.limpar_campos()

        else:

            messagebox.showwarning(
                "Aviso",
                "Paciente não encontrado!"
            )


if __name__ == "__main__":

    CadastroPacientes()