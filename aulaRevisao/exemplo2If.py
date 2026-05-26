# Exemplo utilizando comando if

qtd = int(input("Digite a quantidade de um produto:\n"))
valor = float(input("Digite o preço do produto:\n"))

if qtd > 10:
    valorTotal = (valor * qtd) - 10
    print(f"O desconto é de R$10,00 Reais, e o valor a pagar é R${valorTotal} Reais")
elif qtd == 10:
    valorTotal = valor * qtd
    print(f"Não tem desconto, o valor total é R${valorTotal} Reais")
else:
    valorTotal = (valor * qtd) - 5
    print(f"O desconto é de R$5,00 Reais, o valor total a pagar é R${valorTotal} Reais")