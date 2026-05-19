import tkinter as tk
from tkinter import Menu, Label, Button, messagebox
import subprocess
import sys
import os

# Instale a biblioteca Pillow caso de erro
try:
    from PIL import Image, ImageTk
except:
    os.system(f'"{sys.executable}" -m pip install pillow')
    from PIL import Image, ImageTk


class TelaMenuSistema:

    def __init__(self):
        self.tela = tk.Tk()
        self.tela.title("TELA MENU SISTEMAS")

        self.largura = 1000
        self.altura = 700

        self.centralizar_tela()
        

        self.carregar_imagem_fundo()
        self.criar_menu()
        self.carregar_icones()
        self.criar_botoes()

        self.tela.mainloop()


    # CENTRALIZAR TELA   
    def centralizar_tela(self):
            
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()
        posx = largura_screen/2 - self.largura/2
        posy = altura_screen/2 - self.altura/2
        print(largura_screen, altura_screen)
        self.tela.geometry("%dx%d+%d+%d" % (self.largura,self.altura, posx,posy))
        self.tela.resizable(False,False)

 
    # IMAGEM FUNDO   
    def carregar_imagem_fundo(self):
        caminho = r"icones\escola.png"

        if os.path.exists(caminho):
            imagem = Image.open(caminho)
            imagem = imagem.resize((1000, 700))
            self.imagem_fundo = ImageTk.PhotoImage(imagem)

            self.lbl_fundo = Label(self.tela, image=self.imagem_fundo)
            self.lbl_fundo.place(x=0, y=0)
        else:
            self.tela.configure(bg="lightblue")


    # CRIAR MENU   

    def criar_menu(self):
     
        
        barra_menus = Menu(self.tela)
        opcoes_menus_arquivos = Menu(barra_menus)
        opçoes_menus_gestao = Menu(barra_menus)
        opcoes_novo = Menu(opcoes_menus_arquivos)

        barra_menus.add_cascade(label="Arquivo", menu=opcoes_menus_arquivos)
        opcoes_menus_arquivos.add_cascade(label="Novo", menu=opcoes_novo )

        opcoes_novo.add_command(label="Cadastrar")

        opcoes_menus_arquivos.add_command(label="Abrir")
        opcoes_menus_arquivos.add_command(label="Salvar")

        opcoes_menus_arquivos.add_separator()
        opcoes_menus_arquivos.add_command(label="Sair", command=self.tela.quit)


        barra_menus.add_cascade(label="Gestão", menu=opçoes_menus_gestao)
        opçoes_menus_gestao.add_command(label="Cadastro de Alunos", command=self.abrir_cadastro_aluno)
        opçoes_menus_gestao.add_command(label="Cadastro de Professores",command=self.abrir_cadastro_professor)
        opçoes_menus_gestao.add_command(label="Cadastro de Notas",command=self.abrir_cadastro_notas)
        opçoes_menus_gestao.add_command(label="Calculo da Media",command=self.abrir_calculo_media)
        self.tela.config(menu=barra_menus)


    # ÍCONES

    def carregar_icones(self):
        self.aluno = self.carregar_png(r"icones\cadastro_aluno.png", 80, 80)
        self.professor = self.carregar_png(r"icones\cadastro_professor.png", 80, 80)
        self.notas = self.carregar_png(r"icones\cadastro_notas.png", 80, 80)
        self.media = self.carregar_png(r"icones\calculo_media.png", 80, 80)
        self.logout_img = self.carregar_png(r"icones\logout.png", 80, 80)

    def carregar_png(self, caminho, largura, altura):
        if os.path.exists(caminho):
            img = Image.open(caminho)
            img = img.resize((largura, altura))
            return ImageTk.PhotoImage(img)
        return None


    # BOTÕES   
    def criar_botoes(self):

        Button(self.tela,text="Cadastro de Alunos",image=self.aluno,compound="top",command=self.abrir_cadastro_aluno, width=125).place(x=100, y=200)

        Button(self.tela,text="Cadastro de Professores",image=self.professor,compound="top",command=self.abrir_cadastro_professor,width=125).place(x=320, y=200)

        Button(self.tela,text="Cadastro de Notas",image=self.notas,compound="top",command=self.abrir_cadastro_notas,width=125).place(x=540, y=200)

        Button(self.tela,text="Calculo de Medias",image=self.media,compound="top",command=self.abrir_calculo_media, width=125).place(x=760, y=200)

        Button(self.tela,text="Logout",image=self.logout_img,compound="top",command=self.logout,width=100).place(x=880, y=560)

 
    # MÉTODOS PARA CHAMAR TELAS
    def abrir_cadastro_professor(self):
        subprocess.run([sys.executable, "cadastro_professor.py"])
    
    def abrir_cadastro_aluno(self):
        subprocess.run([sys.executable, "cadastro_aluno.py"])

    def abrir_cadastro_notas(self):
        subprocess.run([sys.executable, "cadastro_notas.py"])

    def abrir_calculo_media(self):
        subprocess.run([sys.executable, "calculo_media.py"])
    
    def logout(self):
        self.tela.destroy()
        subprocess.run([sys.executable, "login.py"])

   


# EXECUTAR

if __name__ == "__main__":
    TelaMenuSistema()