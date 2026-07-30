Tempo = int(input())

horas = Tempo//3600
resto = Tempo % 3600
minutos = resto // 60
segundos = resto % 60

horas = Tempo//3600
minutos = (Tempo % 3600) // 60
segundos = Tempo % 60

print(f"{horas}:{minutos}:{segundos}")