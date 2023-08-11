print('Digite quatro valores inteiros')
valor1 = int(input())
valor2 = int(input())
valor3 = int(input())
valor4 = int(input())

valores = [valor1, valor2, valor3, valor4]
menores = []
maiores = []

media = (valor1 + valor2 + valor3 + valor4) / 4

for i in valores:
    if i < media:
        menores.append(i)

    else:
        maiores.append(i)

print(f'Media = {media:.0f}')

print('Números menores que a média')
for x in menores:
    print(x)

print('Números maiores ou iguais à média')
for x in maiores:
    print(x)