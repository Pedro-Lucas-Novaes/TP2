from passagem import Passagem
import os
os.system('cls')

class Principal_passagem:

    @staticmethod
    def main():
        func = Passagem()

        func.cadastrarDadosPassageiros()
        func.cadastrarDadosPassagem()

        os.system('cls')

        func.mostrarDadosPassageiro()
        func.mostrarDadosPassagem()

if __name__ == "__main__":
    Principal_passagem.main()


