import os
os.system('cls')

# Exemplo fo utilizando lista de valores pré-definida

frutas = ['banana', 'abacaxi', 'goiaba', 'abacate']
for i in frutas:
    print(i)

buscar = 'goiaba'
frutas = ['banana', 'abacaxi', 'goiaba', 'abacate']
for i in frutas:
    if i == buscar:
        a = (f"Fruta Encontrada {buscar}")
        break
    else:
        a = (f"Fruta não encontrada {buscar}")
print(a)