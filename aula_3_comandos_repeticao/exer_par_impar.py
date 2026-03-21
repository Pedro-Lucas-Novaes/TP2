import os
os.system('cls')

numeros = []
pares = []
impares = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}° numero: "))   
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"\nNúmeros digitados: {numeros}")
print(f"\nNúmeros pares digitados: {pares}")
print(f"\nNúmeros impares digitados: {impares}")