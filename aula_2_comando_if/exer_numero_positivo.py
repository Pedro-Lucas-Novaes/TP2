import os
os.system('cls')

num = int(input("Digite o numero: "))

os.system('cls')

if num % 2 == 0:
    quadrado = num * num
    print(f"O numero {num} é par\nO resultado dele ao quadrado é: {quadrado} que é PAR também!")
else:
    cubo = num * num * num
    print(f"O numero {num} é impar\nO resultado dele ao cubo é: {cubo} que é IMPAR também!")