lista = []

print('Digite dez valores inteiros')
numeros = input().split()

for x in numeros:
    lista.append(x)

for i in range(len(lista)):
    lista[i] = int(lista[i])

print(f'O maior valor é {max(lista)} e o menor valor é {min(lista)}')