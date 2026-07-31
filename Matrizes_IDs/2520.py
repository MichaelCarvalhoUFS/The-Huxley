tam_Matriz = int(input())

matriz_Quad = []

for _ in range(tam_Matriz):
    matriz_Quad.append([int(x) for x in input().split()])

diag_invertida = []

for i in range(tam_Matriz - 1, -1, -1):
    diag_invertida.append(matriz_Quad[i][i])

for i in range(tam_Matriz):
    matriz_Quad[i][i] = diag_invertida[i]

for i in range(tam_Matriz):
    for j in range(tam_Matriz):
        if i + j == tam_Matriz - 1:
            matriz_Quad[i][j] *= 2

for i in range(tam_Matriz):
    for j in range(i + 1, tam_Matriz):
        matriz_Quad[i][j], matriz_Quad[j][i] = (
            matriz_Quad[j][i],
            matriz_Quad[i][j]
        )

for i in range(tam_Matriz):
    for j in range(tam_Matriz):
        if j > 0:
            print(" ", end="")
        print(matriz_Quad[i][j], end="")
    print()