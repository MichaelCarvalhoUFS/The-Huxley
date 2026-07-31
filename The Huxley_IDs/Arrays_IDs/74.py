numeros = []

for _ in range(100):
    numeros += [input()]

padrao = input()

for i in range(100):
    if numeros[i] == padrao:
        print(i)