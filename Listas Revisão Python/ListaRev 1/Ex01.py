print('Digite dois valores inteiros')
valor1 = int(input())
valor2 = int(input())

valores = [valor1, valor2]

if valor1 == valor2:
    print('Números iguais')

else:
    print(f'Maior = {max(valores)}')