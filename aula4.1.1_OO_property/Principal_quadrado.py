from quadrado import Quadrado

import os
os.system('cls')

class Principal_quadrado:

    
    @staticmethod
    def main():

        qua = Quadrado()

        qua.inserirNumero()

        os.system('cls')

        qua.calcularQuadrado()

        qua.mostrarQuadrado()

if __name__ == "__main__":
    Principal_quadrado.main()