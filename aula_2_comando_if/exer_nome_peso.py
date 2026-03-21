import os
os.system('cls')

nome1 = input("Digite o nome da primeira pessoa: ")
peso1 = float(input("Digite o peso da primeira pessoa: "))

os.system('cls')

nome2 = input("Digite o nome da segunda pessoa: ")
peso2 = float(input("Digite o peso da segunda pessoa: "))

os.system('cls')

if peso1 > peso2:
    print(f"A pessoa mais pesada é: {nome1}, pesando {peso1:.2f}Kg\nA Pessoa mais leve é: {nome2}, pesando {peso2:.2f}Kg")
elif peso2 > peso1:
    print(f"A pessoa mais pesada é: {nome2}, pesando: {peso2:.2f}Kg\nA Pessoa mais leve é: {nome1}, pesando {peso1:.2f}Kg")
elif peso1 == peso2:
    peso = peso1
    print(f"Tanto {nome1} Quanto {nome2} pesam: {peso:.2f}Kg")