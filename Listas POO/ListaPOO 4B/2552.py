linha, coluna = map(int, input().split())
lista = []

for linhas in range(linha):
    lista.append([])
    for colunas in range(coluna):
        lista[linhas].append(0)

for linhas in range(linha):
    for colunas in range(coluna):
        if lista[linhas][colunas] == 0:
