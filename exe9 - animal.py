class Animal: #classe mãe
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"{self.nome} foi comer.")
    def emitir_som(self):
        print(f"{self.nome} {self.cor} está emitindo som.")


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class Gato(Animal): #herança
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitir_som(self):
        print(f"O gatinho {self.nome} {self.cor} foi miar.")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitir_som(self): #método
        print(f"O cachorro {self.nome} {self.cor} foi latir.")


gato1 = Gato("Ruby", "pretinho", ) #objeto
cachorro1 = Cachorro("Max", "caramelo")
vaca1 = Vaca("Jubicleusa", "branca e preta")

gato1.emitir_som()
cachorro1.emitir_som()
vaca1.emitir_som()