import datetime

class Paciente:
    def __init__(self, nome, cpf, fone, nasc):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = fone
        self.__nascimento = nasc

    def Idade(self):
        hoje = datetime.datetime.today()
        calc = hoje - self.__nascimento
        total_dias = calc.days
        ano = total_dias // 365
        meses = (total_dias % 365) // 30
        dias = (total_dias % 365) % 30
        
        if meses == 0:
            if dias == 0:
                return f'Idade = {ano} anos'
            else:
                return f'Idade = {ano} anos e {dias} dias'

        elif meses != 0:
            if dias == 0:
                return f'Idade = {ano} anos e {meses} meses'
            else:
                return f'Idade = {ano} anos, {meses} meses e {dias} dias'
    
    def __str__(self):
        return f"Nome: {self.__nome}\nCPF: {self.__cpf}\nTelefone: {self.__telefone}\nData de Nascimento: {self.__nascimento.strftime('%d/%m/%Y')}"

class UI:
    def main():
        nome = input('Digite seu nome: ')
        cpf = input('Digite seu CPF no formato xxx.xxx.xxx-yy: ')
        fone = input('Digite seu telefone no formato (xx) yyyyy-zzzz: ')
        
        nasc = input('Digite a sua data de nascimento no formato dd/mm/yyyy: ')
        data = datetime.datetime.strptime(nasc, "%d/%m/%Y")

        p = Paciente(nome, cpf, fone, data)

        print(p)
        print(p.Idade())

UI.main()