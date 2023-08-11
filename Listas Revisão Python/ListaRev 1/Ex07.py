print('Digite os coeficientes a, b e c de uma equação do II grau')
a = int(input())
b = int(input())
c = int(input())

delta = (b **2 ) - 4 * a * c

x1 = (-b + delta ** (1/2)) / (2 * a)
x2 = (-b - delta ** (1/2)) / (2 * a)

if a < 0:
 print('impossível calcular')

if a == 0:
    print(f'A raíz é {x1:.0f}')

if a > 0:
    print(f'As raízes são {x1:.0f} e {x2:.0f}')