class Pessoa:
    def __init__(self, nome, peso, idade, comendo=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo


p1 = Pessoa("João", 80, 18) #OBJETO PESSOA
print(p1.nome, p1.peso)
print(vars(p1))
p2 = Pessoa("Maria", 54, 19, comendo=True)
print(p2.nome, p2.peso, p2.idade, p2.comendo)
print(vars(p2))
