#ChatGPT fez
tam_Matriz = int(input())

matriz_Quad = []

for _ in range(tam_Matriz):
    matriz_Quad.append([int(x) for x in input().split()])

# Guardar diagonal principal invertida
diag_invertida = []

for i in range(tam_Matriz - 1, -1, -1):
    diag_invertida.append(matriz_Quad[i][i])

# Recolocar diagonal invertida
for i in range(tam_Matriz):
    matriz_Quad[i][i] = diag_invertida[i]

# Multiplicar diagonal secundária por 2
for i in range(tam_Matriz):
    for j in range(tam_Matriz):
        if i + j == tam_Matriz - 1:
            matriz_Quad[i][j] *= 2

# Fazer transposta
for i in range(tam_Matriz):
    for j in range(i + 1, tam_Matriz):
        matriz_Quad[i][j], matriz_Quad[j][i] = (
            matriz_Quad[j][i],
            matriz_Quad[i][j]
        )

# Saída
for i in range(tam_Matriz):
    for j in range(tam_Matriz):
        if j > 0:
            print(" ", end="")
        print(matriz_Quad[i][j], end="")
    print()

"""tam_Matriz = int(input())
matriz_Quad = []
diag_invertida = []
diag_secund = []

for _ in range(tam_Matriz):
    matriz_Quad.append([int(x) for x in input().split()])

for i in range(len(matriz_Quad)-1, -1, -1):
    for j in range(len(matriz_Quad)-1, -1, -1):
        if j == i:
            diag_invertida.append(matriz_Quad[i][j])
        # elif j - i == -(i - j):
        #    diag_secund.append(matriz_Quad[i][j] * 2)
    matriz_Quad[i][j], matriz_Quad[j][i] = matriz_Quad[j][i], matriz_Quad[i][j]
print(diag_invertida)
print(diag_secund)
print(matriz_Quad)"""