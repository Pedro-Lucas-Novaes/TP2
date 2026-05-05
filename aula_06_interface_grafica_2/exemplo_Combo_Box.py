from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("Combobox")
janela.geometry('250x250')

combo = Combobox(janela)
combo['values']= ("Iguape", "Ilha Comprida", "Registro", "Juquiá", "Miracatu", "Cajati")
combo.current(1)  # define o item selecionado
combo.pack()

janela.mainloop()

