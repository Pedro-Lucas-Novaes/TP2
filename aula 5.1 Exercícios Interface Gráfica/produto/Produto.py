from tkinter import *

class Produto:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

        # Atributos
        self.__nome = ""
        self.__quantidade = 0
        self.__preco = 0
        self.__total = 0

    def configurar_tela(self):
        self.tela.title("Cálculo Total Produto")
        self.tela.configure(bg="#1e3745")
        self.tela.geometry("400x350")

    def criar_componentes(self):
        self.frame = Frame(self.tela, bg="#28248C", padx=20, pady=20)
        self.frame.pack(expand=True)

        Label(self.frame, text="CÁLCULO TOTAL PRODUTO",
              font=("Arial", 14, "bold"),
              bg="#28248C", fg="white").grid(row=0, column=0, columnspan=2, pady=10)

        # Nome
        Label(self.frame, text="Nome Produto:", bg="#28248C", fg="white").grid(row=1, column=0, sticky="w")
        self.txt_nome = Entry(self.frame)
        self.txt_nome.grid(row=1, column=1)

        # Quantidade
        Label(self.frame, text="Quantidade:", bg="#28248C", fg="white").grid(row=2, column=0, sticky="w")
        self.txt_quantidade = Entry(self.frame)
        self.txt_quantidade.grid(row=2, column=1)

        # Preço
        Label(self.frame, text="Preço:", bg="#28248C", fg="white").grid(row=3, column=0, sticky="w")
        self.txt_preco = Entry(self.frame)
        self.txt_preco.grid(row=3, column=1)

        # Total (Entry)
        Label(self.frame, text="Total:", bg="#28248C", fg="white").grid(row=4, column=0, sticky="w")
        self.txt_total = Entry(self.frame)
        self.txt_total.grid(row=4, column=1)

        # Botão
        Button(self.frame, text="Calcular Total",
               command=self.calcular,
               bg="#4CAF50", fg="white").grid(row=5, column=0, columnspan=2, pady=10)

        # Label resultado
        self.lbl_resultado = Label(self.frame,
                                  text="Dados do produto aparecerão aqui",
                                  bg="yellow",
                                  fg="black",
                                  font=("Arial", 11, "bold"),
                                  justify="left")
        self.lbl_resultado.grid(row=6, column=0, columnspan=2, pady=10)

    def calcular(self):
        try:
            # Pegando valores
            self.__nome = self.txt_nome.get()
            self.__quantidade = int(self.txt_quantidade.get())
            self.__preco = float(self.txt_preco.get())

            # Calculando total
            self.__total = self.__quantidade * self.__preco

            # Mostrar no Entry
            self.txt_total.delete(0, END)
            self.txt_total.insert(0, f"{self.__total:.2f}")

            # Mostrar no Label
            texto = (
                f"Produto: {self.__nome}\n"
                f"Quantidade: {self.__quantidade}\n"
                f"Preço: R$ {self.__preco:.2f}\n"
                f"Total: R$ {self.__total:.2f}"
            )

            self.lbl_resultado.config(text=texto)

        except:
            self.lbl_resultado.config(text="Erro: digite valores válidos!")

    def executar(self):
        self.tela.mainloop()


