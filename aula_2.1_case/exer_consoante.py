import os
os.system('cls')

op = input("Digite uma letra: ")

match op.lower():
    case "a" | "e" | "i" | "o" | "u":
        print(f"A letra {op.upper()} é uma vogal")
    case _:
        print(f"A letra {op.upper()} é uma consoante")
