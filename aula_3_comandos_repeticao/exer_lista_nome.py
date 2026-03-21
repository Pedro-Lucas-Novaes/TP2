import os
os.system('cls')

nomes = []

for i in range(7):
    nome = input(f"Digite o {i+1}° nome que deseja adicionar: ")
    nomes.append(nome)

print("\nNomes armazenados e suas posições: ")
    
for posicao in range(len(nomes)):
    print(f"Posição {posicao+1}: {nomes[posicao]}")    