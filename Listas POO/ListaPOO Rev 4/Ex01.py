class Jogador:
    def __init__(self, nomejog, camisa, gols):
        self.__nomejog = nomejog
        self.__camisa = camisa
        self.__gols = gols

    def GetNome(self):
        return self.__nomejog

    def GetGols(self):
        return self.__gols

    def __str__(self):
        return f'Nome do jogador: {self.__nomejog}\nNº da camisa: {self.__camisa}\nNº de gols: {self.__gols}'

class Time:
    def __init__(self, nometime, estado):
        self.__nometime = nometime
        self.__estado = estado
        self.__jogadores = []

    def Inserir(self, jogador):
        self.__jogadores.append(jogador)

    def Listar(self):
        return self.__jogadores

    def Artilheiro(self):
        if len(self.__jogadores) == 0:
            return None
        art = self.__jogadores[0]
        for jogador in self.__jogadores:
            if jogador.GetGols() > art.GetGols():
                art = jogador
        
        return f'Artilheiro: {art.GetNome()}'
    
    def __str__(self):
        return f'Nome do time: {self.__nometime}\nEstado: {self.__estado}'

class UI:
    def menu():
        print('1 - Novo time, 2 - Inserir jogador, 3 - Listar jogadores, 4 - Artilheiro, 0 - Fim: ')

    def main():
        op = None
        team = 0
        
        while op != 0:
            if op == 1:
                nometime = input('Digite o nome do time: ')
                estado = input('Digite o estado do time: ')
                
                time = Time(nometime, estado)
                print(time)

                team = 1

            if op == 2:
                if team == 0:
                    print('Crie um time antes de inserir um jogador.')
                else:
                    nomejog = input('Digite o nome do jogador: ')
                    camisa = int(input('Digite o número da camisa: '))
                    gols = int(input('Digite a quantidade de gols que o jogador fez: '))
    
                    jogador = Jogador(nomejog, camisa, gols)
                    time.Inserir(jogador)
                    print(jogador)

            if op == 3:
                if team == 0:
                    print('Crie um time antes de listar os jogadores.')
                else:
                    print('Jogadores no time:')
                    for jogador in time.Listar():
                        print(f'{jogador.GetNome()} - {jogador.GetGols()} gols')

            if op == 4:
                if team == 0:
                    print('Crie um time antes de saber o artilheiro.')
                else:
                    print(time.Artilheiro())

            op = int(input('1 - Novo time, 2 - Inserir jogador, 3 - Listar jogadores, 4 - Artilheiro, 0 - Fim: '))

UI.main()