numero_Loop = int(input())
serie_Numeros = input().split()

for i in range(numero_Loop):
    serie_Numeros[i] = int(serie_Numeros[i])

for i in range(numero_Loop-1, -1, -1):
    if i != 0:
        print(serie_Numeros[i], end=" ")
    else:
        print(serie_Numeros[i])

for i in range(1, numero_Loop):
    print(serie_Numeros[i], end=" ")
print(serie_Numeros[0])
 
serie_Numeros.sort()
for i in range(numero_Loop-1, -1, -1):
    print(serie_Numeros[i], end=" ")