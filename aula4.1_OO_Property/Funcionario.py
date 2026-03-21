class Funcionario:
    
    def __init__(self):
        self.__nome = ""
        self.__idade = 0
        self.__salarioAtual = 0.0
        self.__salarioAumento = 0.0

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _idade(self):
        return self.__idade

    @_idade.setter
    def _idade(self, value):
        self.__idade = value

    @property
    def _salarioAtual(self):
        return self.__salarioAtual

    @_salarioAtual.setter
    def _salarioAtual(self, value):
        self.__salarioAtual = value

    @property
    def _salarioAumento(self):
        return self.__salarioAumento

    @_salarioAumento.setter
    def _salarioAumento(self, value):
        self.__salarioAumento = value


    def cadastrarFun(self):
        self.__nome = input("Digite o nome: ")
        self.__idade = int(input("Digite a idade: "))
        self._salarioAtual = float(input("Digite o salario atual: "))

    def calcularAumento(self):
        self.__salarioAumento = self.__salarioAtual + (self.__salarioAtual * 10)/100
        return self.__salarioAumento 