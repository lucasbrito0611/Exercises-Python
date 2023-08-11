import enum

class Dias(enum.Enum):
    segunda = 1
    terca = 2
    quarta = 3
    quinta = 4
    sexta = 5
    
class Turno(enum.Enum):
    matutino = 1
    vespertino = 2
    noturno = 3

class Estagiario:
    def __init__(self, nome, cpf, fone, dias, turno):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = fone
        self.__dias = dias
        self.__turno = turno

        self.SetDias(dias)
        self.SetTurno(turno)

    def SetDias(self, dias):
        if Dias[dias]: 
            self.__dias = dias
            return 'Dia(s) selecionados com sucesso!'
        else: 
            raise KeyError()
    def SetTurno(self, turno):
        if Turno[turno]:
            self.__turno = turno
            return 'Turno selecionado com sucesso'
        else:
            raise KeyError()
        
    def GetDias(self):
        return self.__dias
    def GetTurno(self):
        return self.__turno
    
    def __str__(self):
        return f'Nome: {self.__nome}\nCPF: {self.__cpf}\nTelefone: {self.__telefone}\nDia(s) do estágio: {self.__dias}\nTurno do estágio: {self.__turno}'
    
class UI:
    def main():
        nome = input('Digite o nome do estagiário: ')
        cpf = input('Digite o CPF do estagiário: ')
        fone = input('Digite o telefone do estagiário: ')

        print('Dias disponíveis para o estágio:')
        for d in Dias:
            print(f'{d.value} - {d.name.capitalize()}')
        dias = input('Digite o dia disponível do estagiário: ')
        dias.lower()

        print('Turnos disponíveis para o estágio:')
        for t in Turno:
            print(f'{t.value} - {t.name.capitalize()}')
        turno = input('Digite o turno disponível do estagiário: ')

        estagiario = Estagiario(nome, cpf, fone, dias, turno)
        
        print('\nEstágiario matriculado com sucesso! Dados da matrícula:\n')
        print(estagiario)

UI.main()