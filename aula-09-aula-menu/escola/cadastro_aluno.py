from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient


class TelaAlunos:

    def __init__(self):

        # ================= CONEXÃO MONGODB =================

        self.cliente = MongoClient(
            "mongodb://localhost:27017/"
        )

        self.banco = self.cliente["escola"]

        self.colecao = self.banco["alunos"]

        # ================= TELA =================

        self.tela = Tk()
        self.tela.title("Cadastro de Alunos")
        self.tela.geometry("750x500")
        self.tela.resizable(False, False)

        # ================= TÍTULO =================

        Label(
            self.tela,
            text="Cadastro de Alunos",
            font=("Arial", 22, "bold"),
            fg="blue"
        ).place(x=220, y=20)

        # ================= LABELS =================

        Label(self.tela, text="Código:").place(x=100, y=100)
        Label(self.tela, text="Nome do Aluno:").place(x=100, y=150)
        Label(self.tela, text="Data Nascimento:").place(x=100, y=200)
        Label(self.tela, text="Endereço:").place(x=100, y=250)
        Label(self.tela, text="Telefone:").place(x=100, y=300)

        # ================= CAMPOS =================

        self.codigo = Entry(self.tela, width=20)
        self.nome = Entry(self.tela, width=40)
        self.data = Entry(self.tela, width=30)
        self.endereco = Entry(self.tela, width=40)
        self.telefone = Entry(self.tela, width=30)

        self.codigo.place(x=250, y=100)
        self.nome.place(x=250, y=150)
        self.data.place(x=250, y=200)
        self.endereco.place(x=250, y=250)
        self.telefone.place(x=250, y=300)

        # ================= ÍCONES =================

        self.img_salvar = PhotoImage(file="icones/salvar.png")
        self.img_consultar = PhotoImage(file="icones/consultar.png")
        self.img_alterar = PhotoImage(file="icones/alterar.png")
        self.img_excluir = PhotoImage(file="icones/excluir.png")

        # ================= BOTÕES =================

        Button(
            self.tela,
            text="Cadastrar",
            image=self.img_salvar,
            compound=TOP,
            command=self.cadastrar
        ).place(x=120, y=380)

        Button(
            self.tela,
            text="Consultar",
            image=self.img_consultar,
            compound=TOP,
            command=self.consultar
        ).place(x=260, y=380)

        Button(
            self.tela,
            text="Editar",
            image=self.img_alterar,
            compound=TOP,
            command=self.editar
        ).place(x=400, y=380)

        Button(
            self.tela,
            text="Excluir",
            image=self.img_excluir,
            compound=TOP,
            command=self.excluir
        ).place(x=540, y=380)

        self.tela.mainloop()

    # ================= CADASTRAR =================

    def cadastrar(self):

        codigo = self.codigo.get()
        nome = self.nome.get()
        data = self.data.get()
        endereco = self.endereco.get()
        telefone = self.telefone.get()

        # VALIDAR CAMPOS

        if (
            codigo == "" or
            nome == "" or
            data == "" or
            endereco == "" or
            telefone == ""
        ):

            messagebox.showerror(
                "Erro",
                "Preencha todos os campos!"
            )

            return

        # VERIFICAR DUPLICADO

        aluno_existente = self.colecao.find_one({
            "codigo": codigo
        })

        if aluno_existente:

            messagebox.showwarning(
                "Cadastro",
                "Já existe um aluno com esse código!"
            )

            return

        # INSERIR

        aluno = {

            "codigo": codigo,
            "nome": nome,
            "data_nascimento": data,
            "endereco": endereco,
            "telefone": telefone

        }

        self.colecao.insert_one(aluno)

        messagebox.showinfo(
            "Cadastro",
            "Aluno cadastrado com sucesso!"
        )

        self.limpar_campos()

    # ================= CONSULTAR =================

    def consultar(self):

        codigo = self.codigo.get()

        if codigo == "":

            messagebox.showerror(
                "Erro",
                "Digite o código!"
            )

            return

        aluno = self.colecao.find_one({
            "codigo": codigo
        })

        if aluno:

            self.nome.delete(0, END)
            self.nome.insert(0, aluno["nome"])

            self.data.delete(0, END)
            self.data.insert(
                0,
                aluno["data_nascimento"]
            )

            self.endereco.delete(0, END)
            self.endereco.insert(
                0,
                aluno["endereco"]
            )

            self.telefone.delete(0, END)
            self.telefone.insert(
                0,
                aluno["telefone"]
            )

            messagebox.showinfo(
                "Consulta",
                "Aluno encontrado!"
            )

        else:

            messagebox.showwarning(
                "Consulta",
                "Aluno não encontrado!"
            )

    # ================= EDITAR =================

    def editar(self):

        codigo = self.codigo.get()
        nome = self.nome.get()
        data = self.data.get()
        endereco = self.endereco.get()
        telefone = self.telefone.get()

        # VALIDAR CAMPOS

        if (
            codigo == "" or
            nome == "" or
            data == "" or
            endereco == "" or
            telefone == ""
        ):

            messagebox.showerror(
                "Erro",
                "Preencha todos os campos!"
            )

            return

        resultado = self.colecao.update_one(

            {"codigo": codigo},

            {
                "$set": {

                    "nome": nome,
                    "data_nascimento": data,
                    "endereco": endereco,
                    "telefone": telefone

                }
            }
        )

        if resultado.modified_count > 0:

            messagebox.showinfo(
                "Editar",
                "Aluno alterado com sucesso!"
            )

            self.limpar_campos()

        else:

            messagebox.showwarning(
                "Editar",
                "Aluno não encontrado!"
            )

    # ================= EXCLUIR =================

    def excluir(self):

        codigo = self.codigo.get()

        if codigo == "":

            messagebox.showerror(
                "Erro",
                "Digite o código!"
            )

            return

        resultado = self.colecao.delete_one({
            "codigo": codigo
        })

        if resultado.deleted_count > 0:

            messagebox.showinfo(
                "Excluir",
                "Aluno excluído!"
            )

            self.limpar_campos()

        else:

            messagebox.showwarning(
                "Excluir",
                "Aluno não encontrado!"
            )

    # ================= LIMPAR CAMPOS =================

    def limpar_campos(self):

        self.codigo.delete(0, END)
        self.nome.delete(0, END)
        self.data.delete(0, END)
        self.endereco.delete(0, END)
        self.telefone.delete(0, END)


# ================= EXECUTAR =================

if __name__ == "__main__":
    TelaAlunos()