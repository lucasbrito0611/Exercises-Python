print('Digite uma data no formato dd/mm/aaaa')
dia, mes, ano = input().split('/')

ano = int(ano)
mes = int(mes)
dia = int(dia)

if ano < 1900 or ano > 2100 or mes < 1 or mes > 12 or dia < 1 or dia > 31:
    print('A data informada não é válida')

else:
    print('A data informada é válida')