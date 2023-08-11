def volumeesfera(r):
    volume = (4/3) * 3.14 * (r**3)

    return volume

print(f'{volumeesfera(int(input())):.0f}')