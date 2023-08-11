import datetime

class Recorde:
    def __init__(self, atleta, nac, data, tempo):
        self.__atleta = atleta
        self.__nacionalidade = nac
        self.__data = data
        self.__tempo = tempo

    def GetAtleta(self):
        return self.__atleta
    def GetTempo(self):
        return self.__tempo
    
    def __str__(self):
        return f"Atleta: {self.__atleta}\nNacionalidade: {self.__nacionalidade}\nData: {self.__data.strftime('%d/%m/%Y')}\nTempo: {self.__tempo}"
    
class Esporte:
    def __init__(self, nome, prova):
        self.__nome = nome
        self.__prova = prova
        self.__recordes = []

    def Inserir(self, recorde):
        self.__recordes.append(recorde)

    def Listar(self):
        return self.__recordes
    
    def MenorTempo(self):
        menor = self.__recordes[0]
        for recorde in self.__recordes:
            if recorde.GetTempo() < menor.GetTempo():
                menor = recorde
        
        return f'{menor.GetAtleta()} - {menor.GetTempo()}' 
    
    def __str__(self):
        return f'Nome: {self.__nome}\nProva: {self.__prova}'
    
class UI:
    
    def main():
            nome = input('Digite o nome do esporte: ')
            prova = input('Digite o nome da prova: ')

            esporte = Esporte(nome, prova)
            print(esporte)

            for recorde in range(1,4):   
                atleta = input('Digite o nome do atleta: ')
                nac = input('Digite a nacionalidade do atleta: ')
                data_str = input('Digite a data que ocorreu o recorde (dd/mm/yyyy): ')
                data = datetime.datetime.strptime(data_str, '%d/%m/%Y')
                tempo_str = input('Digite o tempo que ocorreu o recorde (hh:mm:ss): ')
                hrs, min, sec = map(int, tempo_str.split(':'))
                tempo = datetime.timedelta(hours = hrs, minutes = min, seconds = sec)

                recorde = Recorde(atleta, nac, data, tempo)
                print(recorde)

                esporte.Inserir(recorde)

            print()        
            
            print('Lista dos recordes:')
            for record in esporte.Listar():
                print(f'{record.GetAtleta()} - {record.GetTempo()}')
            
            print()
            
            print('Recorde de menor tempo:')
            print(esporte.MenorTempo())
                        
UI.main()