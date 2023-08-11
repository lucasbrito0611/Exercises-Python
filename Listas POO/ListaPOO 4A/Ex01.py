import random

class Bingo:
    def __init__(self):
        self.__numBolas = 10
        self.__sorteados = []

    def Iniciar(self, numBolas):
        if numBolas > 0: 
            self.__numBolas = numBolas
            self.__sorteados = []
        else: raise ValueError('O número de bolas deve ser maior que 0')
    def Proximo(self):
        if len(self.__sorteados) == self.__numBolas:
            return 'Game Over'
        
        bolas = random.randrange(1, self.__numBolas + 1)
        while bolas in self.__sorteados:
            bolas = random.randrange(1, self.__numBolas + 1)
        self.__sorteados.append(bolas)
        return bolas

    def Sorteados(self):
        crescente = self.__sorteados
        crescente.sort()
        return crescente

class UI:
    @staticmethod
    def main():
        op = int(input('1 - Novo jogo, 2- Sortear, 3 - Sorteados, 0 - Fim: '))
        jogo = Bingo()

        while op != 0:
            if op == 1:
                numero = int(input('Digite o numero de bolas: '))
                jogo.Iniciar(numero)
            if op == 2:
                p = jogo.Proximo()
                if p == 'Game Over':
                    print('Todas as bolas já foram sorteadas.')
                else:
                    print('Bola sorteada:', p)
            if op == 3:
                print(f'Bolas já sorteadas: {jogo.Sorteados()}')
            op = int(input('1 - Novo jogo, 2- Sortear, 3 - Sorteados, 0 - Fim: '))

UI.main()