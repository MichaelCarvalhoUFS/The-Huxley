dias = int(input())
km = int(input())

valor_por_diaria = dias*90
valor_por_km = 0

if (km/dias) > 100:
    excedente = km - (dias*100)
    valor_por_km += excedente*12

valor_total = valor_por_diaria + valor_por_km
print(f"{valor_total:.2f}")