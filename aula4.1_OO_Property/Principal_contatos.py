from contatos import Contatos

import os
os.system('cls')

class Principal_contatos:
    

    @staticmethod
    def main():
    
        cont = Contatos()

        cont.cadastrarDados()

        os.system('cls')

        cont.mostrarDados()

if __name__ == "__main__":
    Principal_contatos.main()
