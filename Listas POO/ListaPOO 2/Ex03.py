class Viagem:
    def __init__(self, d, t):
        self.__distancia = 0
        self.__tempo = 0

        self.set_distancia(d)
        self.set_tempo(t)
    
    def set_distancia(self, d):
        if d >= 0: self.__distancia = d         
        else: raise ValueError()
    def set_tempo(self, t):
        if t >= 0: self.__tempo = t  
        else: raise ValueError()
    
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    
    def velocidade_media(self):
        if self.__tempo == 0: return 0
        return self.__distancia / self.__tempo
    
class UI:
    @staticmethod
    def main():
        d = float(input('Digite a distância percorrida em km: '))
        t = input('Digite o tempo em hh:mm: ')
        
        horas, minutos = map(int, t.split(':'))
        horas = horas + (minutos / 60)
        
        v = Viagem(d, horas)

        print(f'Velocidade media = {v.velocidade_media():.2f} km/h')

UI.main()

# -------------------------------------------------------------------------------------------
#                                 DIAGRAMA:
#                                 Cinema
#                                 - dia : string
#                                 - horario : int
# -------------------------------------------------------------------------------------------
#                                 + Cinema(dia: string, horario: int)
#                                 + set_dia(dia: string) : void
#                                 + set_horario(horario: double) : void
#                                 + get_dia() : string
#                                 + get_horario() : double
#                                 + inteira() : int
#                                 + meia_entrada() : int