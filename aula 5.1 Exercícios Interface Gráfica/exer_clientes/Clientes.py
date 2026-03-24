from tkinter import *

class Clientes:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

        #Atributos Privados
        self.__nome = ""
        self.__email = ""
        self.__telefone = ""
        self.__endereco = ""

    


    def configurar_tela(self):
        self.tela.title("Aplicação O_O")
        self.tela.configure(background="#1e3745")

        # Define o tamanho padrao da sua tela
        largura = 800
        altura = 300

        #Pega a largura e altura da tela do windows
        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        #Define o posicionamento centralizado
        posx = largura_screen / 2 - largura / 2
        posy = altura_screen / 2 - altura / 2

        #constroi a tela de acordo com as dimensões da tela do windows
        #%D substitui cada numero   % Concatena cada variavel largura, altura....
        self.tela.geometry("%dx%d+%d+%d" % (largura,altura, posx, posy))

    def criar_componentes(self):
        #Criar Frame    padx pady = espaçamento padding
        self.frame = Frame(self.tela, bg="#28248C", padx= 20, pady= 20)
        #pack posiciona de acordo com a tela expand => ocupa espaço na tela ao redimensionar
        self.frame.pack(expand=True)

        #Titulo
        self.titulo = Label(self.frame, text="Cadastro de Clientes")
        #grid => cria grade  row = linha colum = colunas columnspan = espaço interno coluna
        #pady = espaçamento parte de cima e de baixo de 10px
        self.titulo.grid(row= 0, column= 0, columnspan= 1, pady= 10 )

        

        #sticky = "w" posicionamento do texto lado esquedo (oeste)
        Label(self.frame, text="Nome: ").grid(row=1, column= 0, sticky= "w", pady= 5)

        self.txt_nome = Entry(self.frame)
        self.txt_nome.grid(row= 1, column= 1, pady= 5)

        
        Label(self.frame, text="email: ").grid(row=3, column= 0, sticky= "w", pady= 5)

        self.txt_email = Entry(self.frame)
        self.txt_email.grid(row= 3, column= 1, pady= 5)

        Label(self.frame, text="telefone: ").grid(row=4, column= 0, sticky= "w", pady= 5)

        self.txt_telefone = Entry(self.frame)
        self.txt_telefone.grid(row= 4, column= 1, pady= 5)

        Label(self.frame, text="endereço: ").grid(row=5, column= 0, sticky= "w", pady= 5)

        self.txt_endereco = Entry(self.frame)
        self.txt_endereco.grid(row= 5, column= 1, pady= 5)

        #Resultado

        Label(self.frame, text="Resultado: ").grid(row=6, column= 0, sticky= "w", pady= 5)

        self.txt_resul = Entry(self.frame)
        self.txt_resul.grid(row= 6, column= 1, pady= 5)
        

        #Botao
        self.btn_botao = Button(self.frame, text="Cadastrar Cliente",command= self.calcular)
        self.btn_botao.grid(row = 8, column= 0, columnspan= 2, pady= 15)

    def calcular(self):
        #Recebendo os valores das caixas de texto e guardando atributos
        self.__n1 = float(self.txt_n1.get())
        self.__n2 = float(self.txt_n2.get())
        self.__soma = self.__n1 + self.__n2

        #Colocar o resultado da soma na caixa de texto txt_resul
        self.txt_resul.insert(0,self.__soma)
        
    def executar(self):
        self.tela.mainloop()