tamanho_Arrays = int(input())

itens1 = []
itens2 = []
index = 0

for _ in range (1, tamanho_Arrays +1):
    itens1 += input()

for _ in range (1, tamanho_Arrays +1):
    itens2 += input()

while index < tamanho_Arrays:
    print(itens1[index])
    print(itens2[index])
    index += 1