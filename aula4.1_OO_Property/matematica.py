class Matematica:

    def __init__(self):
        self.__nota1 = 0.0
        self.__nota2 = 0.0
        self.__media = 0.0
        self.__nomeAluno = ""

    @property
    def nota1(self):
        return self.__nota1

    @nota1.setter
    def nota1(self, value):
        self.__nota1 = value

    @property
    def nota2(self):
        return self.__nota2

    @nota2.setter
    def nota2(self, value):
        self.__nota2 = value

    @property
    def media(self):
        return self.__media

    @media.setter
    def media(self, value):
        self.__media = value

    @property
    def nomeAluno(self):
        return self.__nomeAluno

    @nomeAluno.setter
    def nomeAluno(self, value):
        self.__nomeAluno = value


    

    def inserirNotas(self):
        self.__nomeAluno = input("Digite o nome do aluno: ")
        self.nota1 = float(input("Digite a primeira nota: "))
        self.nota2 = float(input("Digite a segunda nota: "))

    def calcularMedia(self):
        self.media = (self.nota1 + self.nota2) / 2

    def mostrarNomeMedia(self):
        print("\n--- Dados do Aluno ---")
        print("Nome do Aluno", self.nomeAluno)
        print("Media Final", self.media)