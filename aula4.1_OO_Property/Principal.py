from Funcionario import Funcionario

class Principal:

    @staticmethod
    def main():
        func = Funcionario()

        func.cadastrarFun()
        print("O aumento de salario do funcionario é R$", func.calcularAumento())

if __name__ == "__main__":
    Principal.main()