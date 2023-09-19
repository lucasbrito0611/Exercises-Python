import datetime

from cliente import Cliente, NCliente
from servico import Servico, NServico
from agenda import Agenda, NAgenda

class UI:
    @classmethod
    def Main(cls):
        op = None
        while(op != 99):
            op = UI.Menu()
            if op == 1: UI.ClienteInserir()
            if op == 2: UI.ClienteListar()
            if op == 3: UI.ClienteAtualizar()
            if op == 4: UI.ClienteExcluir()
            if op == 5: UI.ServicoInserir()
            if op == 6: UI.ServicoListar()
            if op == 7: UI.ServicoAtualizar()
            if op == 8: UI.ServicoExcluir()
            if op == 9: UI.AgendaInserir()
            if op == 10: UI.AgendaListar()
            if op == 11: UI.AgendaAtualizar()
            if op == 12: UI.AgendaExcluir()
            if op == 13: UI.AbrirAgenda()
    
    @classmethod
    def Menu(cls):
        print('\nCLIENTE:1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 99-Sair\nSERVIÇO:5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir, 99-Sair\nAGENDA:9-Inserir, 10-Listar, 11-Atualizar, 12-Excluir, 13-Abrir Agenda, 99-Sair')
        return int(input())
    
    @classmethod
    def ClienteInserir(cls):
        nome = input("Nome: ")
        email = input("E-mail: ")
        fone = input("fone: ")
        cliente = Cliente(0, nome, email, fone)
        
        NCliente.inserir(cliente)
    
    @classmethod
    def ClienteListar(cls):
        for cliente in NCliente.listar():
            print(cliente)
    
    @classmethod
    def ClienteAtualizar(cls):
        UI.ClienteListar()
        id = int(input("Id do cliente a ser atualizado: "))
        nome = input("Novo nome: ")
        email = input("Novo e-mail: ")
        fone = input("Novo fone: ")
        cliente = Cliente(id, nome, email, fone)
        NCliente.atualizar(cliente)    
    
    @classmethod
    def ClienteExcluir(cls):
        UI.ClienteListar()
        id = int(input("Id do cliente a ser excluído: "))
        cliente = Cliente(id, "", "", "")
        NCliente.excluir(cliente)

    @classmethod
    def ServicoInserir(cls):
        descricao = input('Descrição: ')
        valor = float(input('Valor: '))
        duracao = int(input('Duração: '))
        servico = Servico(0, descricao, valor, duracao)

        NServico.inserir(servico)

    @classmethod
    def ServicoListar(cls):
        for servico in NServico.listar():
            print(servico)

    @classmethod
    def ServicoAtualizar(cls):
        UI.ServicoListar()
        id = int(input('ID do serviço a ser atualizado: '))
        descricao = input('Nova descrição: ')
        valor = float(input('Novo valor: '))
        duracao = float(input('Nova duração: '))

        servico = Servico(id, descricao, valor, duracao)
        NServico.atualizar(servico)

    @classmethod
    def ServicoExcluir(cls):
        UI.ServicoListar()
        id = int(input('ID do cliente a ser excluído: '))
        servico = Servico(id, '', '', '')
        NServico.excluir(servico)

    @classmethod
    def AgendaInserir(cls):
        idCliente = int(input('ID do Cliente: '))
        idServico = int(input('ID do Serviço: '))
        data_txt = input('Data: ')
        data = datetime.datetime.strptime(data_txt, '%d/%m/%Y %H:%M')
        conf = input('Confirmado: ')

        agenda = Agenda(0, idCliente, idServico, data, conf)
        NAgenda.inserir(agenda)

    @classmethod
    def AgendaListar(cls):
        for agenda in NAgenda.listar():
            print(agenda)
    
    @classmethod
    def AgendaAtualizar(cls):
        UI.AgendaListar()
        id = int(input('ID da agenda a ser atualizada: '))
        idCliente = int(input('Novo ID do cliente: '))
        idServico = int(input('Novo ID do serviço: '))
        data_txt = input('Nova data: ')
        data = datetime.datetime.strptime(data_txt, '%d/%m/%Y %H:%M')
        conf = input('Confirmado: ')

        agenda = Agenda(id, idCliente, idServico, data, conf)
        NAgenda.atualizar(agenda)

    @classmethod
    def AgendaExcluir(cls):
        UI.AgendaListar()
        id = int(input('ID da agenda a ser excluída: '))
        agenda = Agenda(id, '', '', '', '')
        NAgenda.excluir(agenda)

    @classmethod
    def AbrirAgenda(cls):
        data_txt = input('Data: ')
        data = datetime.datetime.strptime(data_txt, '%d/%m/%Y')

        print(data)
UI.Main()