def decrescente(lista):
    for i in range(1,11):
        lista.append(i)

    return sorted(lista, reverse=True)

lista = []
print('Resultado: ', end='')
for x in decrescente(lista):
    print(x, end=' ')