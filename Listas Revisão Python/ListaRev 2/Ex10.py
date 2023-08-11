print('Digite uma frase:')
frase = input()

for i in range(1,len(frase) + 1):
    nova_frase = frase[i:] + frase[0:i]
    print(nova_frase)