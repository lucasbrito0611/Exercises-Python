operacao = input()
lista = []

for linhas in range(0,12):
    lista.append([])
    for colunas in range(0,12):
        lista[linhas].append(0)

for linhas in range (0,12):
    for colunas in range(0,12):
        lista[linhas][colunas] = float(input())

soma = 0

for linhas in range (0,12):
    for colunas in range(0,12):
        if linhas < colunas:
            soma += lista[linhas][colunas]

media = soma / 66

if operacao == 'S':
    print(f'{soma:.1f}')
if operacao == 'M':
    print(f'{media:.1f}')