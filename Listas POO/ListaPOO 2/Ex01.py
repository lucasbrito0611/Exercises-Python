import math

class Circulo:
    def __init__(self, raio):
        self.__raio = 0
        
        self.set_raio(raio)

    def set_raio(self, raio):
        self.__raio = raio
    def get_raio(self):
        return self.__raio

    def calc_area(self):
        return math.pi * (self.__raio ** 2)
    def calc_circunferencia(self):
        return 2 * math.pi * self.__raio

class UI:
    @staticmethod
    def main():
        raio = float(input('Digite o comprimento do raio: '))

        c = Circulo(raio)
        
        print(f'Área do Círculo: {c.calc_area():.1f}')
        print(f'Circunferência do Círculo: {c.calc_circunferencia():.1f}')

UI.main()