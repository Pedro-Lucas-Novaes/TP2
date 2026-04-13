from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import sys


class ControlePessoas:

    def __init__(self):
        self.tela = Tk()
      
        self.configurar_tela()
        self.criar_componentes()


    # ---------------------------
    def configurar_tela(self):
        
        self.tela.title("Controle de Pessoas")
        self.tela.config(background="#d0d0d0")

        self.largura = 800
        self.altura = 600

        self.var = StringVar()
        self.var.set("m")

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = largura_screen / 2 - self.largura / 2
        posy = altura_screen / 2 - self.altura / 2

        self.tela.geometry("%dx%d+%d+%d" % (self.largura, self.altura, posx, posy))

    # ---------------------------
    def salvar(self):
        dados = (
            f"Código: {self.txt_codigo.get()}  Nome: {self.txt_nome.get()}\n"
            f"Idade: {self.txt_idade.get()}  Sexo: {self.var.get()}\n"
            f"Altura: {self.txt_altura.get()}  Peso: {self.txt_peso.get()}\n"
            f"Cidade: {self.cmb_cidade.get()}  Data Nasc: {self.txt_data_nascimento.get()}"
        )

        Label(self.tela, text=dados).place(x=20, y=320)

    # ---------------------------
    def sair(self):
        self.tela.destroy()
        sys.exit()

    # ---------------------------
    def escolher_imagem(self):
        caminho = filedialog.askopenfilename(
            title="Escolha uma imagem",
            filetypes=(("Imagens", "*.jpg;*.jpeg;*.png"), ("Todos", "*.*"))
        )

        if caminho:
            imagem = Image.open(caminho)
            largura, altura = imagem.size

            if largura > 150:
                proporcao = largura / 150
                nova_altura = int(altura / proporcao)
                imagem = imagem.resize((110, nova_altura))

            imagem_tk = ImageTk.PhotoImage(imagem)

            self.lbl_imagem = Label(self.tela, image=imagem_tk ,  width=95, height=140, bg="gray")
            self.lbl_imagem.image = imagem_tk
            self.lbl_imagem.place(x=10, y=50)

    # ---------------------------
    def criar_componentes(self):

        # Labels
        Label(self.tela, text="Código:").place(x=130, y=50)
        Label(self.tela, text="Nome:").place(x=130, y=80)
        Label(self.tela, text="Idade").place(x=510, y=80)
        Label(self.tela, text="Sexo").place(x=130, y=110)
        Label(self.tela, text="Altura").place(x=260, y=110)
        Label(self.tela, text="Peso").place(x=380, y=110)
        Label(self.tela, text="Cidade").place(x=510, y=110)
        Label(self.tela, text="Data Nascimento").place(x=130, y=140)
        Label(self.tela, text="Data Atualização").place(x=130, y=170)
        Label(self.tela, text="Data Cadastro").place(x=380, y=140)
        Label(self.tela, text="Descrição").place(x=130, y=200)

        # Caixas de Texto
        self.txt_codigo = Entry(self.tela, width=10)
        self.txt_codigo.place(x=180, y=50)
        
        self.txt_nome = Entry(self.tela, width=50)
        self.txt_nome.place(x=180, y=80)
        
        self.txt_idade = Entry(self.tela, width=20)
        self.txt_idade.place(x=560, y=80)
        
        self.txt_altura = Entry(self.tela, width=10)
        self.txt_altura.place(x=300, y=110)
        
        self.txt_peso = Entry(self.tela, width=10)
        self.txt_peso.place(x=420, y=110)

        self.txt_data_nascimento = Entry(self.tela, width=20)
        self.txt_data_nascimento.place(x=240, y=140)
        
        self.txt_data_atualizacao = Entry(self.tela, width=20)
        self.txt_data_atualizacao.place(x=240, y=170)
        
        self.txt_data_cadastro = Entry(self.tela, width=20)
        self.txt_data_cadastro.place(x=470, y=140)
        
        self.txt_descricao = Entry(self.tela, width=50)
        self.txt_descricao.place(x=190, y=205)          
                                                

        # Combobox
        self.cmb_cidade = ttk.Combobox(self.tela)
        self.cmb_cidade['values'] = ("Iguape", "Ilha Comprida", "Registro", "Juquiá", "Miracatu", "Cajati" )
        self.cmb_cidade.current(1)
        self.cmb_cidade.place(x=560, y=110)

        # Radio buttons
        Radiobutton(self.tela, text="M", variable=self.var, value="m").place(x=180, y=110)
        Radiobutton(self.tela, text="F", variable=self.var, value="f").place(x=220, y=110)

       
        # Botões
        Button(self.tela, text="Escolher imagem",command=self.escolher_imagem).place(x=10, y=200)

        self.foto_salvar = PhotoImage(file="icones/salvar.png")
        self.foto_excluir = PhotoImage(file="icones/excluir.png")
        self.foto_alterar = PhotoImage(file="icones/alterar.png")
        self.foto_consultar = PhotoImage(file="icones/consultar.png")
        self.foto_sair = PhotoImage(file="icones/sair.png")

        # Botões (sem .place na mesma linha)
        self.btn_salvar = Button(self.tela, text="Salvar",image=self.foto_salvar,compound=TOP,command=self.salvar)
        self.btn_salvar.place(x=130, y=240)

        self.btn_excluir = Button(self.tela, text="Excluir",image=self.foto_excluir,compound=TOP)
        self.btn_excluir.place(x=200, y=240)
        
        self.btn_alterar = Button(self.tela, text="Alterar",image=self.foto_alterar,compound=TOP)
        self.btn_alterar.place(x=270, y=240)

        self.btn_consultar = Button(self.tela, text="Consultar",image=self.foto_consultar,compound=TOP)        
        self.btn_consultar.place(x=340, y=240)

        self.btn_sair = Button(self.tela, text="Sair",image=self.foto_sair,compound=RIGHT,command=self.sair)  
        self.btn_sair.place(x=620, y=260)

    def executar(self):
        self.tela.mainloop()

