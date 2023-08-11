print('Digite o primeiro horário no formato hh:mm')
horario1 = input().split(':')

print('Digite o segundo horário no formato hh:mm')
horario2 = input().split(':')

lista = [horario1[0], horario1[1], horario2[0], horario2[1]]

for i in range(len(lista)):
    lista[i] = int(lista[i])


minutos_totais = (lista[0] * 60) + (lista[2] * 60) + lista[1] + lista[3]
horas = minutos_totais // 60
minutos = minutos_totais - (horas * 60)

if 0 <= horas < 10: 
    print(f'Total de horas = 0{horas}:{minutos}')

else:
    print(f'Total de horas = {horas}:{minutos}')