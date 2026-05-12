from exemploDbMongo import CadastroClientes

class Principal:

    @staticmethod
    def main():
        cli = CadastroClientes()
        cli.executar()

if __name__ == "__main__":
    Principal.main()