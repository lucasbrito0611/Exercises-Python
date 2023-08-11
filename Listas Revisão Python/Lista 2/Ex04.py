print('Digite a base e a altura do retângulo:')
base = int(input())
altura = int(input())

area = base * altura
perimetro = (base * 2) + (altura * 2)
diagonal = ((base ** 2) + (altura ** 2)) ** 0.5

print(f'Área = {area:.2f} - Perimetro = {perimetro:.2f} - Diagonal = {diagonal:.2f}')
