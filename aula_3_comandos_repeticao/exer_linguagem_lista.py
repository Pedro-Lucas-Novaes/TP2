import os
os.system('cls')

linguagens = ["python", "c#", "visual basic", "c++", "delphi", "cobol", "clipper", "php", "java"]

nome = input("DIgite o nome da linguagem: ")
posicao = linguagens.index(nome)

for i in linguagens:
    if nome.lower() == i:
        print(f"\nLinguagem encontrada: {nome}")
        break
    else:
        print(f"{nome} não encontrado")

print(f"\n{nome} foi localizado na {posicao + 1}° posição")