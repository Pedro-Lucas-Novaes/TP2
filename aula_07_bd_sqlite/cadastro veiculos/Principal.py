from Carros import CadrastroVeiculos

class Principal:
    @staticmethod
    def main():
        #instanciar classe 
        p = CadrastroVeiculos()
        p.executar()

if __name__ == "__main__":
    Principal.main()