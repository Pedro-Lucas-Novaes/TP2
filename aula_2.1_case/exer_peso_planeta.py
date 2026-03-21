import os 
os.system('cls')


peso = float(input('Digite o seu peso (em kg): '))
pesoPlaneta = float()
planeta = int(input('Digite um número de planeta, sendo: \n 1 - Mercúrio \n 2 - Vênus \n 3 - Marte \n 4 - Júpiter \n 5 - Saturno \n Digite sua opção: '))

if planeta > 0 & planeta < 6:
    match planeta:
        case 1:
            pesoPlaneta = peso * 0.37
            print(f'Seu peso em Mercúrio é de: {pesoPlaneta:.2f} kg.')

        case 2:
            pesoPlaneta = peso * 0.88
            print(f'Seu peso em Vênus é de: {pesoPlaneta:.2f} kg.')

        case 3:
            pesoPlaneta = peso * 0.38
            print(f'Seu peso em Marte é de: {pesoPlaneta:.2f} kg.')

        case 4:
            pesoPlaneta = peso * 2.64
            print(f'Seu peso em Júpiter é de: {pesoPlaneta:.2f} kg.')

        case 5:
            pesoPlaneta = peso * 1.15
            print(f'Seu peso em Saturno é de: {pesoPlaneta:.2f} kg.')
        
        case _:
            print('Opção Inválida.')