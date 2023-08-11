print('Digite três valores inteiros')
valor1 = int(input())
valor2 = int(input())
valor3 = int(input())

valores = [valor1, valor2, valor3]

print(f'A soma do maior com o menor número é {min(valores) + max(valores)}.')