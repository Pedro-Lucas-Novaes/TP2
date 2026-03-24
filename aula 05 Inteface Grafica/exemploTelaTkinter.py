from tkinter import *
# Criando tela do Tkinter - Interface Grafica
tela = Tk()

#titulo
tela.title("Fatec Registro")

#cor do fundo
tela.configure(background="#fcba03")
#tamanho tela
tela.geometry("700x500")

#redimensionar tela true=habilita / false desabilita
tela.resizable(True,True)
# define o tamanho minimo para redimensionar
tela.minsize(width=400, height=600)
# define o tamanho maximo para redimensionar
tela.maxsize(width=700, height=800)

#Criando Label
lbl_nome = Label(tela,text="Digite seu nome: ", background="#fcba03", foreground="#FFF", font="Arial 10 bold italic").place(x=10,y=20)
lbl_tel = Label(tela,text="Digite o telefone: ", bg="#fcba03", fg="#FFF", font=("Arial","10","bold","italic")).place(x=10,y=60)

#Criando caixa de texto
txt_nome = Entry(tela,width=50, borderwidth= 3, bg= "white", fg="black")
txt_nome.place(x=120,y=20)

txt_tel = Entry(tela,width= 20, borderwidth= 3, bg= "white", fg= "blue")
txt_tel.place(x=120, y=60)

def mostradados():
    lbl_mostra = Label(tela, text= "Bem vindo: "+ txt_nome.get() + " Telefone: " + txt_tel.get())
    lbl_mostra.place(x=100, y=150)
#Criando Botão
btn_botao = Button(tela, text="Mostrar Dados", command=mostradados)
btn_botao.place(x=160,y=100)

# Executar Tela
tela.mainloop()