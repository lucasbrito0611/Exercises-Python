class Esporte:
    def __init__(self, nomeesp, horarios, mensalidade):
        self.__nomeesp = nomeesp
        self.__horarios = horarios
        self.__mensalidade = mensalidade
    
    def GetNome(self):
        return self.__nomeesp
    def GetMensalidade(self):
        return self.__mensalidade
    
    def __str__(self):
        return f'Nome do esporte: {self.__nomeesp}\nHorários: {self.__horarios}\nMensalidade: R$ {self.__mensalidade:.2f}'
    
class Academia:
    def __init__(self, nomeacad, endereco):
        self.__nomeacad = nomeacad
        self.__endereco = endereco
        self.__esportes = []

    def Inserir(self, esporte):
        self.__esportes.append(esporte)

    def Listar(self):
        return self.__esportes
    
    def MediaMensalidade(self):
        mensalidade = 0
        if len(self.__esportes) == 0:
            return 'Insira um esporte para saber a média mensal.'
        else:
            for esporte in self.__esportes:
                mensalidade += esporte.GetMensalidade()
            
            media = mensalidade / len(self.__esportes)
            return f'Media mensal = R$ {media:.2f}'
    
    def __str__(self):
        return f'Nome da academia: {self.__nomeacad}\nEndereço: {self.__endereco}'
    
class UI:
    def menu():
        print('1 - Nova academia, 2 - Inserir esporte, 3 - Listar esportes, 4 - Média mensal, 0 - Fim: ')

    def main():
        op = None
        acad = 0

        while op != 0:
            if op == 1:
                if acad == 1:
                    print('Você não pode criar duas academias.')
                else:
                    nomeacad = input('Digite o nome da academia: ')
                    endereco = input('Digite o endereço da academia: ')

                    academia = Academia(nomeacad, endereco)
                    print(academia)
                    acad = 1

            if op == 2:
                if acad == 0:
                    print('Crie uma academia antes de inserir um esporte.')
                else:
                    nomeesp = input('Digite o nome do esporte: ')
                    horarios = input('Digite o(s) horário(s) do esporte: ')
                    mensalidade = float(input('Digite o valor da mensalidade do esporte: '))

                    esporte = Esporte(nomeesp, horarios, mensalidade)
                    print(esporte)
                    academia.Inserir(esporte)
            
            if op == 3:
                if acad == 0:
                    print('Crie uma academia antes de inserir um esporte.')
                else:
                    if len(academia.Listar()) == 0:
                        print('Nenhum esporte foi inserido.')
                    else:
                        print('Esportes na academia:')
                        for esporte in academia.Listar():
                            print(esporte.GetNome())
                    
            if op == 4:
                if acad == 0:
                    print('Crie uma academia antes de inserir um esporte.')
                else:
                    print(academia.MediaMensalidade())

            op = int(input('1 - Nova academia, 2 - Inserir esporte, 3 - Listar esportes, 4 - Média mensal, 0 - Fim: '))

UI.main()