import datetime

class Paciente:
    def __init__(self, nome, cpf, fone, nascimento):
        if nascimento > datetime.datetime.today(): raise ValueError('Data de nascimento inválida')
        self.__nome = nome
        self.__cpf = cpf
        self.__fone = fone
        self.__nascimento = nascimento
    
    def SetNome(Self, nome):
        Self.__nome = nome
    def SetCpf(self, cpf):
        self.__cpf = cpf
    def SetFone(self, fone):
        self.__fone = fone
    def SetNascimento(self, nascimento):
        if nascimento > datetime.datetime.today():
            raise ValueError('Data de nascimento inválida')
        self.__nascimento = nascimento

    def GetNome(self):
        return self.__nome
    def GetCpf(self):
        return self.__cpf
    def GetFone(self):
        return self.__fone
    def GetNascimento(self):
        return self.__nascimento

    def __str__(self):
        return f"{self.__nome} - {self.__cpf} - {self.__fone} - {self.__nascimento.strftime('%d/%m/%Y')}"

nome = input('Digite o nome: ')
cpf = input('Digite o CPF: ')
fone = input('Digite o telefone: ')
nasc_txt = input('Digite a data de nascimento: ')
nasc = datetime.datetime.strptime(nasc_txt, '%d/%m/%Y')

try:
    p = Paciente(nome, cpf, fone, nasc)
    print(p)
except ValueError as erro:
    print(erro)