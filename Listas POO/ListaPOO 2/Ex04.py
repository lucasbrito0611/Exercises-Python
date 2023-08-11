class Cinema:
    def __init__(self, dia, horario):
        self.__dia = ''
        self.__horario = 0

        self.set_dia(dia)
        self.set_horario(horario)

    def set_dia(self, dia):
        dias = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado']
        if dia in dias: self.__dia = dia
        else: raise ValueError()
    def set_horario(self, horario):
        if horario >= 0 and horario <= 23: self.__horario = horario
        else: raise ValueError()
            
    def get_dia(self):
        return self.__dia
    def get_horario(self):
        return self.__horario

    def inteira(self):
        valor = 20
        if self.__dia == 'quarta':
            valor = 8
        else:
            if self.__dia == 'segunda' or self.__dia == 'terça' or self.__dia == 'quinta':
                valor = 16
            if self.__horario >= 17 or self.__horario == 0:
                valor *= 1.5

        return valor
    def meia_entrada(self):
        if self.__dia == 'quarta': return 8
        return self.inteira() / 2

class UI:
    def main():
        dia = input('Digite o dia da semana: ')
        horario = input('Digite o horário da sessão: ')
        
        horas, minutos = map(int, horario.split(':'))
    
        c = Cinema(dia, horas)
    
        print(f'Inteira = R${c.inteira():.2f}')
        print(f'Meia-entrada = R${c.meia_entrada():.2f}')

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