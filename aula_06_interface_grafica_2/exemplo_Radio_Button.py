from tkinter import *
tela = Tk()

tela.title("Radio Buttons")

#cor da tela
tela.configure(background='#1e3743')
#configurar tamanho da tela 
tela.geometry("700x600")

var = StringVar()
var.set("m")

rdb_buttonm = Radiobutton(tela,text="M",variable=var, value ="m").place(x=20, y=40)
rdb_buttonf = Radiobutton(tela,text="F",variable=var, value ="f").place(x=20, y=60)

tela.mainloop()