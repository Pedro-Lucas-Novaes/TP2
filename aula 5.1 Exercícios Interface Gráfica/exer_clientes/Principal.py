from Clientes import Clientes

class Principal:
    @staticmethod
    def main():
        #instanciar classe Aplicacao
        cli = Clientes()
        cli.executar()
    
if __name__ == "__main__":
    Principal.main()