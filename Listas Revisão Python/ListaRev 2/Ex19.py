for i in range(1,11):
    indice = 0
    print(f'Tabuada de {i}')
    while indice < 10:
        indice += 1
        print(f'{i} x {indice} = {i * indice}')

        if indice == 10:
            print(f'{i} x {indice} = {i * indice}\n')