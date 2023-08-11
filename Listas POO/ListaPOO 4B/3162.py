numero = int(input())

lista = []
for linhas in range(numero):
    posicoes = list(map(int, input().split()))
    lista.append(posicoes)

print(lista)