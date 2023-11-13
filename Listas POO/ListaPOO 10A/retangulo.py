class Retangulo:
    def __init__(self, b, h):
        if b <= 0: raise ValueError('Base deve ser maior que zero')
        if h <= 0: raise ValueError('Altura deve ser maior que zero')
        self.__b = b
        self.__h = h

    def SetBase(self, b):
        if b <= 0:
            raise ValueError('Base deve ser maior que zero')
        else:
            self.__b = b
    def SetAltura(self, h):
        if h <= 0:
            raise ValueError('Altura deve ser maior que zero')
        else:
            self.__h = h

    def GetBase(self):
        return self.__b
    def GetAltura(self):
        return self.__h

    def __str__(self):
        return f'{self.__b} - {self.__h}'

base = int(input('Digite o valor da base: '))
altura = int(input('Digite o valor da altura: '))

try:
    r = Retangulo(base, altura)
    print(r)
except ValueError as erro:
    print(erro)