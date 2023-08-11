class Cliente:
    def __init__(self, nome_cli, cpf, limite):
        self.__nomecli = nome_cli
        self.__cpf = cpf
        self.__limite = limite
        self.__socio = None
    
    def GetNome(self):
        return self.__nomecli
    
    def SetSocio(self, socio):
        self.__socio = socio
        socio.__socio = self

    def GetLimite(self):
        if self.__socio != None:
            return f'R$ {self.__limite + self.__socio.__limite:.2f}'
        else:
            return f'R$ {self.__limite:.2f}'
    
    def __str__(self):
        return f'Nome do cliente: {self.__nomecli}\nCPF do cliente: {self.__cpf}\nLimite do cliente: R$ {self.__limite:.2f}'

class Empresa:
    def __init__(self, nome_emp):
        self.__nomeemp = nome_emp
        self.__clientes = []

    def Inserir(self, cliente):
        self.__clientes.append(cliente)

    def Listar(self):
        return self.__clientes
    
    def __str__(self):
        return f'Nome da empresa: {self.__nomeemp}'

class UI:
    @staticmethod
    def menu():
        print('1 - Nova empresa, 2 - Inserir cliente, 3- Nova associação, 4 - Listar clientes, 0 - Fim: ')
    
    @staticmethod
    def main():
        op = None
        indice = 0

        while op != 0:
            op = int(input('1 - Nova empresa, 2 - Inserir cliente, 3- Nova associação, 4 - Listar clientes, 0 - Fim: '))
            if op == 1:
                if indice == 0:
                    nome_emp = input('Digite o nome da empresa: ')
                    empresa = Empresa(nome_emp)
                    print(empresa)
                else:
                    print('Você não pode criar duas empresas.')
                indice = 1
            if op == 2:
                if indice == 0:
                    print('Crie uma empresa antes de inserir um cliente.')
                else:
                    nome = input('Digite o nome do cliente: ')
                    cpf = input('Digite o cpf do cliente: ')
                    limite = float(input('Digite o limite do cliente: '))

                    cliente = Cliente(nome, cpf, limite)
                    empresa.Inserir(cliente)
                    print(cliente)
            if op == 3:
                if indice == 0:
                    print('Crie uma empresa antes de associar clientes.')
                elif len(empresa.Listar()) < 2:
                    print('Você precisa ter pelo menos dois clientes para fazer uma associação.')
                else:
                    nome1 = input('Digite o nome do primeiro cliente: ')
                    nome2 = input('Digite o nome do segundo cliente: ')

                    cliente1 = None
                    cliente2 = None
            
                    for cliente in empresa.Listar():
                        if cliente.GetNome() == nome1:
                            cliente1 = cliente
                        if cliente.GetNome() == nome2:
                            cliente2 = cliente

                    if cliente1 == None or cliente2 == None:
                        print('Os clientes não foram achados na empresa.')
                    elif cliente1 == cliente2:
                        print('Os dois sócios devem ser diferentes')
                    else:
                        cliente1.SetSocio(cliente2)
                        print('Assosiação feita com sucesso.')
            
            if op == 4:
                if indice == 0:
                    print('Crie uma empresa antes de listar os clientes.')
                else:
                    listar = empresa.Listar()
                    print('Clientes na empresa:')
                    for clientes in listar:
                        print(f'{clientes.GetNome()} - {clientes.GetLimite()}')
            

UI.main()