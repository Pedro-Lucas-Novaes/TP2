from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import sys
import sqlite3


class ControlePessoas:

    def __init__(self):
        self.tela = Tk()
      
        self.configurar_tela()
        self.criar_componentes()
        self.criar_banco()


    # ---------------------------
    def configurar_tela(self):
        
        self.tela.title("Controle de Pessoas")
        self.tela.config(background="#d0d0d0")

        self.largura = 800
        self.altura = 600

        self.var = StringVar()
        self.var.set("m")

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = largura_screen / 2 - self.largura / 2
        posy = altura_screen / 2 - self.altura / 2

        self.tela.geometry("%dx%d+%d+%d" % (self.largura, self.altura, posx, posy))

    #CRIAR BANCO DE DADOS SQLITE
    def criar_banco(self):
        self.conn = sqlite3.connect("pessoas.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            codigo INTEGER PRIMARY KEY,
            nome TEXT,
            idade INTEGER,
            sexo TEXT,
            altura REAL,
            peso REAL,
            cidade TEXT,
            data_nascimento TEXT,
            data_atualizacao TEXT,
            data_cadastro TEXT,
            descricao TEXT
        )
        """)
        self.conn.commit()    

    # ---------------------------
    #PARA SALVAR OS DADOS NO BD SQLITE
    def salvar(self):

        try:
            self.cursor.execute("""
            INSERT INTO pessoas (
                codigo, nome, idade, sexo, altura, peso,
                cidade, data_nascimento, data_atualizacao,
                data_cadastro, descricao
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                self.txt_codigo.get(),
                self.txt_nome.get(),
                self.txt_idade.get(),
                self.var.get(),
                self.txt_altura.get(),
                self.txt_peso.get(),
                self.cmb_cidade.get(),
                self.txt_data_nascimento.get(),
                self.txt_data_atualizacao.get(),
                self.txt_data_cadastro.get(),
                self.txt_descricao.get()
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
            largura, altura = imagem.size

            if largura > 150:
                proporcao = largura / 150
                nova_altura = int(altura / proporcao)
                imagem = imagem.resize((110, nova_altura))

            imagem_tk = ImageTk.PhotoImage(imagem)

            self.lbl_imagem = Label(self.tela, image=imagem_tk ,  width=95, height=140, bg="gray")
            self.lbl_imagem.image = imagem_tk
            self.lbl_imagem.place(x=10, y=50)

    # ---------------------------
    def criar_componentes(self):

        # Labels
        Label(self.tela, text="Código:").place(x=130, y=50)
        Label(self.tela, text="Nome:").place(x=130, y=80)
        Label(self.tela, text="Idade").place(x=510, y=80)
        Label(self.tela, text="Sexo").place(x=130, y=110)
        Label(self.tela, text="Altura").place(x=260, y=110)
        Label(self.tela, text="Peso").place(x=380, y=110)
        Label(self.tela, text="Cidade").place(x=510, y=110)
        Label(self.tela, text="Data Nascimento").place(x=130, y=140)
        Label(self.tela, text="Data Atualização").place(x=130, y=170)
        Label(self.tela, text="Data Cadastro").place(x=380, y=140)
        Label(self.tela, text="Descrição").place(x=130, y=200)

        # Caixas de Texto
        self.txt_codigo = Entry(self.tela, width=10)
        self.txt_codigo.place(x=180, y=50)
        
        self.txt_nome = Entry(self.tela, width=50)
        self.txt_nome.place(x=180, y=80)
        
        self.txt_idade = Entry(self.tela, width=20)
        self.txt_idade.place(x=560, y=80)
        
        self.txt_altura = Entry(self.tela, width=10)
        self.txt_altura.place(x=300, y=110)
        
        self.txt_peso = Entry(self.tela, width=10)
        self.txt_peso.place(x=420, y=110)

        self.txt_data_nascimento = Entry(self.tela, width=20)
        self.txt_data_nascimento.place(x=240, y=140)
        
        self.txt_data_atualizacao = Entry(self.tela, width=20)
        self.txt_data_atualizacao.place(x=240, y=170)
        
        self.txt_data_cadastro = Entry(self.tela, width=20)
        self.txt_data_cadastro.place(x=470, y=140)
        
        self.txt_descricao = Entry(self.tela, width=50)
        self.txt_descricao.place(x=190, y=205)          
                                                

        # Combobox
        self.cmb_cidade = ttk.Combobox(self.tela)
        self.cmb_cidade['values'] = ("Iguape", "Ilha Comprida", "Registro", "Juquiá", "Miracatu", "Cajati" )
        self.cmb_cidade.current(1)
        self.cmb_cidade.place(x=560, y=110)

        # Radio buttons
        Radiobutton(self.tela, text="M", variable=self.var, value="m").place(x=180, y=110)
        Radiobutton(self.tela, text="F", variable=self.var, value="f").place(x=220, y=110)

       
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
        self.tree = ttk.Treeview(self.tela, columns=("cod","nome","idade","sexo","cidade"), show="headings")

        self.tree.heading("cod", text="Código")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("idade", text="Idade")
        self.tree.heading("sexo", text="Sexo")
        self.tree.heading("cidade", text="Cidade")

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

        self.txt_idade.delete(0, END)
        self.txt_idade.insert(0, dados[2])

        self.var.set(dados[3])
        self.cmb_cidade.set(dados[4])

    #ATUALIZAR DADOS SQLITE
    def atualizar(self):
        self.cursor.execute("""
        UPDATE pessoas SET
            nome=?,
            idade=?,
            sexo=?,
            altura=?,
            peso=?,
            cidade=?,
            data_nascimento=?,
            descricao=?
        WHERE codigo=?
        """, (
            self.txt_nome.get(),
            self.txt_idade.get(),
            self.var.get(),
            self.txt_altura.get(),
            self.txt_peso.get(),
            self.cmb_cidade.get(),
            self.txt_data_nascimento.get(),
            self.txt_descricao.get(),
            self.txt_codigo.get()
        ))

        self.conn.commit()
        self.consultar_dados()
    
     #CONSULTAR DADOS SQLITE
    def consultar_dados(self):
       for item in self.tree.get_children():
           self.tree.delete(item)

       self.cursor.execute("SELECT codigo, nome, idade, sexo, cidade FROM pessoas")
       for row in self.cursor.fetchall():
           self.tree.insert("", "end", values=row)

        #EXCLUIR DADOS BANCO DE DADOS
    def excluir(self):
        self.cursor.execute("DELETE FROM pessoas WHERE codigo=?", (self.txt_codigo.get(),))
        self.conn.commit()
        self.consultar_dados()
        Label(self.tela, text="Dados excluidos com sucesso!", fg="green").place(x=20, y=320)

    
        
        

    def executar(self):
        self.tela.mainloop()

