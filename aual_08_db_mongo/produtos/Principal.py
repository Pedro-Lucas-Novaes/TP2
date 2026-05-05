from Produto import Produtos

class Principal:

    @staticmethod
    def main():
        cli = Produtos()
        cli.executar()

if __name__ == "__main__":
    Principal.main()