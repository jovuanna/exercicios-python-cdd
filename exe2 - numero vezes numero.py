'''def piramide(n):
    for a in range(1, n+1):
        print(str(a)*a)
piramide(9)'''
def piramide(p):
    for a in range(1, p+1):
        for b in range(1, a+1):
            print(b, end=' ')
        print()
piramide(8)