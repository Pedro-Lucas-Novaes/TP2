import os
os.system('cls')


while True:
    try:
        op = int(input("Digite o indice de poluição: "))
        os.system('cls')

        if 0 <= op <= 2 :
            print("Considerar Aceitável")
            break
        elif 3 <= op <= 5:
            print("Suspender Atividades Grupo 1")
            break
        elif 6 <= op <= 7:
            print("Suspender Atividades Grupo 2")
            break
        elif op >= 8:
            print("Suspender Atividades de todos os grupos")
            break
    except ValueError:
            os.system('cls')
            print("numero invalido, por favor inserir apenas numeros...")
            
















#match op:
#    case 0 | 1 | 2:
#        print("")
#    case 3 | 4 | 5:
#        print("")
#    case 6 | 7:
#        print("")
#    case 8