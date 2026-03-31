from tkinter import *

class Clientes:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

        # Atributos privados
        self.__nome = ""
        self.__email = ""
        self.__telefone = ""
        self.__endereco = ""

        

    def configurar_tela(self):
        self.tela.title("Aplicação O_O")
        self.tela.configure(background="#1e3745")

        largura = 800
        altura = 350

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = largura_screen / 2 - largura / 2
        posy = altura_screen / 2 - altura / 2

        self.tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

    def criar_componentes(self):
        self.frame = Frame(self.tela, bg="#28248C", padx=20, pady=20)
        self.frame.pack(expand=True)

        # Título
        self.titulo = Label(
            self.frame,
            text="Cadastro de Clientes",
            font=("Arial", 16, "bold"),
            bg="#28248C",
            fg="white"
        )
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)

        Label(self.frame, text="Nome:", bg="#28248C", fg="white").grid(row=1, column=0, sticky="w", pady=5)
        self.txt_nome = Entry(self.frame, width=30)
        self.txt_nome.grid(row=1, column=1, pady=5)

        Label(self.frame, text="Email:", bg="#28248C", fg="white").grid(row=2, column=0, sticky="w", pady=5)
        self.txt_email = Entry(self.frame, width=30)
        self.txt_email.grid(row=2, column=1, pady=5)

        Label(self.frame, text="Telefone:", bg="#28248C", fg="white").grid(row=3, column=0, sticky="w", pady=5)
        self.txt_telefone = Entry(self.frame, width=30)
        self.txt_telefone.grid(row=3, column=1, pady=5)

        Label(self.frame, text="Endereço:", bg="#28248C", fg="white").grid(row=4, column=0, sticky="w", pady=5)
        self.txt_endereco = Entry(self.frame, width=30)
        self.txt_endereco.grid(row=4, column=1, pady=5)

        # Botão
        self.btn_botao = Button(
            self.frame,
            text="Cadastrar Cliente",
            command=self.cadastrar,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold")
        )
        self.btn_botao.grid(row=5, column=0, columnspan=2, pady=15)

        # Label de resultado
        self.lbl_resultado = Label(
            self.frame,
            text="Os dados do cliente aparecerão aqui",
            bg="#28248C",
            fg="white",
            font=("Arial", 11),
            justify="left"
        )
        self.lbl_resultado.grid(row=6, column=0, columnspan=2, pady=10)

    def cadastrar(self):
        # Recebendo os valores das caixas de texto
        self.__nome = self.txt_nome.get()
        self.__email = self.txt_email.get()
        self.__telefone = self.txt_telefone.get()
        self.__endereco = self.txt_endereco.get()

        # Mostrar no label
        texto = (
            f"Nome: {self.__nome}\n"
            f"Email: {self.__email}\n"
            f"Telefone: {self.__telefone}\n"
            f"Endereço: {self.__endereco}"
        )

        self.lbl_resultado.config(text=texto)

    def executar(self):
        self.tela.mainloop()


if __name__ == "__main__":
    app = Clientes()
    app.executar()