a, b, c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)

pi = 3.14159

atr = a * c /2
ac = pi * c**2
at = ((a + b) * c) / 2
aq = b**2
ar = a * b

print(f'TRIANGULO: {atr:.3f}')
print(f'CIRCULO: {ac:.3f}')
print(f'TRAPEZIO: {at:.3f}')
print(f'QUADRADO: {aq:.3f}')
print(f'RETANGULO: {ar:.3f}')
