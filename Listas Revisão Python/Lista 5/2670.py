andar1 = int(input())
andar2 = int(input())
andar3 = int(input())

minutos_1 = (andar2 * 2) + (andar3 * 4) 
minutos_2 = (andar1 * 2) + (andar3 * 2) 
minutos_3 = (andar2 * 2) + (andar1 * 4) 

minutos = [minutos_1, minutos_2, minutos_3]

print(min(minutos))
