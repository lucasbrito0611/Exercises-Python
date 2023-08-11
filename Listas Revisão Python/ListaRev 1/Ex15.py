print('Digite três valores:')
valor1 = int(input())
valor2 = int(input())
valor3 = int(input())

valores = [valor1, valor2, valor3]
valores.sort()

for i in valores:
    print(i)