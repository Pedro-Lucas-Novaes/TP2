num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
op = input("Digite a operação: ")

def operacao(op):
    match op:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case _:
            return "OPERAÇÃO INVALIDA"
        
print(operacao(op))