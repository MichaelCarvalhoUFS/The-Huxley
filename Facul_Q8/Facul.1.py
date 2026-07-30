numero_X = int(input())
numeros = []

for _ in range(numero_X):
    numeros += [int(input())]

#numeros.sort()

for _ in range(len(numeros)-1):
    for i in range(len(numeros)-1):
        if numeros[i] > numeros[i+1]:
            numeros[i], numeros[i+1] = numeros[i+1], numeros[i]

for i in range(len(numeros)):
    print(f"[{numeros[i]}]", end = "")