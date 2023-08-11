class Retangulo:
    def __init__(self, b, h):
        self.__b = 0
        self.__h = 0

        self.SetBase(b)
        self.SetAltura(h)

    def SetBase(self, b):
        if b >= 0: self.__b = b
        else: raise ValueError()
    def SetAltura(self, h):
        if h >= 0: self.__h = h
        else: raise ValueError()

    def GetBase(self):
        return self.__b
    def GetAltura(self):
        return self.__h

    def CalcArea(self):
        return f'Área= {self.__b * self.__h}'
    def CalcDiagonal(self):
        return f'Diagonal= {((self.__b * 2) + (self.__h ** 2)) ** 0.5:.1f}'

    def __str__(self):
        return f'Base: {self.__b} - Altura: {self.__h}'

class UI:
    @staticmethod
    def main():
        b = float(input('Digite a base do retângulo: '))
        h = float(input('Digite a altura do retângulo: '))

        r = Retangulo(b, h)

        print(r)
        print(r.CalcArea())
        print(r.CalcDiagonal())

UI.main()