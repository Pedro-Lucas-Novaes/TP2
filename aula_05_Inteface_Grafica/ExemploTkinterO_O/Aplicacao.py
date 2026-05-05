from tkinter import *

class Aplicacao:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

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
        self.textnome = Entry(self.tela , width = 20 , borderwidth = 3)
        self.textnome.pack()

    def executar(self):
        self.tela.mainloop()