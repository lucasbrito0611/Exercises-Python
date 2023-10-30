import datetime
from models.cliente import Cliente, NCliente
from models.servico import Servico, NServico
from models.agenda import Agenda, NAgenda

class Views:
    @classmethod
    def cliente_inserir(cls, nome, email, senha, fone):
        cliente = Cliente(0, nome, email, senha, fone)
        if NCliente.ver_email(email) == True:
            NCliente.inserir(cliente)
            return True
        else: 
            return False
    @classmethod
    def cliente_listar(cls):
        return NCliente.listar()
    @classmethod
    def cliente_atualizar(cls, id, nome, email, senha, fone):
        cliente = Cliente(id, nome, email, senha, fone)
        NCliente.atualizar(cliente)
    @classmethod
    def cliente_excluir(cls, id):
        cliente = Cliente(id, '', '', '')
        NCliente.excluir(cliente)

    @classmethod
    def servico_inserir(cls, descricao, valor, duracao):
        servico = Servico(0, descricao, valor, duracao)
        NServico.inserir(servico)
    @classmethod
    def servico_listar(cls):
        return NServico.listar()
    @classmethod
    def servico_atualizar(cls, id, descricao, valor, duracao):
        servico = Servico(id, descricao, valor, duracao)
        NServico.atualizar(servico)
    @classmethod
    def servico_excluir(cls, id):
        servico = Servico(id, '', '', '')
        NServico.excluir(servico)

    @classmethod
    def agenda_inserir(cls, data_txt, confirmado, idCliente, idServico):
        data = datetime.datetime.strptime(data_txt, '%d/%m/%Y %H:%M')
        agenda = Agenda(0, data, confirmado, idCliente, idServico)
        NAgenda.inserir(agenda)
    @classmethod
    def agenda_listar(cls):
        return NAgenda.listar()
    @classmethod
    def agenda_atualizar(cls, id, data_txt, confirmado, idCliente, idServico):
        data = datetime.datetime.strptime(data_txt, '%d/%m/%Y %H:%M')

        agenda = Agenda(id, data, confirmado, idCliente, idServico)
        NAgenda.atualizar(agenda)
    @classmethod
    def agenda_excluir(cls, id):
        agenda = Agenda(id, '', '', '', '')
        NAgenda.excluir(agenda)

    @classmethod
    def abrir_agenda_do_dia(cls, data_txt, hora_ini_txt, hora_fin_txt, contador_txt):
        data = datetime.datetime.strptime(data_txt, '%d/%m/%Y')
        hora_ini = datetime.datetime.strptime(hora_ini_txt, '%H:%M')
        hora_fin = datetime.datetime.strptime(hora_fin_txt, '%H:%M')
        contador = datetime.datetime.strptime(contador_txt, '%H:%M')
        conf = False

        while hora_ini <= hora_fin:
                data_e_horario = datetime.datetime(data.year, data.month, data.day, hora_ini.hour, hora_ini.minute)

                agenda = Agenda(0, data_e_horario, conf, 0, 0)
                NAgenda.inserir(agenda)

                hora_ini += datetime.timedelta(minutes=contador.minute, hours=contador.hour)