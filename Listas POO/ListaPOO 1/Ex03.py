class Viagem:
    def __init__(self):
        self.distancia = 0
        self.tempo = 0

    def calculo(self):
        horas = int(self.tempo[0])
        minutos = int(self.tempo[1])

        tempototal = ((horas * 60) + minutos) / 60

        velocidade = self.distancia / tempototal

        return (f'{velocidade:.0f} Km/h')

x = Viagem()
x.distancia = int(input('Digite a distância: '))
x.tempo = input('Digite o tempo no formato hh:mm:').split(':')

print(x.calculo())