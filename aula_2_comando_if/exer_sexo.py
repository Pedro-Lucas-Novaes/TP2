import os
os.system('cls')


while True:
    sexo = input("Digite o seu sexo: M- Masculino F- Feminino: ")
    
    os.system('cls')

    if sexo.upper() == "M" or sexo.upper() == "F":
        
        altura = float(input("Digite a sua altura: "))
        
        os.system('cls')
        
        if sexo.upper() == "M":
            peso = (76.7 * altura)-58
            print(f"Para alguem do Gênero Masculino com {altura}cm de altura, O peso ideal seria de: {peso:.2f}Kg")
            break
        elif sexo.upper() == "F":
            peso = (62.1 * altura)-44.7
            print(f"Para alguem do Gênero Feminino com {altura}cm de altura, O peso ideal seria de: {peso:.2f}Kg")
            break
    else: 
        print("Sexo invalido!\nEscolha entre M ou F.\n")





