from Turistico import CadastroTuristico

class Principal:
    @staticmethod
    def main():
        #instanciar classe 
        p = CadastroTuristico()
        p.executar()

if __name__ == "__main__":
    Principal.main()