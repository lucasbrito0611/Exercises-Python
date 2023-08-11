lista = []

for i in range(10):
    entrada = int(input())
    if entrada <= 0: 
        entrada = 1
    lista.append(entrada)

for k in range (len(lista)):
    print(f'X[{k}] = {lista[k]}')