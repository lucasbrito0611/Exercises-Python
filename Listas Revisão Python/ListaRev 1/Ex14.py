print('Digite três valores:')
valor1 = int(input())
valor2 = int(input())
valor3 = int(input())

valores = [valor1, valor2, valor3]
valores_crescentes = sorted(valores)

if valores_crescentes[2] >= (valores_crescentes[0] + valores_crescentes[1]):
    print('Esses valores não formam um triângulo')

else:
    if valor1 == valor2 == valor3:
        print('Triângulo equilátero')

    elif valor1 != valor2 != valor3:
        print('Triângulo escaleno')

    else:
        print('Triângulo isósceles')