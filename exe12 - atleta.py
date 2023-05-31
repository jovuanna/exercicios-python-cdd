class Atleta:
    def __init__(self, peso, aposentado):
        self.aposentado = aposentado
        self.peso = peso

    def aposentar(self):
        ...

    def aquecer(self):
        ...

class Corredor(Atleta):
    def __init__(self, peso, aposentado):
        super().__init__(peso, aposentado)

    def aposentar(self):
        if self.aposentado == True:
            self.aposentado = False
            print(f"O atleta com {self.peso}Kg está aposentado.")
        else:
            self.aposentado = True
            print(f"O atleta com {self.peso}Kg não está aposentado")


    def aquecer(self):
        if self.aposentado == True:
            print(f"Está aposentado não vai aquecer")
        else:
            self.aposentado = False
            print(f"Está aquecendo")

    def correr(self):
        if self.aposentado == True:
            print("Não pode correr pois está aposentado.")
        else:
            print("Está correndo.")


class Nadador(Atleta):
    def __init__(self, peso, aposentado):
        super().__init__(peso, aposentado)

    def aquecer(self):
        if self.aposentado == True:
            print(f"Está aposentado não vai aquecer")
        else:
            self.aposentado = False
            print(f"Está aquecendo")

    def aposentar(self):
        if self.aposentado == False:
            self.aposentado = True
            print(f"O atleta com {self.peso}Kg está aposentado.")
        else:
            self.aposentado = False
            print(f"O atleta com {self.peso}Kg não está aposentado")

    def nadar(self):
        if self.aposentado == False:
            print(f"O atleta com {self.peso} está nadando.")
        else:
            print(f"O atleta não pode nadar pois está aposentado.")
print('-'*20)
corredor1 = Corredor(80, aposentado=False)
corredor1.aposentar()
corredor1.aquecer()
corredor1.correr()
print('-'*20)
corredor2 = Corredor(50, aposentado=True)
corredor2.aposentar()
corredor2.aquecer()
corredor2.correr()
print('-'*20)
nadador1 = Nadador(80, aposentado=False)
nadador1.aposentar()
nadador1.aquecer()
nadador1.nadar()
print('-'*20)
nadador2 = Nadador(50, aposentado=True)
nadador2.aposentar()
nadador2.aquecer()
nadador2.nadar()
