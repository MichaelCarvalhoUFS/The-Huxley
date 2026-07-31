dimensoes = input().split()
N = int(dimensoes[0])
M = int(dimensoes[1])
O = int(dimensoes[2])
A = []

for i in range(N):
    linha = [int(x) for x in input().split()]
    A.append(linha)

B = []
for i in range(M):
    linha = [int(x) for x in input().split()]
    B.append(linha)

C = []
for i in range(N):
    C.append([0] * O)

for i in range(N):
    for j in range(O):
        soma = 0
        for k in range(M):
            soma += A[i][k] * B[k][j]
        C[i][j] = soma

for i in range(N):
    print(" ".join(str(x) for x in C[i]))