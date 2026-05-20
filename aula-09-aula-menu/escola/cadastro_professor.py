from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient


class TelaProfessores:

    def __init__(self):

        # ================= CONEXÃO MONGODB =================

        self.cliente = MongoClient(
            "mongodb://localhost:27017/"
        )

        self.banco = self.cliente["escola"]

        self.colecao = self.banco["professores"]

        # ================= TELA =================

        self.tela = Tk()
        self.tela.title("Cadastro de Professores")
        self.tela.geometry("750x500")
        self.tela.resizable(False, False)

        # ================= TÍTULO =================

        Label(
            self.tela,
            text="Cadastro de Professores",
            font=("Arial", 22, "bold"),
            fg="blue"
        ).place(x=180, y=20)

        # ================= LABELS =================

        Label(self.tela, text="Código:").place(x=100, y=100)
        Label(self.tela, text="Nome Professor:").place(x=100, y=150)
        Label(self.tela, text="Disciplina:").place(x=100, y=200)
        Label(self.tela, text="Qtd Aulas Semanais:").place(x=100, y=250)
        Label(self.tela, text="Formação:").place(x=100, y=300)

        # ================= CAMPOS =================

        self.codigo = Entry(self.tela, width=20)
        self.nome = Entry(self.tela, width=40)
        self.disciplina = Entry(self.tela, width=40)
        self.aulas = Entry(self.tela, width=20)
        self.formacao = Entry(self.tela, width=40)

        self.codigo.place(x=300, y=100)
        self.nome.place(x=300, y=150)
        self.disciplina.place(x=300, y=200)
        self.aulas.place(x=300, y=250)
        self.formacao.place(x=300, y=300)

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
        disciplina = self.disciplina.get()
        aulas = self.aulas.get()
        formacao = self.formacao.get()

        # VALIDAR CAMPOS

        if (
            codigo == "" or
            nome == "" or
            disciplina == "" or
            aulas == "" or
            formacao == ""
        ):

            messagebox.showerror(
                "Erro",
                "Preencha todos os campos!"
            )

            return

        # VERIFICAR DUPLICADO

        professor_existente = self.colecao.find_one({
            "codigo": codigo
        })

        if professor_existente:

            messagebox.showwarning(
                "Cadastro",
                "Já existe um professor com esse código!"
            )

            return

        # INSERIR

        professor = {

            "codigo": codigo,
            "nome": nome,
            "disciplina": disciplina,
            "aulas_semanais": aulas,
            "formacao": formacao

        }

        self.colecao.insert_one(professor)

        messagebox.showinfo(
            "Cadastro",
            "Professor cadastrado com sucesso!"
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

        professor = self.colecao.find_one({
            "codigo": codigo
        })

        if professor:

            self.nome.delete(0, END)
            self.nome.insert(0, professor["nome"])

            self.disciplina.delete(0, END)
            self.disciplina.insert(
                0,
                professor["disciplina"]
            )

            self.aulas.delete(0, END)
            self.aulas.insert(
                0,
                professor["aulas_semanais"]
            )

            self.formacao.delete(0, END)
            self.formacao.insert(
                0,
                professor["formacao"]
            )

            messagebox.showinfo(
                "Consulta",
                "Professor encontrado!"
            )

        else:

            messagebox.showwarning(
                "Consulta",
                "Professor não encontrado!"
            )

    # ================= EDITAR =================

    def editar(self):

        codigo = self.codigo.get()
        nome = self.nome.get()
        disciplina = self.disciplina.get()
        aulas = self.aulas.get()
        formacao = self.formacao.get()

        # VALIDAR CAMPOS

        if (
            codigo == "" or
            nome == "" or
            disciplina == "" or
            aulas == "" or
            formacao == ""
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
                    "disciplina": disciplina,
                    "aulas_semanais": aulas,
                    "formacao": formacao

                }
            }
        )

        if resultado.modified_count > 0:

            messagebox.showinfo(
                "Editar",
                "Professor alterado com sucesso!"
            )

            self.limpar_campos()

        else:

            messagebox.showwarning(
                "Editar",
                "Professor não encontrado!"
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
                "Professor excluído!"
            )

            self.limpar_campos()

        else:

            messagebox.showwarning(
                "Excluir",
                "Professor não encontrado!"
            )

    # ================= LIMPAR CAMPOS =================

    def limpar_campos(self):

        self.codigo.delete(0, END)
        self.nome.delete(0, END)
        self.disciplina.delete(0, END)
        self.aulas.delete(0, END)
        self.formacao.delete(0, END)


# ================= EXECUTAR =================

if __name__ == "__main__":
    TelaProfessores()