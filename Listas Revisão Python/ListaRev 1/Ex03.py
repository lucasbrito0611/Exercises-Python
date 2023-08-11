print('Digite quatro valores inteiros')
valor1 = int(input())
valor2 = int(input())
valor3 = int(input())
valor4 = int(input())

valores = [valor1, valor2, valor3, valor4]
pares = []
impares = []

for i in valores:
    if i % 2 == 0:
        pares.append(i)

    if i % 2 != 0:
        impares.append(i)

print(f'Soma dos pares = {sum(pares)}')
print(f'Soma dos ímpares = {sum(impares)}')