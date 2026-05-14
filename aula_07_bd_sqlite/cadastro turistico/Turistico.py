from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import sys
import sqlite3


class CadastroTuristico:

    def __init__(self):
        self.tela = Tk()
      
        self.configurar_tela()
        self.criar_componentes()
        self.criar_banco()


    # ---------------------------
    def configurar_tela(self):
        
        self.tela.title("Cadastro Veiculos")
        self.tela.config(background="#d0d0d0")

        self.largura = 800
        self.placa = 600

        self.var = StringVar()
        self.var.set("sim")

        largura_screen = self.tela.winfo_screenwidth()
        placa_screen = self.tela.winfo_screenheight()

        posx = largura_screen / 2 - self.largura / 2
        posy = placa_screen / 2 - self.placa / 2

        self.tela.geometry("%dx%d+%d+%d" % (self.largura, self.placa, posx, posy))

    #CRIAR BANCO DE DADOS SQLITE
    def criar_banco(self):
        self.conn = sqlite3.connect("turistico.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS turistico (
            codigo INTEGER PRIMARY KEY,
            nome TEXT,
            cidade TEXT,
            guia TEXT,
            valor REAL,
            estado TEXT
        )
        """)
        self.conn.commit()    

    # ---------------------------
    #PARA SALVAR OS DADOS NO BD SQLITE
    def salvar(self):

        try:
            self.cursor.execute("""
            INSERT INTO turistico (
                codigo, nome, cidade, guia, valor,
                estado
            ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                self.txt_codigo.get(),
                self.txt_nome.get(),
                self.txt_cidade.get(),
                self.var.get(),
                self.txt_valor.get(),
                self.cmb_estado.get()
            ))

            self.conn.commit()

            Label(self.tela, text="Dados salvos com sucesso!", fg="green").place(x=20, y=320)

        except Exception as e:
            Label(self.tela, text=f"Erro: {e}", fg="red").place(x=20, y=320)

    #FUNÇÃO SAIR DA APLICAÇÃO
    # ---------------------------
    def sair(self):
        self.tela.destroy()
        #FECHA A CONEXÃO COM SQLITE
        self.conn.close()
        self.tela.destroy()
        sys.exit()

    # ---------------------------
    def escolher_imagem(self):
        caminho = filedialog.askopenfilename(
            title="Escolha uma imagem",
            filetypes=(("Imagens", "*.jpg;*.jpeg;*.png"), ("Todos", "*.*"))
        )

        if caminho:
            imagem = Image.open(caminho)
            largura, placa = imagem.size

            if largura > 150:
                proporcao = largura / 150
                nova_placa = int(placa / proporcao)
                imagem = imagem.resize((110, nova_placa))

            imagem_tk = ImageTk.PhotoImage(imagem)

            self.lbl_imagem = Label(self.tela, image=imagem_tk ,  width=95, height=140, bg="gray")
            self.lbl_imagem.image = imagem_tk
            self.lbl_imagem.place(x=10, y=50)

    # ---------------------------
    def criar_componentes(self):

        # Labels
        Label(self.tela, text="Código:").place(x=130, y=50)
        Label(self.tela, text="Nome Local:").place(x=105, y=80)
        Label(self.tela, text="Cidade").place(x=510, y=80)
        Label(self.tela, text="Necessita Guia:").place(x=97, y=140)
        Label(self.tela, text="Valor Entrada:").place(x=105, y=110)
        Label(self.tela, text="Estado").place(x=510, y=110)
        

        # Caixas de Texto
        self.txt_codigo = Entry(self.tela, width=10)
        self.txt_codigo.place(x=180, y=50)
        
        self.txt_nome = Entry(self.tela, width=50)
        self.txt_nome.place(x=180, y=80)
        
        self.txt_cidade = Entry(self.tela, width=20)
        self.txt_cidade.place(x=560, y=80)
        
        self.txt_valor = Entry(self.tela, width=10)
        self.txt_valor.place(x=185, y=110)
                                   

        # Combobox
        self.cmb_estado = ttk.Combobox(self.tela)
        self.cmb_estado['values'] = ("SP", "MG", "PR", "AL", "ES", "BH" )
        self.cmb_estado.current(1)
        self.cmb_estado.place(x=560, y=110)

        # Radio buttons
        Radiobutton(self.tela, text="Sim", variable=self.var, value="sim").place(x=185, y=140)
        Radiobutton(self.tela, text="Não", variable=self.var, value="nao").place(x=235, y=140)

       
        # Botões
        Button(self.tela, text="Escolher imagem",command=self.escolher_imagem).place(x=10, y=200)

        self.foto_salvar = PhotoImage(file="icones/salvar.png")
        self.foto_excluir = PhotoImage(file="icones/excluir.png")
        self.foto_alterar = PhotoImage(file="icones/alterar.png")
        self.foto_consultar = PhotoImage(file="icones/consultar.png")
        self.foto_sair = PhotoImage(file="icones/sair.png")

        # Botões (sem .place na mesma linha)
        self.btn_salvar = Button(self.tela, text="Salvar",image=self.foto_salvar,compound=TOP,command=self.salvar)
        self.btn_salvar.place(x=130, y=240)

        self.btn_excluir = Button(self.tela, text="Excluir",image=self.foto_excluir,compound=TOP,command=self.excluir)
        self.btn_excluir.place(x=200, y=240)
        
        self.btn_alterar = Button(self.tela, text="Alterar",image=self.foto_alterar,compound=TOP,command=self.atualizar)
        self.btn_alterar.place(x=270, y=240)

        self.btn_consultar = Button(self.tela, text="Consultar",image=self.foto_consultar,compound=TOP,command=self.consultar_dados)        
        self.btn_consultar.place(x=340, y=240)

        self.btn_sair = Button(self.tela, text="Sair",image=self.foto_sair,compound=RIGHT,command=self.sair)  
        self.btn_sair.place(x=620, y=260)

        #TABELA PARA MOSTRAR DADOS SQLITE
        self.tree = ttk.Treeview(self.tela, columns=("cod","nome","cidade","guia","estado"), show="headings")

        self.tree.heading("cod", text="Código")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("cidade", text="cidade")
        self.tree.heading("guia", text="Necessita guia")
        self.tree.heading("estado", text="estado")

        self.tree.place(x=20, y=350, width=950, height=200)

        self.tree.bind("<ButtonRelease-1>", self.selecionar_item)

            #SELECIONAR ITEMS DA TABELA BANCO DE DADOS
    def selecionar_item(self, event):
        item = self.tree.selection()[0]
        dados = self.tree.item(item, "values")

        self.txt_codigo.delete(0, END)
        self.txt_codigo.insert(0, dados[0])

        self.txt_nome.delete(0, END)
        self.txt_nome.insert(0, dados[1])

        self.txt_cidade.delete(0, END)
        self.txt_cidade.insert(0, dados[2])

        self.var.set(dados[3])
        self.cmb_estado.set(dados[4])

    #ATUALIZAR DADOS SQLITE
    def atualizar(self):
        self.cursor.execute("""
        UPDATE turistico SET
            nome=?,
            cidade=?,
            guia=?,
            valor=?,
            estado=?,
        WHERE codigo=?
        """, (
            self.txt_nome.get(),
            self.txt_cidade.get(),
            self.var.get(),
            self.txt_valor.get(),
            self.cmb_estado.get(),
            self.txt_codigo.get()
        ))

        self.conn.commit()
        self.consultar_dados()
    
     #CONSULTAR DADOS SQLITE
    def consultar_dados(self):
       for item in self.tree.get_children():
           self.tree.delete(item)

       self.cursor.execute("SELECT codigo, nome, cidade, guia, estado FROM turistico")
       for row in self.cursor.fetchall():
           self.tree.insert("", "end", values=row)

        #EXCLUIR DADOS BANCO DE DADOS
    def excluir(self):
        self.cursor.execute("DELETE FROM turistico WHERE codigo=?", (self.txt_codigo.get(),))
        self.conn.commit()
        self.consultar_dados()
        Label(self.tela, text="Dados excluidos com sucesso!", fg="green").place(x=20, y=320)

    
        
        

    def executar(self):
        self.tela.mainloop()

