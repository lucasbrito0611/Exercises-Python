import json

class Servico:
    def __init__(self, id, descricao, valor, duracao):
        self.__id = id
        self.__descricao = descricao
        self.__valor = valor
        self.__duracao = duracao

    def set_id(self, id): self.__id = id
    def set_descricao(self, descricao): self.__descricao = descricao
    def set_valor(self, valor): self.__valor = valor
    def set_duracao(self, duracao): self.__duracao = duracao

    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_valor(self): return self.__valor
    def get_duracao(self): return self.__duracao

    def __str__(self):
        return f'{self.__id} - {self.__descricao} - {self.__valor} - {self.__duracao}'

class NServico:
    __servicos = []

    @classmethod
    def inserir(cls, obj):
        NServico.abrir()
        id = 0 
        for servico in cls.__servicos:
            if servico.get_id() > id: id = servico.get_id()

        obj.set_id(id + 1)
        cls.__servicos.append(obj)  
        NServico.salvar()

    @classmethod
    def listar(cls):
        NServico.abrir()
        return cls.__servicos

    @classmethod
    def listar_id(cls, id):
        NServico.abrir()
        for servico in cls.__servicos:
            if servico.get_id() == id: return servico
        return None

    @classmethod
    def atualizar(cls, obj):
        NServico.abrir()
        servico = cls.listar_id(obj.get_id())
        servico.set_descricao(obj.get_descricao())
        servico.set_valor(obj.get_valor())
        servico.set_duracao(obj.get_duracao())
        NServico.salvar()

    @classmethod
    def excluir(cls, obj):
        NServico.abrir()
        servico = cls.listar_id(obj.get_id())
        cls.__servicos.remove(servico)    
        NServico.salvar()

    @classmethod
    def abrir(cls):
        try:
            cls.__servicos = []
            with open("servicos.json", mode="r") as f:
                s = json.load(f)
                for servico in s:
                    ser = Servico(servico["_Servico__id"], servico["_Servico__descricao"], servico["_Servico__valor"], servico["_Servico__duracao"])
                    cls.__servicos.append(ser)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("servicos.json", mode="w") as f:
            json.dump(cls.__servicos, f, default=vars, indent=1)