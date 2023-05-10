def soma(a, b):
    soma = a + b
    print(f"A soma dos números {a} e {b} é igual a: {soma}")
def sub(a, b):
    sub = a - b
    print(f"A subtração dos números {a} e {b} é igual a: {sub}")
def mult(a, b):
    mult = a * b
    print(f"A multiplicação dos números {a} e {b} é igual a: {mult}")
def div(a, b):
    div = a / b
    print(f"A divisão dos números {a} e {b} é igual a: {div}")


print('''1 - SOMA
2 - SUB
3 - MULTIPLICAÇÃO
4 - DIVIDIR
5 - SAIR''')
while True:
    Opcao = int(input("Digite uma opção: "))
    if Opcao == 5:
        break
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    if Opcao == 1:
        soma(num1, num2)
    elif Opcao == 2:
        sub(num1, num2)
    elif Opcao == 3:
        mult(num1, num2)
    elif Opcao == 4:
        div(num1, num2)
    else:
        print("Erro! Digite uma opção válida.")
