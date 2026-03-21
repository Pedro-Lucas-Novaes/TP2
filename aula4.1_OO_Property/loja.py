class Loja:

    def __init__(self):
        self.__razaoSocial = ""
        self.__cpfCliente = ""
        self.__valorCompra = 0.0
        self.__qtdItensComp = 0
        self.__valorTotalCompra = 0.0

    @property
    def razaoSocial(self):
        return self.__razaoSocial

    @razaoSocial.setter
    def razaoSocial(self, value):
        self.__razaoSocial = value

    @property
    def cpfCliente(self):
        return self.__cpfCliente

    @cpfCliente.setter
    def cpfCliente(self, value):
        self.__cpfCliente = value

    @property
    def valorCompra(self):
        return self.__valorCompra

    @valorCompra.setter
    def valorCompra(self, value):
        self.__valorCompra = value

    @property
    def qtdItensComp(self):
        return self.__qtdItensComp

    @qtdItensComp.setter
    def qtdItensComp(self, value):
        self.__qtdItensComp = value

    @property
    def valorTotalCompra(self):
        return self.__valorTotalCompra

    @valorTotalCompra.setter
    def valorTotalCompra(self, value):
        self.__valorTotalCompra = value


    def inserirDadosLoja(self):
        self.razaoSocial = input("Digite a razão social: ")
        self.cpfCliente = input("Digite o seu CPF: ")
        self.valorCompra = float(input("Digite o valor da compra: "))
        self.qtdItensComp = float(input("Digite a quantidade de itens comprados: "))


    def calcularCompraLoja(self):
        self.valorTotalCompra = self.valorCompra * self.qtdItensComp
        return self.valorTotalCompra
    
    def mostrarDadosLoja(self):
        print("\n--- Dados da Loja ---")
        print("Razão Social:", self.razaoSocial)
        print("CPF Cliente:", self.cpfCliente)
        print("Valor da Compra:", self.valorCompra)
        print("Quantidade de itens:", self.qtdItensComp)
        print("Valor Total da Compra:", self.calcularCompraLoja())