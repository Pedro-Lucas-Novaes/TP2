import os
os.system('cls')

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

op = int(input("Digite a opção:\n1- Média ponderada, com pesos 2 e 3, respectivamente\n2- Quadrado da soma dos 2 números\n3- Cubo do menor número\nEscolha uma opção: "))
os.system('cls')

match op:
    case 1:
        media = (num1 * num2 + num2 * 3) / 5
        print(f"A média ponderada dos números é: {media}")
    case 2:
        potencia = (num1 + num2) ** 2
        print(f"O quadrado da soma dos 2 numeros é: {potencia}")
    case 3:
        if num1 < num2:
            cubo = num1 ** 3
        else:
            cubo = num2 ** 3
        print(f"A soma do menor número ao cubo é: {cubo}")
    case _:
        print("Opção invalida!\nEncerrando...")