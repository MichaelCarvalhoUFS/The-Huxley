def verificar_Sudo(matriz):
    for i in range(9):
        linha_sudo = set(range(1, 10))
        for j in range(9):
            if matriz[i][j] in linha_sudo:
                linha_sudo.discard(matriz[i][j])
            else:
                return "NAO"

    for i in range(9):
        coluna_sudo = set(range(1, 10))
        for j in range(9):
            if matriz[j][i] in coluna_sudo:
                coluna_sudo.discard(matriz[j][i])
            else:
                return "NAO"

    for I in range(0, 9, 3):
        for J in range(0, 9, 3):
            bloco_sudo = set(range(1, 10))
            for i in range(3):
                for j in range(3):
                    num = matriz[I + i][J + j]
                    if num in bloco_sudo:
                        bloco_sudo.discard(num)
                    else:
                        return "NAO" 

    return "SIM"

numero_Sudoku = int(input())

for i in range(1, numero_Sudoku + 1):
    matriz = []
    for _ in range(9):
        matriz.append([int(x) for x in input().split()])
    
    verificar = verificar_Sudo(matriz)
    print(f"Instancia {i}")
    print(verificar)
    print()