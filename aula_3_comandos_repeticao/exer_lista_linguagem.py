import os
os.system('cls')

linguagens = ["python", "c#", "Visual Basic", "C++", "Delphi", "Cobol"]

total_caracteres = 0

for i in linguagens:
    total_caracteres += len(i)
    if len(i) > 3:
        print(f"A linguagem {i} possui mais de 3 caracteres.")

print("\n")
for i in linguagens:
    print(f"A linguagem {i} possui {len(i)} caracteres.")
