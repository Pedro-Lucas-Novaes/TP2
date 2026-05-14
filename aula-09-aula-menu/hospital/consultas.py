from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import pymongo


class GestaoConsultas:

    def __init__(self):

        self.tela = Tk()
        self.tela.title("Gestão de Consultas")
        self.tela.configure(bg="#f0f8ff")

        self.largura = 850
        self.altura = 620

        self.pasta_inicial = ""

        self.var_status = StringVar()

        self.centralizar_tela()

        self.conectar_banco()

        self.criar_componentes()

        self.tela.mainloop()

    def centralizar_tela(self):

        largura_screen = self.tela.winfo_screenwidth()

        altura_screen = self.tela.winfo_screenheight()

        posx = int(largura_screen / 2 - self.largura / 2)

        posy = int(altura_screen / 2 - self.altura / 2)

        self.tela.geometry(
            f"{self.largura}x{self.altura}+{posx}+{posy}"
        )

        self.tela.resizable(False, False)

    def conectar_banco(self):

        self.cliente = pymongo.MongoClient(
            "mongodb://localhost:27017/"
        )

        self.db = self.cliente["hospital"]

        self.collection = self.db["consultas"]


    def criar_componentes(self):

        self.criar_labels()

        self.criar_campos()

        self.criar_botoes()

    def criar_labels(self):

        Label(
            self.tela,
            text="Gestão de Consultas",
            font=("Arial", 24, "bold"),
            bg="#f0f8ff",
            fg="#1565c0"
        ).place(x=250, y=20)

        Label(
            self.tela,
            text="Código:",
            bg="#f0f8ff"
        ).place(x=140, y=80)

        Label(
            self.tela,
            text="Paciente:",
            bg="#f0f8ff"
        ).place(x=140, y=120)

        Label(
            self.tela,
            text="Médico:",
            bg="#f0f8ff"
        ).place(x=140, y=160)

        Label(
            self.tela,
            text="Especialidade:",
            bg="#f0f8ff"
        ).place(x=140, y=200)

        Label(
            self.tela,
            text="Data da Consulta:",
            bg="#f0f8ff"
        ).place(x=140, y=240)

        Label(
            self.tela,
            text="Horário:",
            bg="#f0f8ff"
        ).place(x=470, y=240)

        Label(
            self.tela,
            text="Status:",
            bg="#f0f8ff"
        ).place(x=140, y=280)

        Label(
            self.tela,
            text="Observações:",
            bg="#f0f8ff"
        ).place(x=140, y=320)

    def criar_campos(self):

        self.txt_codigo = Entry(
            self.tela,
            width=15
        )

        self.txt_paciente = Entry(
            self.tela,
            width=40
        )

        self.txt_medico = Entry(
            self.tela,
            width=40
        )

        self.txt_especialidade = Entry(
            self.tela,
            width=30
        )

        self.txt_data = Entry(
            self.tela,
            width=20
        )

        self.txt_horario = Entry(
            self.tela,
            width=15
        )

        self.combo_status = ttk.Combobox(
            self.tela,
            values=[
                "Agendada",
                "Realizada",
                "Cancelada"
            ],
            width=20,
            state="readonly"
        )

        self.txt_observacoes = Text(
            self.tela,
            width=50,
            height=5
        )

        # POSICIONAMENTO

        self.txt_codigo.place(x=250, y=80)

        self.txt_paciente.place(x=250, y=120)

        self.txt_medico.place(x=250, y=160)

        self.txt_especialidade.place(x=250, y=200)

        self.txt_data.place(x=250, y=240)

        self.txt_horario.place(x=540, y=240)

        self.combo_status.place(x=250, y=280)

        self.txt_observacoes.place(x=250, y=320)

    def criar_botoes(self):

        self.foto_salvar = PhotoImage(
            file=r"icones\salvar.png"
        )

        self.foto_excluir = PhotoImage(
            file=r"icones\excluir.png"
        )

        self.foto_alterar = PhotoImage(
            file=r"icones\alterar.png"
        )

        self.foto_consultar = PhotoImage(
            file=r"icones\consultar.png"
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
        ).place(x=120, y=500)

        Button(
            self.tela,
            text="Alterar",
            image=self.foto_alterar,
            compound=TOP,
            width=90,
            height=90,
            command=self.alterar
        ).place(x=250, y=500)

        Button(
            self.tela,
            text="Consultar",
            image=self.foto_consultar,
            compound=TOP,
            width=90,
            height=90,
            command=self.consultar
        ).place(x=380, y=500)

        Button(
            self.tela,
            text="Excluir",
            image=self.foto_excluir,
            compound=TOP,
            width=90,
            height=90,
            command=self.excluir
        ).place(x=510, y=500)

        Button(
            self.tela,
            text="Sair",
            image=self.foto_sair,
            compound=TOP,
            width=90,
            height=90,
            command=self.tela.destroy
        ).place(x=640, y=500)


    def limpar_campos(self):

        self.txt_codigo.delete(0, END)

        self.txt_paciente.delete(0, END)

        self.txt_medico.delete(0, END)

        self.txt_especialidade.delete(0, END)

        self.txt_data.delete(0, END)

        self.txt_horario.delete(0, END)

        self.combo_status.set("")

        self.txt_observacoes.delete("1.0", END)

    def validar_campos(self):

        if self.txt_codigo.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite o código!"
            )

            self.txt_codigo.focus()

            return False

        elif self.txt_paciente.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite o nome do paciente!"
            )

            self.txt_paciente.focus()

            return False

        elif self.txt_medico.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite o médico!"
            )

            self.txt_medico.focus()

            return False

        elif self.txt_especialidade.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite a especialidade!"
            )

            self.txt_especialidade.focus()

            return False

        elif self.txt_data.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite a data da consulta!"
            )

            self.txt_data.focus()

            return False

        elif self.txt_horario.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Digite o horário!"
            )

            self.txt_horario.focus()

            return False

        elif self.combo_status.get() == "":

            messagebox.showwarning(
                "Aviso",
                "Selecione o status!"
            )

            self.combo_status.focus()

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

            dados = {

                "codigo": self.txt_codigo.get(),

                "paciente": self.txt_paciente.get(),

                "medico": self.txt_medico.get(),

                "especialidade": self.txt_especialidade.get(),

                "data": self.txt_data.get(),

                "horario": self.txt_horario.get(),

                "status": self.combo_status.get(),

                "observacoes": self.txt_observacoes.get(
                    "1.0",
                    END
                )
            }

            self.collection.insert_one(dados)

            messagebox.showinfo(
                "Sucesso",
                "Consulta salva com sucesso!"
            )

            self.limpar_campos()

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

            self.txt_codigo.insert(
                0,
                resultado["codigo"]
            )

            self.txt_paciente.insert(
                0,
                resultado["paciente"]
            )

            self.txt_medico.insert(
                0,
                resultado["medico"]
            )

            self.txt_especialidade.insert(
                0,
                resultado["especialidade"]
            )

            self.txt_data.insert(
                0,
                resultado["data"]
            )

            self.txt_horario.insert(
                0,
                resultado["horario"]
            )

            self.combo_status.set(
                resultado["status"]
            )

            self.txt_observacoes.insert(
                "1.0",
                resultado["observacoes"]
            )

        else:

            messagebox.showwarning(
                "Aviso",
                "Consulta não encontrada!"
            )

    def alterar(self):

        if self.validar_campos():

            codigo = self.txt_codigo.get()

            resultado = self.collection.find_one(
                {"codigo": codigo}
            )

            if resultado:

                dados = {

                    "codigo": self.txt_codigo.get(),

                    "paciente": self.txt_paciente.get(),

                    "medico": self.txt_medico.get(),

                    "especialidade": self.txt_especialidade.get(),

                    "data": self.txt_data.get(),

                    "horario": self.txt_horario.get(),

                    "status": self.combo_status.get(),

                    "observacoes": self.txt_observacoes.get(
                        "1.0",
                        END
                    )
                }

                self.collection.update_one(

                    {"codigo": codigo},

                    {
                        "$set": dados
                    }
                )

                messagebox.showinfo(
                    "Sucesso",
                    "Consulta alterada!"
                )

                self.limpar_campos()

            else:

                messagebox.showwarning(
                    "Aviso",
                    "Consulta não encontrada!"
                )

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
                "Consulta excluída!"
            )

            self.limpar_campos()

        else:

            messagebox.showwarning(
                "Aviso",
                "Consulta não encontrada!"
            )


if __name__ == "__main__":

    GestaoConsultas()