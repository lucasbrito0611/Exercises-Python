numero = 1
indice = 0
lista = []
while numero < 46:
    numero = numero + indice
    indice += 1
    lista.append(numero)

print('Resultado: ', end='')
for i in lista:
    print(i, end=' ')