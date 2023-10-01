from views import Views

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
        
        Views.cliente_inserir(nome, email, fone)
    
    @classmethod
    def ClienteListar(cls):
        for cliente in Views.cliente_listar():
            print(cliente)
    
    @classmethod
    def ClienteAtualizar(cls):
        UI.ClienteListar()
        id = int(input("Id do cliente a ser atualizado: "))
        nome = input("Novo nome: ")
        email = input("Novo e-mail: ")
        fone = input("Novo fone: ")  

        Views.cliente_atualizar(id, nome, email, fone)
    
    @classmethod
    def ClienteExcluir(cls):
        UI.ClienteListar()
        id = int(input("Id do cliente a ser excluído: "))

        Views.cliente_excluir(id)

    @classmethod
    def ServicoInserir(cls):
        descricao = input('Descrição: ')
        valor = float(input('Valor: '))
        duracao = int(input('Duração: '))
        
        Views.servico_inserir(descricao, valor, duracao)
    
    @classmethod
    def ServicoListar(cls):
        for servico in Views.servico_listar():
            print(servico)

    @classmethod
    def ServicoAtualizar(cls):
        UI.ServicoListar()
        id = int(input('ID do serviço a ser atualizado: '))
        descricao = input('Nova descrição: ')
        valor = float(input('Novo valor: '))
        duracao = float(input('Nova duração: '))

        Views.servico_atualizar(id, descricao, valor, duracao)

    @classmethod
    def ServicoExcluir(cls):
        UI.ServicoListar()
        id = int(input('ID do cliente a ser excluído: '))

        Views.servico_excluir(id)

    @classmethod
    def AgendaInserir(cls):
        data_txt = input('Data e horário: ')
        UI.ClienteListar()
        idCliente = int(input('ID do Cliente: '))
        UI.ServicoListar()
        idServico = int(input('ID do Serviço: '))
        conf = True

        Views.agenda_inserir(data_txt, idCliente, idServico, conf)

    @classmethod
    def AgendaListar(cls):
        for agenda in Views.agenda_listar():
            print(agenda)
    
    @classmethod
    def AgendaAtualizar(cls):
        UI.AgendaListar()
        id = int(input('ID da agenda a ser atualizada: '))
        data_txt = input('Nova data e horário: ')
        idCliente = int(input('Novo ID do cliente: '))
        idServico = int(input('Novo ID do serviço: '))
        conf = input('Confirmado: ')

        Views.agenda_atualizar(id, data_txt, idCliente, idServico, conf)

    @classmethod
    def AgendaExcluir(cls):
        UI.AgendaListar()
        id = int(input('ID da agenda a ser excluída: '))

        Views.agenda_excluir(id)

    @classmethod
    def AbrirAgenda(cls):
        data_txt = input('Data: ')
        
        while True:
            hora_ini_txt = input('Hora inicial: ')
            hora_fin_txt = input('Hora final: ')
            if hora_ini_txt >= hora_fin_txt:
                print('A hora inicial deve ser menor que a hora final.')
            else:
                contador_txt = input('Contador: ')
                Views.abrir_agenda(data_txt, hora_ini_txt, hora_fin_txt, contador_txt)

                break
UI.Main()