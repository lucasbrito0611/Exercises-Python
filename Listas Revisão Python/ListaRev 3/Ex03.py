def diagonal(b,h):
    hipotenusa = ((b**2) + (h**2)) ** 0.5

    return hipotenusa

print(f'{diagonal(int(input()), int(input())):.0f}')