lista = []
for i in range(1,31):
    if i % 3 == 0:
        i = (i * -1)
        lista.append(i)

    if i % 3 != 0:
        lista.append(i)

print('Resultado: ', end='')
for x in lista:
    print(x, end=' ')