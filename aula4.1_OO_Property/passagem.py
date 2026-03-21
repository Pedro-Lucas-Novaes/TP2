class Passagem:

    def __init__(self):
        self.__nomePassageiro = ""
        self.__telefone = ""
        self.__rg = ""
        self.__localViagem = ""
        self.__data = ""
        self.__horario = ""
        self.__numPoltrona = ""

    @property
    def nomePassageiro(self):
        return self.__nomePassageiro

    @nomePassageiro.setter
    def nomePassageiro(self, value):
        self.__nomePassageiro = value

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, value):
        self.__telefone = value

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, value):
        self.__rg = value

    @property
    def localViagem(self):
        return self.__localViagem

    @localViagem.setter
    def localViagem(self, value):
        self.__localViagem = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, value):
        self.__horario = value

    @property
    def numPoltrona(self):
        return self.__numPoltrona

    @numPoltrona.setter
    def numPoltrona(self, value):
        self.__numPoltrona = value

    def cadastrarDadosPassageiros(self):
        self.nomePassageiro = input("Digite o seu nome: ")
        self.telefone = input("Digite o seu numero de telefone: ")
        self.rg = input("Digite o seu RG: ")

    def cadastrarDadosPassagem(self):
        self.localViagem = input("Digite o local da viagem: ")
        self.data = input("Digite a data da viagem: ")
        self.horario = input("Digite o horario da viagem: ")
        self.numPoltrona = input("Digite o numero da poltrona: ")

    def mostrarDadosPassageiro(self):
        print("\n---- Dados Passageiro ---")
        print("Nome", self.nomePassageiro)
        print("Telefone", self.telefone)
        print("RG", self.rg)

    def mostrarDadosPassagem(self):
        print("\n--- Dados Passagem ---")
        print("Local da Viagem", self.localViagem)
        print("Data", self.data)
        print("Horário", self.horario)
        print("Numero da Poltrona", self.numPoltrona)