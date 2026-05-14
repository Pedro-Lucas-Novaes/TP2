from Media import Media

class Principal:
    @staticmethod
    def main():
        #instanciar classe Aplicacao
        som = Media()
        som.executar()
    
if __name__ == "__main__":
    Principal.main()