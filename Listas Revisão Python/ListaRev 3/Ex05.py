def volumelitros(h,l,p):
    volume = h * l * p

    return volume

print(f'{volumelitros(int(input()), int(input()), int(input()))} litros')