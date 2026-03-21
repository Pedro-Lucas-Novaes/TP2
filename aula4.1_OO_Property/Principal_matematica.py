from matematica import Matematica

import os
os.system('cls')

class Principal_matematica:


    @staticmethod
    def main():

        mat = Matematica()

        mat.inserirNotas()

        mat.calcularMedia()

        os.system('cls')

        mat.mostrarNomeMedia()

if __name__ == "__main__":
    Principal_matematica.main()