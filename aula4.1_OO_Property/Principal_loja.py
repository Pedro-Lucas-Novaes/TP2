from loja import Loja

import os
os.system('cls')

class Principal_loja:

    @staticmethod
    def main():
        
        loja = Loja()

        loja.inserirDadosLoja()

        loja.calcularCompraLoja()

        os.system('cls')

        loja.mostrarDadosLoja()

if __name__ == "__main__":
    Principal_loja.main()