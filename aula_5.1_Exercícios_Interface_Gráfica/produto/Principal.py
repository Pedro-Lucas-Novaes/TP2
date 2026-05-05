from Produto import Produto

class Principal:
    @staticmethod
    def main():
        #instanciar classe Aplicacao
        pro = Produto()
        pro.executar()
    
if __name__ == "__main__":
    Principal.main()