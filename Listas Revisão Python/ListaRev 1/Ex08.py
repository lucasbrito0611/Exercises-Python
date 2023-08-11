print('Digite quatro valores inteiros')
valor1 = int(input())
valor2 = int(input())
valor3 = int(input())
valor4 = int(input())

valores = [valor1, valor2, valor3, valor4]

valores_crescente = sorted(valores)

print(f'Maior valor = {valores_crescente[3]}')
print(f'Menor valor = {valores_crescente[0]}')
print(f'A soma do segundo maior valor com o segundo menor = {valores_crescente[1] + valores_crescente[2]}')