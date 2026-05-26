from tkinter import *

class Triangulo:
    def __init__(self):
        self.tela = Tk()
        self.configurarTela()
        self.criar_componentes()

    def configurarTela(self):
        self.tela.title("Calcular triangulo")
        self.tela.configure(background="#6407c7")
        self.tela.geometry("700x600")

    def criar_componentes(self):
        self.lbl_base = Label(self.tela , text="Digite a base: ", font="Arial 15 bold", fg="#0faf97", bg="#6407c7")
        self.lbl_base.place(x=200, y=15)

        self.txt_base = Entry(self.tela, width= 20, fg="#1e7aca")
        self.txt_base.place(x= 335, y=20)

        self.lbl_altura = Label(self.tela , text="Digite a altura: ", font="Arial 15 bold", fg="#0faf97", bg="#6407c7")
        self.lbl_altura.place(x=190, y=50)

        self.txt_altura = Entry(self.tela, width= 20, fg="#1e7aca")
        self.txt_altura.place(x= 335, y=55)

        self.lbl_resul = Label(self.tela , text="Resultado: ", font="Arial 15 bold", fg="#0faf97", bg="#6407c7")
        self.lbl_resul.place(x=220, y=115)

        self.txt_resul = Entry(self.tela, width= 20, fg="#1e7aca")
        self.txt_resul.place(x= 330, y=120)

        self.btn_botao = Button(self.tela, text="Calcular Area", bg="#08ab98", command= self.calcularArea, width= 30)
        self.btn_botao.place(x=200 , y=200)

        self.lbl_res = Label(self.tela , font="Arial 15", fg="#0faf97", bg="#6407c7" )
        self.lbl_res.place(x=65, y=300)

    def calcularArea(self):
        area =( float(self.txt_base.get()) * float(self.txt_altura.get())) /2
        # Mostra resultado caixa texto
        self.txt_resul.insert(0,f"A area é {area:.2f}")

        # Mostra resultado labal
        self.lbl_res.config(Text=f"A Area é {area:.2f}")

    def executar(self):
        self.tela.mainloop()


        