class Quadrado:

    def __init__(self):
        self.__numero = 0.0
        self.__resultado = 0.0

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, value):
        self.__numero = value

    @property
    def resultado(self):
        return self.__resultado

    @resultado.setter
    def resultado(self, value):
        self.__resultado = value

    def inserirNumero(self):
        self.numero = float(input("Digite o número: "))

    def calcularQuadrado(self):
        self.resultado = pow(self.numero,2)

    def mostrarQuadrado(self):
        print("O quadrado do número é:", self.resultado)

