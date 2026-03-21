import os
os.system('cls')


nomes = ["maria", "joao", "paulo", "magali"]

while True:
    buscar = input("Digite o nome que deseja buscar: ").lower()

    for i in nomes:
        if i == buscar:
            print(f"Nome Encontrado {buscar}")
            break
    else:
        os.system('cls')
        print(f"Nome não encontrado {buscar}")
        continue
    break
print("\nPrograma Encerrado...")