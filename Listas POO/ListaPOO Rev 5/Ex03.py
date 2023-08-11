import enum
import datetime

class Ensino(enum.Enum):
    Infantil = 0
    Fundamental = 1
    Médio = 2
    Superior = 3
    Técnico = 4

class TipoAmbiente(enum.Enum):
    SalaAula = 0
    SalaAdministrativa = 1
    Laboratorio = 2
    QuadraEsporte = 3
    Auditorio = 4
    Lanchonete = 5
    Banheiro = 6

class Ambiente:
    def __init__(self, nome_amb, area, capacidade, tipo):
        self.__nome_amb = nome_amb
        self.__area = area
        self.__capacidade = capacidade
        self.__tipo = tipo

        self.SetNome_amb(nome_amb)
        self.SetArea(area)
        self.SetCapacidade(capacidade)
        self.SetTipo(tipo)

    def SetNome_amb(self, nome_amb):
        self.__nome_amb = nome_amb
    def SetArea(self, area):
        if area >= 0: self.__area = area
        else: raise ValueError()
    def SetCapacidade(self, capacidade):
        if capacidade >= 0: self.__capacidade = capacidade
        else: raise ValueError()
    def SetTipo(self, tipo):
        if TipoAmbiente[tipo]:
            self.__tipo = tipo
        else:
            raise KeyError()

    def GetNome_amb(self):
        return self.__nome_amb
    def GetArea(self):
        return self.__area
    def GetCapacidade(self):
        return self.__capacidade
    def GetTipo(self):
        return self.__tipo
    
    def __str__(self):
        return f'Nome: {self.__nome_amb}\nArea: {self.__area} m2\nCapacidade: {self.__capacidade}\nTipo: {self.__tipo}'
    
class Escola:
    def __init__(self, nome_esc, endereco, fundacao, nivel):
        self.__nome_esc = nome_esc
        self.__endereco = endereco
        self.__fundacao = fundacao
        self.__nivel = nivel
        self.__ambientes = []

        self.SetNivel(nivel)
    
    def SetNivel(self, nivel):
        if Ensino[nivel]:
            self.__nivel = nivel
        else:
            raise KeyError()
    
    def Inserir(self, ambiente):
        self.__ambientes.append(ambiente)

    def Listar(self):
        return self.__ambientes
    
    def Soma(self):
        soma = 0
        for ambiente in self.__ambientes:
            soma += ambiente.GetArea()
        
        return soma

    def __str__(self):
        return f"Nome: {self.__nome_esc}\nEndereço: {self.__endereco}\nFundação: {self.__fundacao.strftime('%d/%m/%Y')}\nNível: {self.__nivel}"
    
class UI:
    def main():
        nome_esc = input('Digite o nome da escola: ')
        endereco = input('Digite o endereço da escola: ')
        fundacao_txt = input('Digite a data de fundação da escola: ')
        fundacao = datetime.datetime.strptime(fundacao_txt, '%d/%m/%Y')
        nivel = input('Digite o nível de ensino da escola: ')

        escola = Escola(nome_esc, endereco, fundacao, nivel)
        print(escola)
        print()

        for i in range(1,4):
            nome_amb = input('Digite o nome do ambiente: ')
            area = float(input('Digite a área do ambiente em m2: '))
            capacidade = int(input('Digite a capacidade do ambiente: '))
            tipo = input('Digite o tipo do ambiente: ')

            ambiente = Ambiente(nome_amb, area, capacidade, tipo)
            print(ambiente)
            escola.Inserir(ambiente)

            print()

        print('Lista dos ambientes:')
        for ambiente in escola.Listar():
            print(f'{ambiente.GetNome_amb()} - {ambiente.GetArea()} m2')
        print()

        print('Área da escola:')
        print(f'{escola.Soma()} m2')

UI.main()