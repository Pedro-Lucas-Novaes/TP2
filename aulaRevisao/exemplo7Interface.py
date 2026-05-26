from tkinter import *

# Definições da tela
tela = Tk()
tela.title("Titulo")
tela.configure(background="#6407c7")
tela.geometry("700x600")

# Definições componentes

lbl_base = Label(tela , text="Digite a base: ", font="Arial 15 bold", fg="#0faf97", bg="#6407c7")
lbl_base.place(x=200, y=15)

txt_base = Entry(tela, width= 20, fg="#1e7aca")
txt_base.place(x= 335, y=20)

lbl_altura = Label(tela , text="Digite a altura: ", font="Arial 15 bold", fg="#0faf97", bg="#6407c7")
lbl_altura.place(x=190, y=55)

txt_altura = Entry(tela, width= 20, fg="#1e7aca")
txt_altura.place(x= 335, y=60)

lbl_resul = Label(tela , text="Resultado: ", font="Arial 15 bold", fg="#0faf97", bg="#6407c7")
lbl_resul.place(x=220, y=115)

txt_resul = Entry(tela, width= 20, fg="#1e7aca")
txt_resul.place(x= 330, y=120)


def calcularArea():
    area =( float(txt_base.get()) * float(txt_altura.get())) /2
    txt_resul.insert(0,f"A area é {area:.2f}")

btn_botao = Button(tela, text="Calcular Area", bg="#b11d1d", command= calcularArea, width= 30)
btn_botao.place(x=200 , y=200)



# executar tela
tela.mainloop()