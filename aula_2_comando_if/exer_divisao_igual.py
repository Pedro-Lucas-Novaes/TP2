import os
os.system('cls')

num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero: "))

os.system('cls')

if num1 > num2:
    maior = num1
    menor = num2
    div = maior / menor
    print(f'Os numeros não são iguais\nO maior numero é: {maior}\nO menor numero é: {menor}\nO resultado da divisão entre o maior numero e o menor é: {div}')
elif num2 > num1:
    maior = num2
    menor = num1
    div = maior / menor
    print(f'Os numeros não são iguais\nO maior numero é: {maior}\nO menor numero é: {menor}\nO resultado da divisão entre o maior numero e o menor é: {div}')
elif num1 == num2:
    div = num1 / num2
    print(f"Os numeros são iguais\nA divisão entre os numeros é: {div}")


