salario = float(input("Digite o valor do salario atual: "))
porc = float(input("Digite a porcetangem de aumento do salario: "))
ns = (salario * porc)/100 + salario
print(f"O valor do novo salario é: R${ns:.2f}")