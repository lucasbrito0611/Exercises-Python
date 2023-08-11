lista = []

for i in range(100):
    entrada = float(input())
    lista.append(entrada)

for k in range (len(lista)):
    if lista[k] <= 10:
        print(f'A[{k}] = {lista[k]}')