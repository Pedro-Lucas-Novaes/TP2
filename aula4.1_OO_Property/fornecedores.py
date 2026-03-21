class Fornecedores:
    
    def __init__(self):
        self.__nomeFornecedor = ""
        self.__nomeProduto = ""
        self.__descricaoProduto = ""

    @property
    def nomeFornecedor(self):
        return self.__nomeFornecedor

    @nomeFornecedor.setter
    def nomeFornecedor(self, value):
        self.__nomeFornecedor = value

    @property
    def nomeProduto(self):
        return self.__nomeProduto

    @nomeProduto.setter
    def nomeProduto(self, value):
        self.__nomeProduto = value

    @property
    def descricaoProduto(self):
        return self.__descricaoProduto

    @descricaoProduto.setter
    def descricaoProduto(self, value):
        self.__descricaoProduto = value


    def cadastrarFornecedor(self):
            self.nomeFornecedor = input("Digite o nome do fornecedor: ")
            self.nomeProduto = input("Digite o nome do produto: ")
            self.descricaoProduto = input("Digite a descrição do produto: ")
        
    def listarFornecedor(self):
            print("\n--- Dados do Fornecedor ---")
            print("Fornecedor", self.nomeFornecedor)
            print("Produto", self.nomeProduto)
            print("Descrição", self.descricaoProduto)

