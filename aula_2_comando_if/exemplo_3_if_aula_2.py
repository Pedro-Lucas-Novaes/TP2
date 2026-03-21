import os
os.system('cls')



print('$$$ Programa de Empréstimos $$$ \n Responda(0-Não 1-Sim)')

neg = int(input("Possui nome negativo? "))
if neg == 1:
    print('você não pode realizar empréstimo')
else:
    cartass = int(input("Você possui carteira assinada? "))
    if cartass == 0:
        print("Não pode realizar empréstimo")
    else:
        casa = int(input("Possui casa própria? "))
        if casa == 0:
            print("Não pode realizar empréstimo")
        else:
            print("Conceder o empréstimo")