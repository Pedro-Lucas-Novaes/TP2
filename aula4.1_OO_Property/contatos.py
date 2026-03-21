class Contatos:

    def __init__(self):
        self.__nome = ""
        self.__telefone = ""
        self.__endereco = ""
        self.__cidade = ""

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, value):
        self.__telefone = value

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, value):
        self.__endereco = value

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, value):
        self.__cidade = value


    def cadastrarDados(self):
        self.nome = input("Digite o seu nome: ")
        self.telefone = input("Digite o seu telefone: ")
        self.endereco = input("Digite o seu endereço: ")
        self.cidade = input("Digite a sua cidade: ")

    def mostrarDados(self):
        print("\n--- Dados Cadastrados ---")
        print("Nome", self.nome)
        print("Telefone", self.telefone)
        print("Endereço", self.endereco)
        print("Cidade", self.cidade)
