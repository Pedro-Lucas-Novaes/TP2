#Exemplo Estrutura condicional IF - Média

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

#comando IF = SE -- elif = SENÃO -- else = SENÃO
if media > 6.0:
    print(f"Aluno Aprovado!, a média é: {media:.2f}")
elif media > 5.0 and media < 6.0:
    print(f"Aluno está de Exame, a sua média é: {media:.2f}")
else:
    print(f"Aluno Reprovado!, a média é: {media:.2f}")