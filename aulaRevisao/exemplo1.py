op = int(input("Digite a opção:\n 1-Calculo Perimetro \n 2-Calculo Area \n 3-Sair\n"))

match op:

    case 1:
        # leitura de dados e conversão de valores
        ladoa = float(input("Digite o lado a do retangulo:\n "))
        ladob = float(input("Digite o lado b do retangulo:\n "))

        calculo = 2 * ladoa + 2 * ladob
        
        # para converter o resultado com dois numeros :.2f
        print(f"O Resultado do perimetro é {calculo:.2f}")
    
    case 2:
        # leitura de dados e conversão de valores
        ladoa = float(input("Digite o lado a do retangulo:\n "))
        ladob = float(input("Digite o lado b do retangulo:\n "))

        calculo = ladoa * ladob
        
        # para converter o resultado com dois numeros :.2f
        print(f"O Resultado da area é {calculo:.2f}")

    case 3:
        exit

    case _:
        print("opção incorreta")