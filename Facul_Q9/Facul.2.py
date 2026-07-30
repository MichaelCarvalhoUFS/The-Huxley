#Gemini q fez
def estrada(numero, matriz):
    i = 0
    j = 0

    if matriz[0][0] == 0 or matriz[numero-1][numero-1] == 0:
        return "NOT OK"

    while i != numero-1 or j != numero-1:
        matriz[i][j] = 0

        if i + 1 < numero and matriz[i+1][j] == 1:
            i += 1
        elif j + 1 < numero and matriz[i][j+1] == 1:
            j += 1
        elif i - 1 >= 0 and matriz[i-1][j] == 1:
            i -= 1
        elif j - 1 >= 0 and matriz[i][j-1] == 1:
            j -= 1
        else:
            return "NOT OK"
    return "OK"

linha_n = input()
if linha_n:
    n = int(linha_n)
    matriz_principal = []

    for _ in range(n):
        dados_linha = input().split()
        linha_int = []
        for valor in dados_linha:
            linha_int.append(int(valor))
        matriz_principal.append(linha_int)

    print(estrada(n, matriz_principal))

#Fiz e deu erro
"""def estrada(numero ,matriz):
    verificaco = "OK"
    i = 0
    j = 0

    if matriz[0][0] == 0 or matriz[numero-1][numero-1] == 0:
        return "NOT OK"

    while i != numero-1 or j != numero-1:
            matriz[i][j] = 0

            if i != numero -1 and 1 == matriz[i+1][j]:
                i += 1
                if matriz[i][j] == matriz[i][j-1] and j > 0:
                    j -= 1
            elif j != numero -1 and 1 == matriz[i][j+1]:
                j += 1
                if matriz[i][j] == matriz[i-1][j] and i > 0:
                    i -= 1
            else:
                return "NOT OK"
    return "OK"

numero = int(input())
matriz = []

for _ in range(numero):
    matriz.append([int(x) for x in input().split()])

print(estrada(numero, matriz))"""