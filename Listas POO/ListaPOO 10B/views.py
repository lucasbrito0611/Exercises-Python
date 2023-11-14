from models.cliente import Cliente, NCliente
from models.servico import Servico, NServico
from models.agenda import Agenda, NAgenda
import datetime

class View:
    def cliente_inserir(nome, email, fone, senha):
        if nome == '' or email == '' or fone == '' or senha == '': raise ValueError('Preencha os valores vazios!')
        if NCliente.ver_email(email) == False: raise ValueError('Email já cadastrado!')
        cliente = Cliente(0, nome, email, fone, senha)
        NCliente.inserir(cliente)

    def cliente_listar():
        return NCliente.listar()

    def cliente_listar_id(id):
        return NCliente.listar_id(id)

    def cliente_atualizar(id, nome, email, fone, senha):
        if nome == '' or email == '' or fone == '' or senha == '': raise ValueError('Preencha os valores vazios!')
        if NCliente.ver_email(email) == False: raise ValueError('Email já cadastrado!')
        cliente = Cliente(id, nome, email, fone, senha)
        NCliente.atualizar(cliente)

    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "", "")
        NCliente.excluir(cliente)    

    def cliente_admin():
        for cliente in View.cliente_listar():
            if cliente.get_nome() == "admin": return
        View.cliente_inserir("admin", "admin", "0000", "admin")  

    def cliente_login(email, senha):
        for cliente in View.cliente_listar():
            if cliente.get_email() == email and cliente.get_senha() == senha:
                return cliente
        return None

    def servico_listar():
        return NServico.listar()

    def servico_listar_id(id):
        return NServico.listar_id(id)

    def servico_inserir(descricao, valor, duracao):
        if descricao == '': raise ValueError('Preencha a descrição!')
        if valor < 0: raise ValueError('O valor não pode ser negativo!')
        if duracao <= 0: raise ValueError('A duração deve ser positiva!')

        NServico.inserir(Servico(0, descricao, valor, duracao))

    def servico_atualizar(id, descricao, valor, duracao):
        NServico.atualizar(Servico(id, descricao, valor, duracao))

    def servico_excluir(id):
        NServico.excluir(Servico(id, "", "", ""))

    def servico_reajustar(percentual):
        for servico in View.servico_listar():    
            NServico.atualizar(Servico(servico.get_id(), servico.get_descricao(), servico.get_valor() * (1 + percentual/100), servico.get_duracao()))

    def agenda_listar():
        return NAgenda.listar()

    def agenda_listarhoje():
        r = []
        hoje = datetime.datetime.today()
        for horario in View.agenda_listar():
            if horario.get_confirmado() == False and horario.get_data().date() == hoje.date():
                r.append(horario)
        return r    

    def agenda_inserir(data, confirmado, id_cliente, id_servico):
        NAgenda.inserir(Agenda(0, data, confirmado, id_cliente, id_servico))

    def agenda_atualizar(id, data, confirmado, id_cliente, id_servico):
        NAgenda.atualizar(Agenda(id, data, confirmado, id_cliente, id_servico))

    def agenda_excluir(id):
        NAgenda.excluir(Agenda(id, "", "", 0, 0))

    def agenda_abrir_agenda(data, hinicio, hfim, intervalo):
        data_inicio = datetime.datetime.strptime(f"{data} {hinicio}", "%d/%m/%Y %H:%M")
        data_fim = datetime.datetime.strptime(f"{data} {hfim}", "%d/%m/%Y %H:%M")
        delta = datetime.timedelta(minutes = intervalo) 
        aux = data_inicio

        if data_inicio < datetime.datetime.today():
            raise TypeError('A data não pode ter passado!')
        if intervalo <= 0:
            raise TypeError('O intervalo deve ser positivo!')

        while aux <= data_fim :
            NAgenda.inserir(Agenda(0, aux, False, 0, 0))
            aux = aux + delta