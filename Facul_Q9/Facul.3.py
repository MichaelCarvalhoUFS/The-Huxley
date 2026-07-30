#Gemini q fez
def montar_matriz(matriz, linhas):
    for i in range(linhas):
        matriz.append([int(x) for x in input().split()])

# Criamos uma função para verificar se a matriz_2 bate perfeitamente 
# com o pedaço da matriz_1 a partir da posição (linha_inicio, coluna_inicio)
def verificar_submatriz(matriz_grande, matriz_pequena, linha_inicio, coluna_inicio, linhas_M2, colunas_M2):
    for i in range(linhas_M2):
        for j in range(colunas_M2):
            # Se qualquer pixel não bater, este pedaço não serve
            if matriz_grande[linha_inicio + i][coluna_inicio + j] != matriz_pequena[i][j]:
                return False
    return True


linhas_M1, colunas_M1 = [int(x) for x in input().split()]
matriz_1 = []
montar_matriz(matriz_1, linhas_M1)

linhas_M2, colunas_M2 = [int(x) for x in input().split()]
matriz_2 = []
montar_matriz(matriz_2, linhas_M2)

contador = 0

for i in range(linhas_M1 - linhas_M2 + 1):
    for j in range(colunas_M1 - colunas_M2 + 1):
        if verificar_submatriz(matriz_1, matriz_2, i, j, linhas_M2, colunas_M2):
            contador += 1

print(contador)

"""def montar_matriz(matriz, linhas):
    for i in range(linhas):
        matriz.append([str(x) for x in input().split()])

def concatenar(matriz, linhas, colunas):
    for i in range(linhas-1):
        for j in range(colunas-1):
            matriz[i][j] = [matriz[i][j] + matriz[i][j+1]]


linhas_M1, colunas_M1 = [int(x) for x in input(). split()]
matriz_1 = []
matriz_2 = []
contador = 0

montar_matriz(matriz_1, linhas_M1)
concatenar(matriz_1, linhas_M1, colunas_M1)
linhas_M2, colunas_M2 = [int(x) for x in input(). split()]

montar_matriz(matriz_2, linhas_M2)
concatenar(matriz_2, linhas_M2, colunas_M2)

for i in range(linhas_M1):
    for j in range(colunas_M1):
        if matriz_2 == matriz_1[i][j]:
            contador += 1

print(contador)"""