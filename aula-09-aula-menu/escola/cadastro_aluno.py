from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk


class GestaoAnimais:
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Gestão de Animais")

        self.largura = 700
        self.altura = 400
        self.pasta_inicial = ""

        self.var_sexo = StringVar()
        self.var_sexo.set("m")

        self.centralizar_tela()
        self.criar_componentes()


        self.tela.mainloop()

   
    # CONFIGURAÇÕES DA TELA

    def centralizar_tela(self):
      
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()
        posx = largura_screen/2 - self.largura/2
        posy = altura_screen/2 - self.altura/2
        print(largura_screen, altura_screen)
        self.tela.geometry("%dx%d+%d+%d" % (self.largura,self.altura, posx,posy))
        self.tela.resizable(False,False)


  
    # COMPONENTES

    def criar_componentes(self):
        self.criar_labels()
        self.criar_campos()
        self.criar_botoes()
   

    def criar_labels(self):
        Label(self.tela, text="Código:").place(x=130, y=50)
        Label(self.tela, text="Nome:").place(x=130, y=80)
        Label(self.tela, text="Idade").place(x=510, y=80)
        Label(self.tela, text="Sexo").place(x=130, y=110)
        Label(self.tela, text="Raça").place(x=260, y=110)
        Label(self.tela, text="Peso").place(x=380, y=110)
        Label(self.tela, text="Espécie").place(x=510, y=110)
        Label(self.tela, text="Data Nascimento").place(x=130, y=140)
        Label(self.tela, text="Data Cadastro").place(x=380, y=140)
        Label(self.tela, text="Data Atualização").place(x=130, y=170)
        Label(self.tela, text="Descrição").place(x=130, y=200)

    def criar_campos(self):
        self.txt_codigo = Entry(self.tela, width=10)
        self.txt_nome = Entry(self.tela, width=50)
        self.txt_idade = Entry(self.tela, width=20)
        self.txt_raca = Entry(self.tela, width=10)
        self.txt_peso = Entry(self.tela, width=10)

        self.cmb_especie = ttk.Combobox(
            self.tela,
            values=["Vira-Lata", "Beagle", "Pastor ALemão"],
            width=10
        )

        self.txt_data_nascimento = Entry(self.tela, width=20)
        self.txt_data_cadastro = Entry(self.tela, width=20)
        self.txt_data_atualizacao = Entry(self.tela, width=20)
        self.txt_descricao = Text(self.tela, width=50, height=5)

        self.rdb_m = Radiobutton(
            self.tela,
            text="M",
            variable=self.var_sexo,
            value="m"
        )

        self.rdb_f = Radiobutton(
            self.tela,
            text="F",
            variable=self.var_sexo,
            value="f"
        )

        # POSIÇÕES
        self.txt_codigo.place(x=180, y=50)
        self.txt_nome.place(x=180, y=80)
        self.txt_idade.place(x=560, y=80)
        self.rdb_m.place(x=180, y=110)
        self.rdb_f.place(x=220, y=110)
        self.txt_raca.place(x=300, y=110)
        self.txt_peso.place(x=420, y=110)
        self.cmb_especie.place(x=560, y=110)

        self.txt_data_nascimento.place(x=240, y=140)
        self.txt_data_cadastro.place(x=470, y=140)
        self.txt_data_atualizacao.place(x=240, y=170)
        self.txt_descricao.place(x=190, y=205)

      

    def criar_botoes(self):

        self.foto_salvar = PhotoImage(file=r"icones\salvar.png")
        self.foto_excluir = PhotoImage(file=r"icones\excluir.png")
        self.foto_alterar = PhotoImage(file=r"icones\alterar.png")
        self.foto_consultar = PhotoImage(file=r"icones\consultar.png")
        self.foto_sair = PhotoImage(file=r"icones\sair.png")

        Button(
            self.tela,
            text="Escolher imagem",
            command=self.escolher_imagem
        ).place(x=10, y=140)

        self.btn_salvar = Button(
            self.tela,
            text="Salvar",
            image=self.foto_salvar,
            compound=TOP,
            command=self.salvar
        )

        self.btn_excluir = Button(
            self.tela,
            text="Excluir",
            image=self.foto_excluir,
            compound=TOP,
            command=self.excluir
        )

        self.btn_alterar = Button(
            self.tela,
            text="Alterar",
            image=self.foto_alterar,
            compound=TOP,
            command=self.alterar
        )

        self.btn_consultar = Button(
            self.tela,
            text="Consultar",
            image=self.foto_consultar,
            compound=TOP,
            command=self.consultar
        )

        self.btn_sair = Button(
            self.tela,
            text="Sair",
            image=self.foto_sair,
            compound=RIGHT,
            command=self.tela.destroy
        )

        self.btn_salvar.place(x=130, y=310)
        self.btn_excluir.place(x=200, y=310)
        self.btn_alterar.place(x=270, y=310)
        self.btn_consultar.place(x=340, y=310)
        self.btn_sair.place(x=620, y=340)
    
    # FUNÇÕES

    def escolher_imagem(self):
        caminho = filedialog.askopenfilename(
            initialdir=self.pasta_inicial,
            title="Escolha uma imagem",
            filetypes=(
                ("Arquivos de imagem", "*.jpg;*.jpeg;*.png"),
                ("Todos os arquivos", "*.*")
            )
        )

        if caminho:
            imagem = Image.open(caminho)
            largura, altura = imagem.size

            if largura > 150:
                proporcao = largura / 150
                nova_altura = int(altura / proporcao)
                imagem = imagem.resize((110, nova_altura))

            imagem_tk = ImageTk.PhotoImage(imagem)

            self.lbl_imagem = Label(self.tela, image=imagem_tk)
            self.lbl_imagem.image = imagem_tk
            self.lbl_imagem.place(x=10, y=50)

  

  
    # AÇÕES DOS BOTÕES
  
    def salvar(self):
        messagebox.showinfo("Salvar", "Registro salvo com sucesso!")

    def excluir(self):
        messagebox.showinfo("Excluir", "Registro excluído!")

    def alterar(self):
        messagebox.showinfo("Alterar", "Registro alterado!")

    def consultar(self):
        messagebox.showinfo("Consultar", "Consulta realizada!")


# EXECUTAR
if __name__ == "__main__":
    GestaoAnimais()