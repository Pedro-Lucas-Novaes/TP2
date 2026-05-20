from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient


class TelaNotas:

    def __init__(self):

        # ================= CONEXÃO MONGODB =================

        self.cliente = MongoClient(
            "mongodb://localhost:27017/"
        )

        self.banco = self.cliente["escola"]

        self.colecao_notas = self.banco["notas"]
        self.colecao_alunos = self.banco["alunos"]
        self.colecao_professores = self.banco["professores"]

        # ================= TELA =================

        self.tela = Tk()
        self.tela.title("Controle de Notas")
        self.tela.geometry("850x650")
        self.tela.resizable(False, False)

        # ================= TÍTULO =================

        Label(
            self.tela,
            text="Controle de Notas",
            font=("Arial", 22, "bold"),
            fg="blue"
        ).place(x=280, y=20)

        # ================= LABELS =================

        Label(self.tela, text="ID Aluno:").place(x=100, y=100)
        Label(self.tela, text="Nome Aluno:").place(x=450, y=100)

        Label(self.tela, text="ID Professor:").place(x=100, y=150)
        Label(self.tela, text="Nome Professor:").place(x=450, y=150)

        Label(self.tela, text="Código Nota:").place(x=100, y=220)

        Label(self.tela, text="Nota 1:").place(x=100, y=280)
        Label(self.tela, text="Nota 2:").place(x=100, y=330)
        Label(self.tela, text="Nota 3:").place(x=100, y=380)
        Label(self.tela, text="Nota 4:").place(x=100, y=430)

        # ================= CAMPOS =================

        self.id_aluno = Entry(self.tela, width=20)
        self.id_professor = Entry(self.tela, width=20)

        self.codigo = Entry(self.tela, width=20)

        self.nota1 = Entry(self.tela, width=20)
        self.nota2 = Entry(self.tela, width=20)
        self.nota3 = Entry(self.tela, width=20)
        self.nota4 = Entry(self.tela, width=20)

        self.id_aluno.place(x=220, y=100)
        self.id_professor.place(x=220, y=150)

        self.codigo.place(x=220, y=220)

        self.nota1.place(x=220, y=280)
        self.nota2.place(x=220, y=330)
        self.nota3.place(x=220, y=380)
        self.nota4.place(x=220, y=430)

        # ================= LABELS NOMES =================

        self.lbl_nome_aluno = Label(
            self.tela,
            text="",
            width=30,
            bg="white",
            relief="solid",
            anchor="w"
        )

        self.lbl_nome_aluno.place(x=560, y=100)

        self.lbl_nome_professor = Label(
            self.tela,
            text="",
            width=30,
            bg="white",
            relief="solid",
            anchor="w"
        )

        self.lbl_nome_professor.place(x=560, y=150)

        # ================= EVENTOS =================

        self.id_aluno.bind(
            "<KeyRelease>",
            self.buscar_aluno
        )

        self.id_professor.bind(
            "<KeyRelease>",
            self.buscar_professor
        )

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
        ).place(x=120, y=520)

        Button(
            self.tela,
            text="Consultar",
            image=self.img_consultar,
            compound=TOP,
            command=self.consultar
        ).place(x=280, y=520)

        Button(
            self.tela,
            text="Editar",
            image=self.img_alterar,
            compound=TOP,
            command=self.editar
        ).place(x=440, y=520)

        Button(
            self.tela,
            text="Excluir",
            image=self.img_excluir,
            compound=TOP,
            command=self.excluir
        ).place(x=600, y=520)

        # ================= MÉDIA =================

        self.lbl_media = Label(
            self.tela,
            text="Média: 0.0",
            font=("Arial", 16, "bold"),
            fg="green"
        )

        self.lbl_media.place(x=330, y=610)

        self.tela.mainloop()

    # ================= BUSCAR ALUNO =================

    def buscar_aluno(self, event):

        codigo = self.id_aluno.get()

        aluno = self.colecao_alunos.find_one({
            "codigo": codigo
        })

        if aluno:

            self.lbl_nome_aluno.config(
                text=aluno["nome"]
            )

        else:

            self.lbl_nome_aluno.config(
                text=""
            )

    # ================= BUSCAR PROFESSOR =================

    def buscar_professor(self, event):

        codigo = self.id_professor.get()

        professor = self.colecao_professores.find_one({
            "codigo": codigo
        })

        if professor:

            self.lbl_nome_professor.config(
                text=professor["nome"]
            )

        else:

            self.lbl_nome_professor.config(
                text=""
            )

    # ================= CADASTRAR =================

    def cadastrar(self):

        codigo = self.codigo.get()

        id_aluno = self.id_aluno.get()
        nome_aluno = self.lbl_nome_aluno.cget("text")

        id_professor = self.id_professor.get()
        nome_professor = self.lbl_nome_professor.cget("text")

        nota1 = self.nota1.get()
        nota2 = self.nota2.get()
        nota3 = self.nota3.get()
        nota4 = self.nota4.get()

        # VALIDAR CAMPOS

        if (
            codigo == "" or
            id_aluno == "" or
            id_professor == "" or
            nota1 == "" or
            nota2 == "" or
            nota3 == "" or
            nota4 == ""
        ):

            messagebox.showerror(
                "Erro",
                "Preencha todos os campos!"
            )

            return

        # VALIDAR ALUNO

        if nome_aluno == "":

            messagebox.showerror(
                "Erro",
                "Aluno não encontrado!"
            )

            return

        # VALIDAR PROFESSOR

        if nome_professor == "":

            messagebox.showerror(
                "Erro",
                "Professor não encontrado!"
            )

            return

        # VERIFICAR DUPLICADO

        nota_existente = self.colecao_notas.find_one({
            "codigo": codigo
        })

        if nota_existente:

            messagebox.showwarning(
                "Cadastro",
                "Já existe uma nota com esse código!"
            )

            return

        # CALCULAR MÉDIA

        media = (
            float(nota1) +
            float(nota2) +
            float(nota3) +
            float(nota4)
        ) / 4

        # INSERIR

        nota = {

            "codigo": codigo,

            "id_aluno": id_aluno,
            "nome_aluno": nome_aluno,

            "id_professor": id_professor,
            "nome_professor": nome_professor,

            "nota1": nota1,
            "nota2": nota2,
            "nota3": nota3,
            "nota4": nota4,

            "media": media

        }

        self.colecao_notas.insert_one(nota)

        self.lbl_media.config(
            text=f"Média: {media:.2f}"
        )

        messagebox.showinfo(
            "Cadastro",
            "Notas cadastradas!"
        )

        self.limpar_campos()

    # ================= CONSULTAR =================

    def consultar(self):

        codigo = self.codigo.get()

        nota = self.colecao_notas.find_one({
            "codigo": codigo
        })

        if nota:

            self.id_aluno.delete(0, END)
            self.id_aluno.insert(
                0,
                nota["id_aluno"]
            )

            self.lbl_nome_aluno.config(
                text=nota["nome_aluno"]
            )

            self.id_professor.delete(0, END)
            self.id_professor.insert(
                0,
                nota["id_professor"]
            )

            self.lbl_nome_professor.config(
                text=nota["nome_professor"]
            )

            self.nota1.delete(0, END)
            self.nota1.insert(
                0,
                nota["nota1"]
            )

            self.nota2.delete(0, END)
            self.nota2.insert(
                0,
                nota["nota2"]
            )

            self.nota3.delete(0, END)
            self.nota3.insert(
                0,
                nota["nota3"]
            )

            self.nota4.delete(0, END)
            self.nota4.insert(
                0,
                nota["nota4"]
            )

            self.lbl_media.config(
                text=f"Média: {nota['media']:.2f}"
            )

            messagebox.showinfo(
                "Consulta",
                "Registro encontrado!"
            )

        else:

            messagebox.showwarning(
                "Consulta",
                "Registro não encontrado!"
            )

    # ================= EDITAR =================

    def editar(self):

        codigo = self.codigo.get()

        nota1 = self.nota1.get()
        nota2 = self.nota2.get()
        nota3 = self.nota3.get()
        nota4 = self.nota4.get()

        media = (
            float(nota1) +
            float(nota2) +
            float(nota3) +
            float(nota4)
        ) / 4

        resultado = self.colecao_notas.update_one(

            {"codigo": codigo},

            {
                "$set": {

                    "nota1": nota1,
                    "nota2": nota2,
                    "nota3": nota3,
                    "nota4": nota4,
                    "media": media

                }
            }
        )

        if resultado.modified_count > 0:

            self.lbl_media.config(
                text=f"Média: {media:.2f}"
            )

            messagebox.showinfo(
                "Editar",
                "Notas alteradas!"
            )

        else:

            messagebox.showwarning(
                "Editar",
                "Registro não encontrado!"
            )

    # ================= EXCLUIR =================

    def excluir(self):

        codigo = self.codigo.get()

        resultado = self.colecao_notas.delete_one({
            "codigo": codigo
        })

        if resultado.deleted_count > 0:

            messagebox.showinfo(
                "Excluir",
                "Registro excluído!"
            )

            self.limpar_campos()

        else:

            messagebox.showwarning(
                "Excluir",
                "Registro não encontrado!"
            )

    # ================= LIMPAR =================

    def limpar_campos(self):

        self.codigo.delete(0, END)

        self.id_aluno.delete(0, END)
        self.id_professor.delete(0, END)

        self.nota1.delete(0, END)
        self.nota2.delete(0, END)
        self.nota3.delete(0, END)
        self.nota4.delete(0, END)

        self.lbl_nome_aluno.config(text="")
        self.lbl_nome_professor.config(text="")

        self.lbl_media.config(
            text="Média: 0.0"
        )


# ================= EXECUTAR =================

if __name__ == "__main__":
    TelaNotas()