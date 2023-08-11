print('Digite uma sequência de números separados por vírgula:')
sequencia = list(map(int, input().split(',')))

print(f'Soma = {sum(sequencia)}')