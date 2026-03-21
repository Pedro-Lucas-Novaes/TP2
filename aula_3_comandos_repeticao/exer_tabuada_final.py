import os
os.system('cls')

i = int(input("Digite o numero que deseja começar a tabuada: "))
f = int(input("Digite o numero que deseja terminar a tabuada: "))
while i <= f:
    print(f"4 x {i} = {4 * i}")
    i += 1