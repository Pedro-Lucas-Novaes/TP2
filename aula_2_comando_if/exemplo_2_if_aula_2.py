#comando para limpar a tela na execução
import os
os.system('cls')

#Estrutura if Operadores Relacionais and = e or = ou

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if num1 == num2 or num2 == num3 or num3 == num1: 
    exit()#termina a execução
if num1 > num2 and num1 > num3:
    print("O primeiro número é maior")
if num2 > num1 and num2 > num3:
    print("O segundo número é maior")
if num3 > num1 and num3 > num2:
    print("O terceiro número é maior")