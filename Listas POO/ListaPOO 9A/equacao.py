class Equacao:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def SetA(self, a): self.__a = a
    def SetB(self, b): self.__b = b
    def SetC(self, c): self.__c = c
    def GetA(self): return self.__a 
    def GetB(self): return self.__b 
    def GetC(self): return self.__c 

    def Delta(self):
        return ((self.__b**2) - (4 * self.__a * self.__c))
    def TemRaizesReais(self):
        if self.Delta() < 0: return False
        else: return True
    def Raiz1(self):
        return ((- self.__b) + (self.Delta() ** 0.5)) / 2 * self.__a
    def Raiz2(self):
        return ((- self.__b) - (self.Delta() ** 0.5)) / 2 * self.__a
    
    def __str__(self):
        return f'A = {self.__a}\nB = {self.__b}\nC = {self.__c}'