print('Digite uma frase:')
frase = input()
A = E = I = O = U = 0

for i in frase:
    if i == 'a' or 'A':
        A += 1
    if i == 'e' or i == 'E':
        E += 1
    if i == 'i' or i == 'I':
        I += 1
    if i == 'o' or i == 'O':
        O += 1
    if i == 'u' or i == 'U':
        U += 1

print(f'A - {A}')
print(f'E - {E}')
print(f'I - {I}')
print(f'O - {O}')
print(f'U - {U}')