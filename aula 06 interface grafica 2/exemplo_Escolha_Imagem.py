
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


tela = Tk()
tela.title("open file")
tela.geometry("300x300")

largura = 700
altura = 900

pasta_inicial = ""

def escolher_imagem():

    caminho_imagem = filedialog.askopenfilename(initialdir=pasta_inicial, title="Escolha a imagem...",
                                                filetypes=(("Arquivos de Imagem", "*.jpg;*.jpeg;*.png"),
                                                           ("Todos os arquivos", "*.*")))
    imagem_pil = Image.open(caminho_imagem)
    largura, altura = imagem_pil.size
    if largura > 150:
        proporcao = largura / 150
        nova_altura = int(altura/proporcao)
        imagem_pil = imagem_pil.resize((110, nova_altura))

    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    lbl_imagem = Label(tela, image=imagem_tk)
    lbl_imagem.image = imagem_tk
    lbl_imagem.place(x=10, y=50)

btn_escolher = Button(tela, text ="Escolher Imagem" , command=escolher_imagem)
btn_escolher.place(x=10,y=140)

tela.mainloop()
