notas = int(input())
valores = []

for _ in range(notas):
    valores += [int(input())]

media = sum(valores)/len(valores)
contador_Maior = 0
contador_Menor = 0

for i in valores:
    if i > (media*1.1):
        contador_Maior += 1
    elif i < (media*0.9):
        contador_Menor += 1

print(f"{media:.2f}")
print(contador_Maior)
print(contador_Menor)