def mmc(x,y):
    maior = max(x,y)

    while True:
        if (maior % x == 0) and (maior % y == 0):
            return maior
        else:
            maior += 1

print(mmc(int(input()), int(input())))