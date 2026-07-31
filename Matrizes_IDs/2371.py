local = input()
valor_limiaar = int(input())
ordem_M = int(input())
elementos = []
soma = 0
verificacao = "False"

for _ in range(ordem_M):
    elementos.append([int(x) for x in input().split()])

for i in range(ordem_M):
    for j in range(ordem_M):
        if j > i and local == "acima":
            soma += elementos[i][j]
        elif j < i and local == "abaixo":
            soma += elementos[i][j]

if soma > valor_limiaar:
    verificacao = "True"

print(verificacao)