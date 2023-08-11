print('Digite uma data no formato dd/mm/aaaa')
dia, mes, ano = input().split('/')

ano = int(ano)
mes = int(mes)
dia = int(dia)

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

nome_mes = meses[mes-1]

print(f'A data é {dia} de {nome_mes} de {ano}')