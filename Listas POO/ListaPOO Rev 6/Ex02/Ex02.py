import datetime

class Campeonato:
    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome

    def SetNome(self, nome):
        self.__nome = nome

    def GetID(self):
        return self.__id
    def GetNome(self):
        return self.__nome
    
    def __str__(self):
        return f'ID: {self.__id} - Nome: {self.__nome}'
    
class Fase:
    def __init__(self, id, idCampeonato, nome):
        self.__id = id
        self.__idCampeonato = idCampeonato
        self.__nome = nome

    def SetNome(self, nome):
        self.__nome = nome
    
    def GetID(self):
        return self.__id
    def GetID_Camp(self):
        return self.__idCampeonato
    def GetNome(self):
        return self.__nome
    
    def __str__(self):
        return f'ID: {self.__id} - ID do Campeonato: {self.__idCampeonato} - Nome: {self.__nome}'

class Equipe: 
    def __init__(self, id, nome, pais):
        self.__id = id
        self.__nome = nome
        self.__pais = pais

    def SetNome(self, nome):
        self.__nome = nome
    def SetPais(self, pais):
        self.__pais = pais
    
    def GetID(self):
        return self.__id
    def GetNome(self):
        return self.__nome
    def GetPais(self):
        return self.__pais
    
    def __str__(self):
        return f'ID: {self.__id} - Nome: {self.__nome} - País: {self.__pais}'

class Jogo:
    def __init__(self, id, idFase, idEquipe, local, transmissao, data):
        self.__id = id
        self.__idFase = idFase
        self.__idEquipe = idEquipe
        self.__local = local
        self.__transmissao = transmissao
        self.__data = data

    def SetLocal(self, local):
        self.__local = local
    def SetTransmissao(self, transmissao):
        self.__transmissao = transmissao
    def SetData(self, data):
        self.__data = data

    def GetID(self):
        return self.__id
    def GetID_Fase(self):
        return self.__idFase
    def GetID_Equipe(self):
        return self.__idEquipe
    def GetLocal(self):
        return self.__local
    def GetTransmissao(self):
        return self.__transmissao
    def GetData(self):
        return self.__data
    
    def __str__(self):
        return f"ID: {self.__id} - ID da Fase: {self.__idFase} - ID da Equipe: {self.__idEquipe} - Local: {self.__local} - Transmissão: {self.__transmissao} - Data: {self.__data.strftime('%d/%m/%Y %H:%M')}"
    
class Jogador:
    def __init__(self, id, idEscalacao, idEquipe, numcamisa):
        self.__id = id
        self.__idEscalacao = idEscalacao
        self.__idEquipe = idEquipe
        self.__numcamisa = numcamisa

    def SetNumcamisa(self, numcamisa):
        self.__numcamisa = numcamisa

    def GetID(self):
        return self.__id
    def GetID_Escalacao(self):
        return self.__idEscalacao
    def GetID_Equipe(self):
        return self.__idEquipe
    def GetHorario(self):
        return self.__horario
    
    def __str__(self):
        return f'ID: {self.__id} - ID da Escalação: {self.__idEscalacao} - ID da Equipe: {self.__idEquipe} - Número da camisa: {self.__numcamisa}'

class Escalacao:
    def __init__(self, id, idEquipe, idJogador):
        self.__id = id
        self.__idEquipe = idEquipe
        self.__idJogador = idJogador

    def GetID(self):
        return self.__id
    def GetID_Equipe(self):
        return self.__idEquipe
    def GetID_Jogador(self):
        return self.__idJogador
    
    def __str__(self):
        return f'ID: {self.__id} - ID da Equipe: {self.__idEquipe} - ID do Jogador: {self.__idJogador}'

class Gol:
    def __init__(self, id, idJogo, idJogador, horario):
        self.__id = id
        self.__idJogo = idJogo
        self.__idJogador = idJogador
        self.__horario = horario

    def SetHorario(self, horario):
        self.__horario = horario

    def GetID(self):
        return self.__id
    def GetID_Jogo(self):
        return self.__idJogo
    def GetID_Jogador(self):
        return self.__idJogador
    def GetHorario(self):
        return self.__horario
    
    def __str__(self):
        return f"ID: {self.__id} - ID do Jogo: {self.__idJogo} - ID do Jogador: {self.__idJogador} - Horário do gol: {self.__horario}"
    
class Substituicao:
    def __init__(self, id, idEquipe, idJogador, idJogo):
        self.__id = id
        self.__idEquipe = idEquipe
        self.__idJogador = idJogador
        self.__idJogo = idJogo

    def GetID(self):
        return self.__id
    def GetID_Equipe(self):
        return self.__idEquipe
    def GetID_Jogador(self):
        return self.__idJogador
    def GetID_Jogo(self):
        return self.__idJogo
    
    def __str__(self):
        return f'ID: {self.__id} - ID da Equipe: {self.__idEquipe} - ID do Jogador: {self.__idJogador} - ID do Jogo: {self.__idJogo}'
    
class NEquipe:
    def __init__(self):
        self.__equipes = []

    def Inserir(self, equipe):
        self.__equipes.append(equipe)
    def Remover(self, equipe):
        self.__equipes.remove(equipe)
    def Atualizar(self, equipe):
        for obj in self.__equipes:
            if obj.GetID() == equipe.GetID():
                obj.SetNome(equipe.GetNome())
                obj.SetPais(equipe.GetPais())
    def Listar(self):
        return self.__equipes
    
camp = Campeonato(1, 'Copa Libertadores da América')
print(camp)
fase = Fase(1, 1, 'Semifinal')
print(fase)
jogo = Jogo(1, 1, 1, 'Arena das Dunas', 'ESPN', datetime.datetime.strptime('11/08/2023 16:30', '%d/%m/%Y %H:%M'))
print(jogo)
jogador = Jogador(1, 1, 1, 10)
print(jogador)
escal = Escalacao(1, 1, 1)
print(escal)
gol = Gol(1, 1, 1, datetime.timedelta(minutes=44, seconds=12))
print(gol)
subs = Substituicao(1, 1, 1, 1)
print(subs)

print()

equipe1 = Equipe(1, 'São Paulo', 'Brasil')
equipe2 = Equipe(2, 'Racing', 'Paraguai')
equipe3 = Equipe(3, 'Santos', 'Brasil')

equipes = NEquipe()

equipes.Inserir(equipe1)
equipes.Inserir(equipe2)
equipes.Inserir(equipe3)

print('Lista das equipes:')
for equipe in equipes.Listar():
    print(f'{equipe.GetNome()} - {equipe.GetPais()}')

equipe2_at = Equipe(2, 'Racing', 'Argentina')
equipes.Atualizar(equipe2_at)

print()

print('Lista das equipes atualizadas:')
for equipe in equipes.Listar():
    print(f'{equipe.GetNome()} - {equipe.GetPais()}')

equipes.Remover(equipe3)

print()

print('Lista das equipes atualizadas:')
for equipe in equipes.Listar():
    print(f'{equipe.GetNome()} - {equipe.GetPais()}')