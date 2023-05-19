class Pessoa:
    def __init__(self, nome, peso, idade, comendo=False, falando=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    def comer(self, comida):
        self.comida = comida
        if self.comendo == False:
            print(f"{self.nome} foi comer {comida}.")
            self.comendo = True
            print(f"{self.nome} está comendo {comida}.")
        elif self.comendo == True:
            print(f"Não fale")
            print(f"{self.nome} já está comendo {comida}.")
    def parar_comer(self):
        if self.comendo == True:
            self.comendo = False
            print(f"{self.nome} parou de comer.")
        else:
            print(f"{self.nome} não está comendo")
    def falar(self):
        if self.falando == True:
            print(f"{self.nome} está falando.")
        elif self.comendo == False:
            print(f"{self.nome} pode falar.")

    def parar_falar(self):
        if self.falando == True and self.comendo == True:
            print(f"{self.nome}, pare de falar.")

print('.'*50)
p1 = Pessoa("João", 80, 18, falando=True) #OBJETO PESSOA
p1.comer("banana")
p1.parar_comer()
p1.falar()
p1.parar_falar()

print('.'*50)
p2 = Pessoa("Maria", 54, 19, comendo=True, falando=True)
p2.comer("banana")
p2.parar_comer()
p2.falar()
p2.parar_falar()

print('.'*50)
p3 = Pessoa("Julia", 45, 23,)
p3.parar_comer()
p3.falar()
p3.parar_falar()
