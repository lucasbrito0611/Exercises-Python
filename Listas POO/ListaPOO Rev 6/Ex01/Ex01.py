import datetime

class Local:
    def __init__(self, id, nome, endereco, fone):
        self.__id = id
        self.__nome = nome
        self.__endereco = endereco
        self.__fone = fone

        self.SetNome(nome)
        self.SetEndereco(endereco)
        self.SetFone(fone)

    def SetNome(self, nome):
        self.__nome = nome
    def SetEndereco(self, endereco):
        self.__endereco = endereco
    def SetFone(self, fone):
        self.__fone = fone

    def GetID(self):
        return self.__id
    def GetNome(self):
        return self.__nome
    def GetEndereco(self):
        return self.__endereco
    def GetFone(self):
        return self.__fone
    
    def __str__(self):
        return f'ID: {self.__id} - Nome: {self.__nome} - Endereço: {self.__endereco} - Telefone: {self.__fone}'

class Evento:
    def __init__(self, id, idLocal, nome, data, valor):
        self.__id = id
        self.__idLocal = idLocal
        self.__nome = nome
        self.__data = data
        self.__valor_ingresso = valor

        self.SetNome(nome)
        self.SetData(data)
        self.SetValor(valor)

    def SetNome(self, nome):
        self.__nome = nome
    def SetData(self, data):
        self.__data = data
    def SetValor(self, valor):
        if valor.isdigit(): self.__valor_ingresso = valor
        else: raise ValueError()

    def GetID(self):
        return self.__id
    def GetID_Local(self):
        return self.__idLocal
    def GetNome(self):
        return self.__nome
    def GetData(self):
        return self.__data
    def GetValor(self):
        return self.__valor_ingresso
    
    def __str__(self):
        return f"ID: {self.__id} - ID do Local: {self.__idLocal} - Nome: {self.__nome} - Data do evento: {self.__data.strftime('%d/%m/%Y')} - Valor do ingresso: {self.__valor_ingresso}"
    
class Artista:
    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome

        self.SetNome(nome)

    def SetNome(self, nome):
        self.__nome = nome
    
    def GetID(self):
        return self.__id
    def GetNome(self):
        return self.__nome
    
    def __str__(self):
        return f'ID: {self.__id} - Nome: {self.__nome}'
    
class Personagem:
    def __init__(self, id, idEvento, idArtista, nome):
        self.__id = id
        self.__idEvento = idEvento
        self.__idArtista = idArtista
        self.__nome = nome

        self.SetNome(nome)

    def SetNome(self, nome):
        self.__nome = nome

    def GetID(self):
        return self.__id
    def GetID_Evento(self):
        return self.__idEvento
    def GetID_Artista(self):
        return self.__idArtista
    def GetNome(self):
        return self.__nome
    
    def __str__(self):
        return f'ID: {self.__id} - ID do Evento: {self.__idEvento} - ID do Artista: {self.__idArtista} - Nome: {self.__nome}'
    
class Curtida:
    def __init__(self, id, idEvento, idUsuario):
        self.__id = id
        self.__idEvento = idEvento
        self.__idUsuario = idUsuario

    def GetID(self):
        return self.__id
    def GetID_Evento(self):
        return self.__idEvento
    def GetID_Usuario(self):
        return self.__idUsuario
    
    def __str__(self):
        return f'ID: {self.__id} - ID do Evento: {self.__idEvento} - ID do Usuario: {self.__idUsuario}'
    
class Comentario:
    def __init__(self, id, idEvento, idUsuario, texto, data):
        self.__id = id
        self.__idEvento = idEvento
        self.__idUsuario = idUsuario
        self.__texto = texto
        self.__data = data

        self.SetTexto(texto)
        self.SetData(data)

    def SetTexto(self, texto):
        self.__texto = texto
    def SetData(self, data):
        self.__data = data

    def GetID(self):
        return self.__id
    def GetID_Evento(self):
        return self.__idEvento
    def GetID_Usuario(self):
        return self.__idUsuario
    def GetTexto(self):
        return self.__texto
    def GetData(self):
        return self.__data
    
    def __str__(self):
        return f"ID: {self.__id} - ID do Evento: {self.__idEvento} - ID do Usuário: {self.__idUsuario} - Texto: {self.__texto} - Data do comentário: {self.__data.strftime('%d/%m/%Y')}"

class Usuario:
    def __init__(self, id, nome, email, senha):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__senha = senha

        self.SetNome(nome)
        self.SetEmail(email)
        self.SetSenha(senha)
    
    def SetNome(self, nome):
        self.__nome = nome
    def SetEmail(self, email):
        self.__email = email
    def SetSenha(self, senha):
        self.__senha = senha

    def GetID(self):
        return self.__id
    def GetNome(self):
        return self.__nome
    def GetEmail(self):
        return self.__email
    def GetSenha(self):
        return self.__senha
    
    def __str__(self):
        return f'ID: {self.__id} - Nome: {self.__nome} - Email: {self.__email} - Senha: {self.__senha}'
    
class NLocal:
    def __init__(self):
        self.__locais = []
    
    def Inserir(self, local):
        self.__locais.append(local)
    def Remover(self, local):
        self.__locais.remove(local)
    def Atualizar(self, local):
        for obj in self.__locais:
            if obj.GetID() == local.GetID():
                obj.SetNome(local.GetNome())
                obj.SetEndereco(local.GetEndereco())
                obj.SetFone(local.GetFone())
    def Listar(self):
        return self.__locais
    

evento = Evento(1, 1, 'Show', datetime.datetime.strptime('06/08/2023', '%d/%m/%Y'), '50')
print(evento)
artista = Artista(1, 'Fulano de Tal')
print(artista)
personagem = Personagem(1, 1, 1, 'Guitarrista')
print(personagem)
curtida = Curtida(1, 1, 1)
print(curtida)
comentario = Comentario(1, 1, 1, 'Ótimo evento!', datetime.datetime.strptime('06/08/2023', '%d/%m/%Y'))
print(comentario)

usuario = Usuario(1, 'Fulano da Silva', 'fulano@example.com', 'senha123')
print(usuario)

local1 = Local(1, 'Midway', 'Rua Principal, 123', '555-1234')
local2 = Local(2, 'NS', 'Rua Principal, 456', '123-5555')

x = NLocal()
x.Inserir(local1)
x.Inserir(local2)

print()
print('Lista dos locais sem atualizar:')
for loc in x.Listar():
    print(loc)

local1_att = Local(1, 'Midway', 'Rua Principal, 136', '111-2222')
x.Atualizar(local1_att)
x.Remover(local2)

print()
print('Lista dos locais atualizada:')
for loc in x.Listar():
    print(loc)