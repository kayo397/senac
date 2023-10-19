import math

class FiguraPlana:
    def __init__(self, base_menor, base_maior, altura):
        self.base_menor = base_menor
        self.base_maior = base_maior
        self.altura = altura

    def calcular_area(self):
        pass

class TrianguloRetangulo(FiguraPlana):
    def __init__(self, base_menor, base_maior, altura):
        super().__init__(base_menor, base_maior, altura)

    def calcular_area(self):
        return 0.5 * self.base_maior * self.altura

class Retangulo(FiguraPlana):
    def __init__(self, base_menor, base_maior, altura):
        super().__init__(base_menor, base_maior, altura)

    def calcular_area(self):
        return self.base_menor * self.altura

class Circulo(FiguraPlana):
    def __init__(self, raio):
        super().__init__(raio, raio, None)

    def calcular_area(self):
        return math.pi * self.base_menor**2

class Losango(FiguraPlana):
    def calcular_area(self):
        return (self.base_menor * self.base_maior) / 2

class Paralelogramo(FiguraPlana):
    def __init__(self, base, altura):
        super().__init__(base, base, altura)

    def calcular_area(self):
        return self.base_menor * self.altura

class Trapezio(FiguraPlana):
    def __init__(self, base_menor, base_maior, altura):
        super().__init__(base_menor, base_maior, altura)

    def calcular_area(self):
        return 0.5 * (self.base_menor + self.base_maior) * self.altura

# Exemplo de uso
triangulo = TrianguloRetangulo(5, 3, 4)
print("Área do Triângulo:", triangulo.calcular_area())

retangulo = Retangulo(4, 6, 4)
print("Área do Retângulo:", retangulo.calcular_area())

circulo = Circulo(3)
print("Área do Círculo:", circulo.calcular_area())

losango = Losango(4, 6, 4)
print("Área do Losango:", losango.calcular_area())

paralelogramo = Paralelogramo(5, 4)
print("Área do Paralelogramo:", paralelogramo.calcular_area())

trapezio = Trapezio(5, 3, 4)
print("Área do Trapézio:", trapezio.calcular_area())
