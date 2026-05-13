from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import sys
import os

try:
    import pymongo
except:
    os.system(f'"{sys.executable}" -m pip install pymongo')
    import pymongo


class CadastroTratamentos:

    def __init__(self):

        self.tela = Tk()
        self.tela.title("Cadastro de Tratamentos")
        self.tela.configure(bg="#ffffff")

        self.largura = 750
        self.altura = 450

        self.centralizar_tela()
        self.conectar_banco()
        self.criar_componentes()

        self.tela.mainloop()

    # CENTRALIZAR TELA

    def centralizar_tela(self):

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = int(largura_screen / 2 - self.largura / 2)
        posy = int(altura_screen / 2 - self.altura / 2)

        self.tela.geometry(f"{self.largura}x{self.altura}+{posx}+{posy}")

        self.tela.resizable(False, False)

    # CONEXÃO COM MONGODB

    def conectar_banco(self):

        self.cliente = pymongo.MongoClient(
            "mongodb://localhost:27017/"
        )

        self.db = self.cliente["exemplo"]

        self.collection = self.db["tratamentos"]

    # COMPONENTES

    def criar_componentes(self):

        self.criar_labels()
        self.criar_campos()
        self.criar_icones()
        self.criar_botoes()

    # LABELS

    def criar_labels(self):

        Label(
            self.tela,
            text="Cadastro de Tratamentos",
            font=("Arial", 22, "bold"),
            bg="#ffffff",
            fg="#2c3e50"
        ).place(x=180, y=20)

        Label(
            self.tela,
            text="Código:",
            bg="#ffffff"
        ).place(x=80, y=90)

        Label(
            self.tela,
            text="Nome do Tratamento:",
            bg="#ffffff"
        ).place(x=80, y=130)

        Label(
            self.tela,
            text="Categoria:",
            bg="#ffffff"
        ).place(x=80, y=170)

        Label(
            self.tela,
            text="Descrição:",
            bg="#ffffff"
        ).place(x=80, y=210)

        Label(
            self.tela,
            text="Duração (min):",
            bg="#ffffff"
        ).place(x=80, y=250)

        Label(
            self.tela,
            text="Valor:",
            bg="#ffffff"
        ).place(x=400, y=250)

        Label(
            self.tela,
            text="Profissional:",
            bg="#ffffff"
        ).place(x=80, y=290)

        Label(
            self.tela,
            text="Status:",
            bg="#ffffff"
        ).place(x=412, y=290)

    # CAMPOS

    def criar_campos(self):

        self.txt_codigo = Entry(self.tela, width=15)

        self.txt_nome = Entry(self.tela, width=45)

        self.txt_categoria = Entry(self.tela, width=30)

        self.txt_descricao = Entry(self.tela, width=50)

        self.txt_duracao = Entry(self.tela, width=15)

        self.txt_valor = Entry(self.tela, width=15)

        self.txt_profissional = Entry(self.tela, width=30)

        self.combo_status = ttk.Combobox(
            self.tela,
            values=["Ativo", "Inativo"],
            width=15
        )

        self.txt_codigo.place(x=230, y=90)

        self.txt_nome.place(x=230, y=130)

        self.txt_categoria.place(x=230, y=170)

        self.txt_descricao.place(x=230, y=210)

        self.txt_duracao.place(x=230, y=250)

        self.txt_valor.place(x=450, y=250)

        self.txt_profissional.place(x=230, y=290)

        self.combo_status.place(x=450, y=290)

    # ÍCONES

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

    # BOTÕES

    def criar_botoes(self):

        Button(
            self.tela,
            text="Salvar",
            image=self.foto_salvar,
            compound=TOP,
            command=self.salvar
        ).place(x=120, y=350)

        Button(
            self.tela,
            text="Alterar",
            image=self.foto_alterar,
            compound=TOP,
            command=self.atualizar
        ).place(x=240, y=350)

        Button(
            self.tela,
            text="Consultar",
            image=self.foto_consultar,
            compound=TOP,
            command=self.consultar
        ).place(x=360, y=350)

        Button(
            self.tela,
            text="Excluir",
            image=self.foto_excluir,
            compound=TOP,
            command=self.apagar
        ).place(x=490, y=350)

        Button(
            self.tela,
            text="Sair",
            image=self.foto_sair,
            compound=TOP,
            command=self.tela.quit
        ).place(x=610, y=350)

    # LIMPAR CAMPOS

    def limpar(self):

        self.txt_codigo.delete(0, END)

        self.txt_nome.delete(0, END)

        self.txt_categoria.delete(0, END)

        self.txt_descricao.delete(0, END)

        self.txt_duracao.delete(0, END)

        self.txt_valor.delete(0, END)

        self.txt_profissional.delete(0, END)

        self.combo_status.set("")

    # DADOS

    def dados(self):

        return {

            "codigo": self.txt_codigo.get(),

            "nome": self.txt_nome.get(),

            "categoria": self.txt_categoria.get(),

            "descricao": self.txt_descricao.get(),

            "duracao": self.txt_duracao.get(),

            "valor": self.txt_valor.get(),

            "profissional": self.txt_profissional.get(),

            "status": self.combo_status.get()
        }

    # VALIDAR CAMPOS

    def validar_campos(self):

        if self.txt_codigo.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Preencha o código!"
            )

            self.txt_codigo.focus()

            return False

        elif self.txt_nome.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Preencha o nome do tratamento!"
            )

            self.txt_nome.focus()

            return False

        elif self.txt_categoria.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Preencha a categoria!"
            )

            self.txt_categoria.focus()

            return False

        elif self.txt_descricao.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Preencha a descrição!"
            )

            self.txt_descricao.focus()

            return False

        elif self.txt_duracao.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Preencha a duração!"
            )

            self.txt_duracao.focus()

            return False

        elif self.txt_valor.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Preencha o valor!"
            )

            self.txt_valor.focus()

            return False

        elif self.txt_profissional.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Preencha o profissional!"
            )

            self.txt_profissional.focus()

            return False

        elif self.combo_status.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Selecione o status!"
            )

            self.combo_status.focus()

            return False

        return True

    # SALVAR

    def salvar(self):

        if self.validar_campos():

            self.collection.insert_one(
                self.dados()
            )

            self.limpar()

            messagebox.showinfo(
                "Sucesso",
                "Tratamento salvo com sucesso!"
            )

    # ALTERAR

    def atualizar(self):

        if self.validar_campos():

            codigo = self.txt_codigo.get()

            self.collection.update_one(
                {"codigo": codigo},
                {"$set": self.dados()}
            )

            messagebox.showinfo(
                "Sucesso",
                "Tratamento atualizado!"
            )

    # EXCLUIR

    def apagar(self):

        codigo = self.txt_codigo.get()

        self.collection.delete_one(
            {"codigo": codigo}
        )

        self.limpar()

        messagebox.showinfo(
            "Sucesso",
            "Tratamento excluído!"
        )

    # CONSULTAR

    def consultar(self):

        codigo = self.txt_codigo.get()

        resultado = self.collection.find_one(
            {"codigo": codigo}
        )

        if resultado:

            self.limpar()

            self.txt_codigo.insert(
                0,
                resultado["codigo"]
            )

            self.txt_nome.insert(
                0,
                resultado["nome"]
            )

            self.txt_categoria.insert(
                0,
                resultado["categoria"]
            )

            self.txt_descricao.insert(
                0,
                resultado["descricao"]
            )

            self.txt_duracao.insert(
                0,
                resultado["duracao"]
            )

            self.txt_valor.insert(
                0,
                resultado["valor"]
            )

            self.txt_profissional.insert(
                0,
                resultado["profissional"]
            )

            self.combo_status.set(
                resultado["status"]
            )

        else:

            messagebox.showwarning(
                "Aviso",
                "Tratamento não encontrado!"
            )


# EXECUTAR

if __name__ == "__main__":
    CadastroTratamentos()