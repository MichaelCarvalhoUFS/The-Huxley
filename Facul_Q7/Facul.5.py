numeros = [int(x) for x in input().split()]

padrao = numeros[-1]
contador_Padrao = 0

for i in numeros:
    if i == padrao:
        contador_Padrao += 1

print(f"O numero {padrao} apareceu {contador_Padrao} vezes")