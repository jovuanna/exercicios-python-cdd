def vogais(t):
    cont = 0
    for a in t:
        if a in 'aeiouAEIOU':
            cont += 1
            print(cont)
texto = "O rato roeu a roupa do rei de roma"
vogais(texto)