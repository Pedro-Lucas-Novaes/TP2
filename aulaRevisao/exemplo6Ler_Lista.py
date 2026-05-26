# Armazena os valores de uma lista que foi definido pelo usuario

pessoas = []

for lista in range(1,6):
    p = input(f"Digite o nome da {lista} pessoa ")
    # armazenando dados no vetor
    pessoas.append(p)

#mostrar os dados

for i in pessoas:
    print(i)