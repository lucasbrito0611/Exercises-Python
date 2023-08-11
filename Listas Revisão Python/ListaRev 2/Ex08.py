print('Digite uma frase')
nome = input()
palavras = nome.split()
resultado = ''
for palavra in palavras:
    resultado += palavra[-1]

print(resultado)