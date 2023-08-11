class Frete:
    def __init__(self, d, p):
        self.__d = 0
        self.__p = 0

        self.SetDistancia(d)
        self.SetPeso(p)

    def SetDistancia(self, d):
        if d >= 0: self.__d = d
        else: raise ValueError('A distância deve ser um número não negativo')
    def SetPeso(self, p):
        if p >= 0: self.__p = p
        else: raise ValueError('O peso deve ser um número não negativo')

    def GetDistancia(self):
        return self.__d
    def GetPeso(self):
        return self.__p

    def CalcFrete(self):
        centavos = self.__d * self.__p
        reais = centavos / 100
        
        return f'Frete = R${reais:.2f}'

    def __str__(self):
        return f'Distância: {self.__d} - Peso: {self.__p}'

class UI:
    @staticmethod
    def main():
        d = float(input('Digite a distância percorrida em km: '))
        p = float(input('Digite o peso em kg: '))

        f = Frete(d, p)

        print(f)
        print(f.CalcFrete())

UI.main()