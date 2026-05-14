from Soma import Soma

class Principal:
    @staticmethod
    def main():
        #instanciar classe Aplicacao
        som = Soma()
        som.executar()
    
if __name__ == "__main__":
    Principal.main()