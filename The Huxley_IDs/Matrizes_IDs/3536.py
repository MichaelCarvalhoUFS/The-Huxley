
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