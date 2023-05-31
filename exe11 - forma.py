class Forma:
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calculaArea(self, altura, base):
        self.area = altura * base
        print(f"A área do retângulo é {self.area}.")


    def calculaPerimetro(self, altura, base):
        self.perimetro = altura * 2 + base * 2
        print(f"O perímetro do triângulo é {self.perimetro}.")


class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def calculaArea(self, altura, base):
        area = (base * altura) / 2
        print(f"A área do triângulo é {area}.")


    def calculaPerimetro(self, lado1, lado2, lado3):
        perimetro = lado1 + lado2 + lado3
        print(f"O perímetro do triângulo é {perimetro}")

retangulo1 = Retangulo()
retangulo1.calculaArea(30, 20)
retangulo1.calculaPerimetro(30, 20)

triangulo1 = Triangulo()
triangulo1.calculaArea(4, 10)
triangulo1.calculaPerimetro(4, 7, 9)
