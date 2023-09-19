import datetime
import json

class Agenda:
    def __init__(self, id, idCliente, idServico, data, confirmado):
        self.__id = id
        self.__idCliente = idCliente
        self.__idServico = idServico
        self.__data = data
        self.__confirmado = confirmado

    def set_id(self, id): self.__id = id
    def set_idCliente(self, idCliente): self.__idCliente = idCliente
    def set_idServico(self, idServico): self.__idServico = idServico
    def set_data(self, data): self.__data = data
    def set_confirmado(self, confirmado): self.__confirmado = confirmado

    def get_id(self): return self.__id
    def get_idCliente(self): return self.__idCliente
    def get_idServico(self): return self.__idServico
    def get_data(self): return self.__data
    def get_confirmado(self): return self.__confirmado

    def to_json(self):
        return { '__id': self.__id, '__data': self.__data.strftime('%d/%m/%Y %H:%M'), '__confirmado': self.__confirmado, '__idCliente': self.__idCliente, '__idServico': self.__idServico }

    def __str__(self):
        return f"{self.__id} - {self.__idCliente} - {self.__idServico} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__confirmado}"

class NAgenda:
    __agendas = []

    @classmethod
    def inserir(cls, obj):
        NAgenda.abrir()
        id = 0 
        for agenda in cls.__agendas:
            if agenda.get_id() > id: id = agenda.get_id()
    
        obj.set_id(id + 1)
        cls.__agendas.append(obj)  
        NAgenda.salvar()

    @classmethod
    def listar(cls):
        NAgenda.abrir()
        return cls.__agendas

    @classmethod
    def listar_id(cls, id):
        NAgenda.abrir()
        for agenda in cls.__agendas:
            if agenda.get_id() == id: return agenda
        return None

    @classmethod
    def atualizar(cls, obj):
        NAgenda.abrir()
        cliente = cls.listar_id(obj.get_id())
        cliente.set_idCliente(obj.get_idCliente())
        cliente.set_idServico(obj.get_idServico())
        cliente.set_data(obj.get_data())
        cliente.set_confirmado(obj.get_confirmado())
        NAgenda.salvar()

    @classmethod
    def excluir(cls, obj):
        NAgenda.abrir()
        agenda = cls.listar_id(obj.get_id())
        cls.__agendas.remove(agenda)    
        NAgenda.salvar()

    @classmethod
    def abrir(cls):
        try:
            cls.__agendas = []
            with open("agendas.json", mode="r") as f:
                s = json.load(f)
                for agenda in s:
                    a = Agenda(agenda["__id"], agenda["__idCliente"], agenda["__idServico"], datetime.datetime.strptime(agenda["__data"], '%d/%m/%Y %H:%M'), agenda["__confirmado"])
                    cls.__agendas.append(a)
        except FileNotFoundError:
            pass
  
    @classmethod
    def salvar(cls):
        with open("agendas.json", mode="w") as f:
            json.dump(cls.__agendas, f, default = Agenda.to_json, indent=1)