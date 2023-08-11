import enum
import datetime

class Midia(enum.Enum):
    LP = 0
    CD = 1
    DVD = 2
    BD = 3
    Stream = 4

class Album:
    def __init__(self, titulo, formato, gravadora, lancamento):
        self.__titulo = titulo
        self.__formato = formato
        self.__gravadora = gravadora
        self.__lancamento = lancamento

        self.SetTitulo(titulo)
        self.SetFormato(formato)
        self.SetGravadora(gravadora)
        self.SetLancamento(lancamento)

    def SetTitulo(self, titulo):
        self.__titulo = titulo
    def SetFormato(self, formato):
        if Midia[formato]:
            self.__formato = formato
        else: raise KeyError()
    def SetGravadora(self, gravadora):
        self.__gravadora = gravadora
    def SetLancamento(self, lancamento):
        self.__lancamento = lancamento
    
    def GetTitulo(self):
        return self.__titulo
    def GetFormato(self):
        return self.__formato
    def GetGravadora(self):
        return self.__gravadora
    def GetLancamento(self):
        return self.__lancamento

    def __str__(self):
        return f"Título: {self.__titulo}\nFormato: {self.__formato}\nGravadora: {self.__gravadora}\nLançamento: {self.__lancamento.strftime('%d/%m/%Y')}"

class Banda:
    def __init__(self, nome, pais, estilo):
        self.__nome = nome
        self.__pais = pais
        self.__estilo = estilo
        self.__albuns = []

    def Inserir(self, album):
        self.__albuns.append(album)
    
    def Listar(self):
        return self.__albuns
    
    def Ultimo(self):
        ultimo = self.__albuns[0]
        for album in self.__albuns:
            if album.GetLancamento() > ultimo.GetLancamento():
                ultimo = album

        return f"{ultimo.GetTitulo()} - {ultimo.GetLancamento().strftime('%d/%m/%Y')}"
    
    def __str__(self):
        return f'Nome da banda: {self.__nome}\nPaís da banda: {self.__pais}\nEstilo musical: {self.__estilo}'
    
class UI:
    def main():
        nome = input('Digite o nome da banda: ')
        pais = input('Digite o país da banda: ')
        estilo = input('Digite o estilo musical da banda: ')

        banda = Banda(nome, pais, estilo)
        print(banda)
        print()

        for albuns in range(1,4):
            titulo = input('Digite o título do álbum: ')
            formato = input('Digite o formato do álbum: ')
            gravadora = input('Digite a gravadora do álbum: ')
            lancamento_txt = input('Digite a data de lançamento do álbum (dd/mm/yyyy): ')
            lancamento = datetime.datetime.strptime(lancamento_txt, '%d/%m/%Y')

            album = Album(titulo, formato, gravadora, lancamento)
            banda.Inserir(album)

            print(album)

            print()

        print('Listas dos álbuns:')
        for album in banda.Listar():
            print(f"{album.GetTitulo()} - {album.GetLancamento().strftime('%d/%m/%Y')}")
        
        print()

        print('Último lançamento:')
        print(banda.Ultimo())

UI.main()