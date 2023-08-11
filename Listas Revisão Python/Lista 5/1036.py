entrada = input().split()
a = float(entrada[ 0 ])
b = float(entrada[ 1 ])
c = float(entrada[ 2 ])
d = 'Impossivel calcular'

delta = (b **2 ) - 4 * a * c

if a == 0:
 print(d)

elif delta < 0:
 print(d)

else: 
 x1 = (-b + delta ** (1/2)) / (2 * a)
 x2 = (-b - delta ** (1/2)) / (2 * a)
 print(f'R1 = {x1:.5f}')
 print(f'R2 = {x2:.5f}')
