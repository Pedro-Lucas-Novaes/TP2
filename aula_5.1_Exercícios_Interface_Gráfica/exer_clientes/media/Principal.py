from Media import Media

class Principal:
    @staticmethod
    def main():
        #instanciar classe Aplicacao
        med = Media()
        med.executar()
    
if __name__ == "__main__":
    Principal.main()