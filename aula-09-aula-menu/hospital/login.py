from tkinter import *
from tkinter import messagebox
import subprocess
import sys


class TelaLogin:

    def __init__(self):
        self.tela = Tk()
        self.tela.title("Acesso ao Sistema")

        self.largura = 400
        self.altura = 200

        self.centralizar_tela()
        self.tela.resizable(False, False)

        self.criar_componentes()

        self.tela.mainloop()

    
    # CONFIGURAÇÃO DA TELA
    
    def centralizar_tela(self):
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()
        posx = largura_screen/2 - self.largura/2
        posy = altura_screen/2 - self.altura/2
        print(largura_screen, altura_screen)
        self.tela.geometry("%dx%d+%d+%d" % (self.largura,self.altura, posx,posy))
        self.tela.resizable(False,False)
        self.tela.configure(bg="#6099D6")


 
    # COMPONENTES
   
    def criar_componentes(self):

        Label(self.tela, text="Usuário").place(x=50, y=60)
        Label(self.tela, text="Senha").place(x=50, y=100)

        self.txt_usuario = Entry(self.tela, width=20)
        self.txt_usuario.place(x=100, y=60)

        self.txt_senha = Entry(self.tela, width=20, show="*")
        self.txt_senha.place(x=100, y=100)

        self.carregar_icones()
        self.criar_botoes()

    def carregar_icones(self):
        self.foto_acesso = PhotoImage(file=r"icones\acesso.png")
        self.foto_sair = PhotoImage(file=r"icones\sair.png")

    def criar_botoes(self):

        Button(self.tela,text="Acessar", image=self.foto_acesso,compound=TOP,command=self.validar_acesso).place(x=250, y=50)

        Button(self.tela,text="Sair",image=self.foto_sair,compound=TOP,command=self.sair).place(x=320, y=50)

    
    # FUNÇÕES
   
    def validar_acesso(self):
        usuario = self.txt_usuario.get()
        senha = self.txt_senha.get()

        if usuario == "admin" and senha == "123":
            self.abrir_menu()
        else:
            messagebox.showerror(
                "Erro de Login",
                "Usuário ou senha incorretos"
            )

    def abrir_menu(self):
        self.tela.destroy()
        subprocess.run([sys.executable, "Menu.py"])

    def sair(self):
        resposta = messagebox.askquestion(
            "Sair do Sistema?",
            "Você tem certeza que deseja sair?"
        )

        if resposta == "yes":
            self.tela.destroy()

