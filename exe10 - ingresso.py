class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def ImprimeValor(self):
        print(f"O valor do ingresso normal é R${self.valor}.")


class Vip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def ImprimeValor(self, percentual): #polimorfismo
        ValorVip = self.valor + ((self.valor * percentual) / 100)
        print(f"O ingresso VIP custa R${ValorVip}.")


Ingresso1 = Vip(200)
Ingresso1.ImprimeValor(50)
