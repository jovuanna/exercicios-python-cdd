#soma de dois números
def soma(a, b):
    soma = a + b
    print(f"A soma dos números {a} e {b} é igual a: {soma}")
#soma de numeros com quantidade indeterminada
def somaindet(*num):
    total = 0
    for a in num:
        total += a
    return total
#soma com retorno
def soma2(a, b):
    soma = a + b
    return soma

#subtração de dois números
def sub(a, b):
    sub = a - b
    print(f"A subtração dos números {a} e {b} é igual a: {sub}")
#multiplicação de dois números
def mult(a, b):
    mult = a * b
    print(f"A multiplicação dos números {a} e {b} é igual a: {mult}")
#divisão de dois números
def div(a, b):
    div = a / b
    print(f"A divisão dos números {a} e {b} é igual a: {div}")
#piramides de número
def piramide1(n):
    for a in range(1, n+1):
        print(str(a)*a)
def piramide2(p):
    for a in range(1, p+1):
        for b in range(1, a+1):
            print(b, end=' ')
        print()
#quantidade de vogais em uma frase
def vogais(t):
    cont = 0
    for a in t:
        if a in 'aeiouAEIOU':
            cont += 1
            print(cont)
#estoque
def estoque(prod, quant, valor):
    total = quant * valor
    return prod, total
#quantidade de letras de um texto e texto invertido
def letras(*texto):
    cont = 0
    invertido = texto[::-1]
    for a in texto:
        for b in a:
            if b != " " and b != "," and b != ".":
                cont += 1
        return invertido, cont