from Passageiro import Passagem

class Principal:

    @staticmethod
    def main():
        cli = Passagem()
        cli.executar()

if __name__ == "__main__":
    Principal.main()