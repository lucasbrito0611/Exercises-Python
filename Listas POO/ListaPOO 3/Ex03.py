class Equacao:

    def __init__(self, a, b, c):
        self.__a = 0
        self.__b = 0
        self.__c = 0

        self.SetA(a)
        self.SetB(b)
        self.SetC(c)

    def SetA(self, a):
        if a != 0: self.__a = a
        else: raise ValueError('O coeficiente a deve ser um número não nulo.')

    def SetB(self, b):
        self.__b = b

    def SetC(self, c):
        self.__c = c

    def GetA(self):
        return self.__a

    def GetB(self):
        return self.__b

    def GetC(self):
        return self.__c

    def CalcDelta(self):
        return (self.__b ** 2) - (4 * self.__a * self.__c)
    def TemRaizesReais(self):
        if Equacao.CalcDelta(self) < 0:
            return 'negativo'
        elif Equacao.CalcDelta(self) == 0:
            return 'nulo'
        else:
            return 'positivo'
    def Raiz1(self):
        raiz1 = (-self.__b + Equacao.CalcDelta(self) ** (1/2)) / (2 * self.__a)
        return raiz1
    def Raiz2(self):
        raiz2 = (-self.__b - Equacao.CalcDelta(self) ** (1/2)) / (2 * self.__a)
        return raiz2
    
    def __str__(self):
        return f'Coeficiente A: {self.__a} - Coeficiente B: {self.__b} - Coeficiente C: {self.__c}'


class UI:
    @staticmethod
    def main():
        a = int(input('Digite o coeficiente A: '))
        b = int(input('Digite o coeficiente B: '))
        c = int(input('Digite o coeficiente C: '))

        e = Equacao(a, b, c)

        print(e)
        
        if e.TemRaizesReais() == 'negativo':
            print('Essa equação não possui raízes reais.')
        elif e.TemRaizesReais() == 'nulo':
            print('Essa equação possui apenas uma raíz.')
            print(f'Raíz = {e.Raiz1():.2f}')
        else:
            print('Essa equação possui duas raízes.')
            print(f'Raízes = {e.Raiz1():.2f} e {e.Raiz2():.2f}')
UI.main()

# -------------------------------------------------------------------------------------------
#                                 DIAGRAMA:
#                                 Equacao
#                                 - a : int
#                                 - b : int
#                                 - c : int
# -------------------------------------------------------------------------------------------
#                                 + Equacao(a: int, b: int, c: int)
#                                 + SetA(a: int) : void
#                                 + SetB(b: int) : void
#                                 + SetC(c: int) : void
#                                 + GetA() : int
#                                 + GetB() : int
#                                 + GetC() : int
#                                 + CalcDelta() : int
#                                 + TemRaizesReais() : string
#                                 + Raiz1() : double
#                                 + Raiz2() : double
#                                 + ToString() : string