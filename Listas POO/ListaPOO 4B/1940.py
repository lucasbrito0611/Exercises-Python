jogadores, rodadas = map(int, input().split())
jogadas = list(map(int, input().split()))

lista = []
for i in range(jogadores):
    soma = sum(jogadas[i::jogadores])
    lista.append(soma)

posicao = None
maior = max(lista)

if lista.count(maior) > 1:
    posicao = len(lista) - 1 - lista[::-1].index(maior)
else:
    posicao = lista.index(maior)

print(posicao + 1)