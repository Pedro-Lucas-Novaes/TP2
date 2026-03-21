num = float(input("Digite o número: "))
exp = float(input("Digite o expoente: "))
#Potência utilizando o operador
pot = num ** exp
#Potência utilizando a função math
pote = pow(num,exp)
print(f"O resultado da potência pot {pot}")
print(f"O resultado da potência pote {pote}")