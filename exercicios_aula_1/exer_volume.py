import math

raio = float(input("Digite o valor do raio da lata de tinta: "))
altura = float(input("Digite o valor da altura da lata de tinta: "))

volume = math.pi * pow(raio,2) * altura

print(f"O volume da lata de tinta é de: {volume:.2f}")