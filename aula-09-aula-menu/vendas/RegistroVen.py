from tkinter import *
from tkinter import ttk, messagebox
import pymongo


class RegistroVendas:

    def __init__(self):

        # =====================================
        # JANELA
        # =====================================

        self.tela = Tk()

        self.tela.title("Registro de Vendas")

        self.tela.configure(bg="#f0f8ff")

        self.largura = 980
        self.altura = 720

        self.centralizar_tela()

        # =====================================
        # BANCO
        # =====================================

        self.conectar_banco()

        # =====================================
        # COMPONENTES
        # =====================================

        self.criar_componentes()

        self.tela.mainloop()

    # =====================================
    # CENTRALIZAR TELA
    # =====================================

    def centralizar_tela(self):

        largura_screen = self.tela.winfo_screenwidth()

        altura_screen = self.tela.winfo_screenheight()

        posx = int(largura_screen / 2 - self.largura / 2)

        posy = int(altura_screen / 2 - self.altura / 2)

        self.tela.geometry(
            f"{self.largura}x{self.altura}+{posx}+{posy}"
        )

        self.tela.resizable(False, False)

    # =====================================
    # CONECTAR BANCO
    # =====================================

    def conectar_banco(self):

        self.cliente = pymongo.MongoClient(
            "mongodb://localhost:27017/"
        )

        self.db = self.cliente["empresa"]

        self.collection = self.db["vendas"]

    # =====================================
    # COMPONENTES
    # =====================================

    def criar_componentes(self):

        self.criar_labels()

        self.criar_campos()

        self.criar_botoes()

    # =====================================
    # LABELS
    # =====================================

    def criar_labels(self):

        Label(
            self.tela,
            text="Registro de Vendas",
            font=("Arial", 24, "bold"),
            bg="#f0f8ff",
            fg="#1565c0"
        ).place(x=330, y=20)

        Label(
            self.tela,
            text="Código da Venda:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=120, y=90)

        Label(
            self.tela,
            text="Cliente:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=120, y=140)

        Label(
            self.tela,
            text="Produto:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=120, y=190)

        Label(
            self.tela,
            text="Quantidade:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=120, y=240)

        Label(
            self.tela,
            text="Valor Unitário:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=500, y=240)

        Label(
            self.tela,
            text="Valor Total:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=120, y=290)

        Label(
            self.tela,
            text="Forma de Pagamento:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=500, y=290)

        Label(
            self.tela,
            text="Data da Venda:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=120, y=340)

        Label(
            self.tela,
            text="Vendedor:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=500, y=340)

        Label(
            self.tela,
            text="Observações:",
            bg="#f0f8ff",
            font=("Arial", 11)
        ).place(x=120, y=390)

    # =====================================
    # CAMPOS
    # =====================================

    def criar_campos(self):

        self.txt_codigo = Entry(
            self.tela,
            width=20,
            font=("Arial", 11)
        )

        self.txt_cliente = Entry(
            self.tela,
            width=45,
            font=("Arial", 11)
        )

        self.txt_produto = Entry(
            self.tela,
            width=45,
            font=("Arial", 11)
        )

        self.txt_quantidade = Entry(
            self.tela,
            width=20,
            font=("Arial", 11)
        )

        self.txt_valor_unitario = Entry(
            self.tela,
            width=20,
            font=("Arial", 11)
        )

        self.txt_valor_total = Entry(
            self.tela,
            width=20,
            font=("Arial", 11),
            state="readonly"
        )

        self.combo_pagamento = ttk.Combobox(
            self.tela,
            values=[
                "Dinheiro",
                "Cartão Débito",
                "Cartão Crédito",
                "PIX",
                "Boleto"
            ],
            width=25,
            state="readonly"
        )

        self.txt_data = Entry(
            self.tela,
            width=20,
            font=("Arial", 11)
        )

        self.txt_vendedor = Entry(
            self.tela,
            width=30,
            font=("Arial", 11)
        )

        self.txt_observacoes = Text(
            self.tela,
            width=65,
            height=6,
            font=("Arial", 10)
        )

        # EVENTOS PARA CALCULAR TOTAL

        self.txt_quantidade.bind(
            "<KeyRelease>",
            self.calcular_total
        )

        self.txt_valor_unitario.bind(
            "<KeyRelease>",
            self.calcular_total
        )

        # POSIÇÕES

        self.txt_codigo.place(x=280, y=90)

        self.txt_cliente.place(x=280, y=140)

        self.txt_produto.place(x=280, y=190)

        self.txt_quantidade.place(x=280, y=240)

        self.txt_valor_unitario.place(x=630, y=240)

        self.txt_valor_total.place(x=280, y=290)

        self.combo_pagamento.place(x=630, y=290)

        self.txt_data.place(x=280, y=340)

        self.txt_vendedor.place(x=630, y=340)

        self.txt_observacoes.place(x=280, y=390)

    # =====================================
    # BOTÕES
    # =====================================

    def criar_botoes(self):

        self.foto_salvar = PhotoImage(
            file=r"icones\salvar.png"
        )

        self.foto_alterar = PhotoImage(
            file=r"icones\alterar.png"
        )

        self.foto_consultar = PhotoImage(
            file=r"icones\consultar.png"
        )

        self.foto_excluir = PhotoImage(
            file=r"icones\excluir.png"
        )

        self.foto_sair = PhotoImage(
            file=r"icones\sair.png"
        )

        Button(
            self.tela,
            text="Salvar",
            image=self.foto_salvar,
            compound=TOP,
            width=90,
            height=90,
            command=self.salvar
        ).place(x=140, y=600)

        Button(
            self.tela,
            text="Alterar",
            image=self.foto_alterar,
            compound=TOP,
            width=90,
            height=90,
            command=self.alterar
        ).place(x=300, y=600)

        Button(
            self.tela,
            text="Consultar",
            image=self.foto_consultar,
            compound=TOP,
            width=90,
            height=90,
            command=self.consultar
        ).place(x=460, y=600)

        Button(
            self.tela,
            text="Excluir",
            image=self.foto_excluir,
            compound=TOP,
            width=90,
            height=90,
            command=self.excluir
        ).place(x=620, y=600)

        Button(
            self.tela,
            text="Sair",
            image=self.foto_sair,
            compound=TOP,
            width=90,
            height=90,
            command=self.tela.destroy
        ).place(x=780, y=600)

    # =====================================
    # CALCULAR TOTAL
    # =====================================

    def calcular_total(self, event=None):

        quantidade = self.txt_quantidade.get()

        valor = self.txt_valor_unitario.get()

        try:

            qtd = float(quantidade)

            val = float(valor)

            total = qtd * val

            self.txt_valor_total.config(state="normal")

            self.txt_valor_total.delete(0, END)

            self.txt_valor_total.insert(
                0,
                f"{total:.2f}"
            )

            self.txt_valor_total.config(state="readonly")

        except:

            self.txt_valor_total.config(state="normal")

            self.txt_valor_total.delete(0, END)

            self.txt_valor_total.config(state="readonly")

    # =====================================
    # LIMPAR CAMPOS
    # =====================================

    def limpar_campos(self):

        self.txt_codigo.delete(0, END)

        self.txt_cliente.delete(0, END)

        self.txt_produto.delete(0, END)

        self.txt_quantidade.delete(0, END)

        self.txt_valor_unitario.delete(0, END)

        self.txt_valor_total.config(state="normal")

        self.txt_valor_total.delete(0, END)

        self.txt_valor_total.config(state="readonly")

        self.combo_pagamento.set("")

        self.txt_data.delete(0, END)

        self.txt_vendedor.delete(0, END)

        self.txt_observacoes.delete(
            "1.0",
            END
        )

    # =====================================
    # VALIDAR CAMPOS
    # =====================================

    def validar_campos(self):

        if self.txt_codigo.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite o código da venda!"
            )

            self.txt_codigo.focus()

            return False

        elif self.txt_cliente.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite o cliente!"
            )

            self.txt_cliente.focus()

            return False

        elif self.txt_produto.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite o produto!"
            )

            self.txt_produto.focus()

            return False

        elif self.txt_quantidade.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite a quantidade!"
            )

            self.txt_quantidade.focus()

            return False

        elif self.txt_valor_unitario.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite o valor unitário!"
            )

            self.txt_valor_unitario.focus()

            return False

        elif self.combo_pagamento.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Selecione a forma de pagamento!"
            )

            self.combo_pagamento.focus()

            return False

        elif self.txt_data.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite a data da venda!"
            )

            self.txt_data.focus()

            return False

        elif self.txt_vendedor.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite o vendedor!"
            )

            self.txt_vendedor.focus()

            return False

        elif self.txt_observacoes.get(
            "1.0",
            END
        ).strip() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite as observações!"
            )

            self.txt_observacoes.focus()

            return False

        return True

    # =====================================
    # DADOS
    # =====================================

    def dados(self):

        return {

            "codigo": self.txt_codigo.get(),

            "cliente": self.txt_cliente.get(),

            "produto": self.txt_produto.get(),

            "quantidade": self.txt_quantidade.get(),

            "valor_unitario": self.txt_valor_unitario.get(),

            "valor_total": self.txt_valor_total.get(),

            "forma_pagamento": self.combo_pagamento.get(),

            "data_venda": self.txt_data.get(),

            "vendedor": self.txt_vendedor.get(),

            "observacoes": self.txt_observacoes.get(
                "1.0",
                END
            )
        }

    # =====================================
    # SALVAR
    # =====================================

    def salvar(self):

        if self.validar_campos():

            existe = self.collection.find_one(
                {"codigo": self.txt_codigo.get()}
            )

            if existe:

                messagebox.showwarning(
                    "Aviso",
                    "Código já cadastrado!"
                )

                return

            self.collection.insert_one(
                self.dados()
            )

            messagebox.showinfo(
                "Sucesso",
                "Venda cadastrada!"
            )

            self.limpar_campos()

    # =====================================
    # CONSULTAR
    # =====================================

    def consultar(self):

        codigo = self.txt_codigo.get()

        if codigo == "":

            messagebox.showwarning(
                "Aviso",
                "Digite o código!"
            )

            return

        resultado = self.collection.find_one(
            {"codigo": codigo}
        )

        if resultado:

            self.limpar_campos()

            self.txt_codigo.insert(0, resultado["codigo"])

            self.txt_cliente.insert(0, resultado["cliente"])

            self.txt_produto.insert(0, resultado["produto"])

            self.txt_quantidade.insert(
                0,
                resultado["quantidade"]
            )

            self.txt_valor_unitario.insert(
                0,
                resultado["valor_unitario"]
            )

            self.txt_valor_total.config(state="normal")

            self.txt_valor_total.insert(
                0,
                resultado["valor_total"]
            )

            self.txt_valor_total.config(state="readonly")

            self.combo_pagamento.set(
                resultado["forma_pagamento"]
            )

            self.txt_data.insert(
                0,
                resultado["data_venda"]
            )

            self.txt_vendedor.insert(
                0,
                resultado["vendedor"]
            )

            self.txt_observacoes.insert(
                "1.0",
                resultado["observacoes"]
            )

        else:

            messagebox.showwarning(
                "Aviso",
                "Venda não encontrada!"
            )

    # =====================================
    # ALTERAR
    # =====================================

    def alterar(self):

        if self.validar_campos():

            codigo = self.txt_codigo.get()

            resultado = self.collection.find_one(
                {"codigo": codigo}
            )

            if resultado:

                self.collection.update_one(

                    {"codigo": codigo},

                    {
                        "$set": self.dados()
                    }
                )

                messagebox.showinfo(
                    "Sucesso",
                    "Venda alterada!"
                )

                self.limpar_campos()

            else:

                messagebox.showwarning(
                    "Aviso",
                    "Venda não encontrada!"
                )

    # =====================================
    # EXCLUIR
    # =====================================

    def excluir(self):

        codigo = self.txt_codigo.get()

        if codigo == "":

            messagebox.showwarning(
                "Aviso",
                "Digite o código!"
            )

            return

        resultado = self.collection.find_one(
            {"codigo": codigo}
        )

        if resultado:

            self.collection.delete_one(
                {"codigo": codigo}
            )

            messagebox.showinfo(
                "Sucesso",
                "Venda excluída!"
            )

            self.limpar_campos()

        else:

            messagebox.showwarning(
                "Aviso",
                "Venda não encontrada!"
            )


# =====================================
# EXECUTAR
# =====================================

if __name__ == "__main__":

    RegistroVendas()