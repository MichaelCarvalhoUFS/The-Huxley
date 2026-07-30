notas = [int(x) for x in input().split()]

maior = notas[0]

for i in notas:
    if i > maior:
        maior = i
        
print(maior)