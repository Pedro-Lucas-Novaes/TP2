import os
os.system('cls')

maior = 0
mediana = 0
menor = 0
igual = 0

alt1 = input("Digite a altura da primeira pessoa: ")
alt2 = input("Digite a altura da segunda pessoa: ")
alt3 = input("Digite a altura da terceira pessoa: ")

os.system('cls')

if alt1 > alt2 and alt1 > alt3:
    maior = alt1
    if alt2 > alt3:
        mediana = alt2
        menor = alt3
    else:
        mediana = alt3
        menor = alt2
    print(f"A maior pessoa possui: {maior}cm de altura\nA pessoa mediana possui: {mediana}cm de altura\nE a menor pessoa: {menor}cm de altura")
elif alt2 > alt1 and alt2 > alt3:
    maior = alt2
    if alt1 > alt3:
        mediana = alt1
        menor = alt3
    else:
        mediana = alt3
        menor = alt1
    print(f"A maior pessoa possui: {maior}cm de altura\nA pessoa mediana possui: {mediana}cm de altura\nE a menor pessoa: {menor}cm de altura")
elif alt3 > alt1 and alt3 > alt2:
    maior = alt3
    if alt1 > alt2:
        mediana = alt1
        menor = alt2
    else:
        mediana = alt2
        menor = alt1
    print(f"A maior pessoa possui: {maior}cm de altura\nA pessoa mediana possui: {mediana}cm de altura\nE a menor pessoa: {menor}cm de altura")


    
        