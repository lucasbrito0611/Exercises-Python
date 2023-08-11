entrada = int(input())
numeros = list(map(int, input().split()))

menor = min(numeros)
posicao = numeros.index(menor)

print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')