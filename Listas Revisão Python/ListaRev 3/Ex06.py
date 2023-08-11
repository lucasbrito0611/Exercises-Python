def frete(massa, distancia):
    centavos = 1 * massa * distancia

    if centavos < 100:
        preco = centavos
        return (f'R$ 0,{preco}')
    
    else:
        reais = centavos // 100
        centavos = centavos - (reais * 100)
        preco = [reais, centavos]
        if centavos != 0:
            return (f'R$ {preco[0]},{preco[1]}')
        else:
            return (f'R$ {preco[0]},00')
    
print(frete(int(input()), int(input())))