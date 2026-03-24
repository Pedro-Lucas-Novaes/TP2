from Soma import Soma_Numeros

class Principal:
    @staticmethod
    def main():
        #instanciar classe Aplicacao
        som = Soma_Numeros()
        som.executar()
    
if __name__ == "__main__":
    Principal.main()