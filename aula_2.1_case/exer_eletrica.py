import os
os.system('cls')

print("********** CALCULO DE GRANDEZAS ELETRICAS **********\n")
print("Tensão(v)")
print("Resistencia(r)")
print("Corrente(i)\n")

while True:
    try:

        op = int(input("Escolhar uma das opções: \n \n 1-Tensão (em Volt) \n 2-Resistência (em Ohm) \n 3-Corrente (em Ampére) \n \n Digite a sua opção: "))


        match op:
            case 1:
                r = float(input("Digite o valor de R: "))
                i = float(input("Digite o valor de I: "))
                u = r * i
                print(f"Tensão(u) = {u}V")
                break
            case 2:
                while True:
                    u = float(input("Digite o valor de U: "))
                    i = float(input("Digite o valor de I: "))
                    if i != 0:
                        r = u / i
                        print(f"Resistência(R) = {r}Ohms")
                        break
                    else:
                        os.system('cls')
                        print("Corrente não pode ser zero!")
                break
            case 3:
                while True:
                    u = float(input("Digite o valor de U: "))
                    r = float(input("Digite o valor de R: "))
                    if r != 0:
                        i = u / r
                        print(f"Corrente(i) = {i}A")
                        break
                    else:
                        os.system('cls')
                        print("Resistência não pode ser zero!")
                break
    except ValueError:
           print("\nOpção invalida, escolha uma das 3 opções...\n ")