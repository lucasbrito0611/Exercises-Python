numero = 0
lista = []
soma = 0
while numero < 30:
    numero += 1
    lista.append(numero)
    soma = numero + (numero-1) + (numero-2)
    
    if numero % 3 == 0:
        lista.append(soma)

print('Resultado: ', end='')
for i in lista:
    print(i, end=' ')