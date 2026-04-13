from tkinter import *

class Media:
    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_componentes()

        # Atributos
        self.__n1 = 0
        self.__n2 = 0
        self.__n3 = 0
        self.__media = 0

    def configurar_tela(self):
        self.tela.title("Cálculo de Média")
        self.tela.configure(bg="#1e3745")
        self.tela.geometry("400x300")

    def criar_componentes(self):
        self.frame = Frame(self.tela, bg="#28248C", padx=20, pady=20)
        self.frame.pack(expand=True)

        Label(self.frame, text="CÁLCULO MÉDIA",
              font=("Arial", 14, "bold"),
              bg="#28248C", fg="white").grid(row=0, column=0, columnspan=2, pady=10)

        # Nota 1
        Label(self.frame, text="Nota 1:", bg="#28248C", fg="white").grid(row=1, column=0, sticky="w")
        self.txt_n1 = Entry(self.frame)
        self.txt_n1.grid(row=1, column=1)

        # Nota 2
        Label(self.frame, text="Nota 2:", bg="#28248C", fg="white").grid(row=2, column=0, sticky="w")
        self.txt_n2 = Entry(self.frame)
        self.txt_n2.grid(row=2, column=1)

        # Nota 3
        Label(self.frame, text="Nota 3:", bg="#28248C", fg="white").grid(row=3, column=0, sticky="w")
        self.txt_n3 = Entry(self.frame)
        self.txt_n3.grid(row=3, column=1)

        # Resultado (Entry)
        Label(self.frame, text="Resultado:", bg="#28248C", fg="white").grid(row=4, column=0, sticky="w")
        self.txt_resul = Entry(self.frame)
        self.txt_resul.grid(row=4, column=1)

        # Botão
        Button(self.frame, text="Calcular Média",
               command=self.calcular,
               bg="#4CAF50", fg="white").grid(row=5, column=0, columnspan=2, pady=10)

        # Label de resultado final
        self.lbl_final = Label(self.frame,
                               text="Resultado aparecerá aqui",
                               bg="yellow",
                               fg="black",
                               font=("Arial", 11, "bold"))
        self.lbl_final.grid(row=6, column=0, columnspan=2, pady=10)

    def calcular(self):
        try:
            # Pegando valores
            self.__n1 = float(self.txt_n1.get())
            self.__n2 = float(self.txt_n2.get())
            self.__n3 = float(self.txt_n3.get())

            # Calculando média
            self.__media = (self.__n1 + self.__n2 + self.__n3) / 3

            # Mostrar no Entry
            self.txt_resul.delete(0, END)
            self.txt_resul.insert(0, f"{self.__media:.2f}")

            # Verificando situação
            if self.__media >= 7:
                situacao = "Aprovado"
            elif self.__media >= 3:
                situacao = "Exame"
            else:
                situacao = "Reprovado"

            # Mostrar no Label
            self.lbl_final.config(
                text=f"Média: {self.__media:.2f}\nAluno: {situacao}"
            )

        except:
            self.lbl_final.config(text="Erro: Digite números válidos!")

    def executar(self):
        self.tela.mainloop()


