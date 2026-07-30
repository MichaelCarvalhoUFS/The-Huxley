#Gemini Fez
def verificar_Sudo(matriz):
    # 1. Verificar Linhas
    for i in range(9):
        linha_sudo = set(range(1, 10))
        for j in range(9):
            if matriz[i][j] in linha_sudo:
                linha_sudo.discard(matriz[i][j])
            else:
                return "NAO"

    # 2. Verificar Colunas
    for i in range(9):
        coluna_sudo = set(range(1, 10))
        for j in range(9):
            if matriz[j][i] in coluna_sudo:
                coluna_sudo.discard(matriz[j][i])
            else:
                return "NAO"

    # 3. Verificar Blocos 3x3
    # Os loops externos (I, J) andam de 3 em 3 para achar o início de cada bloco
    for I in range(0, 9, 3):
        for J in range(0, 9, 3):
            bloco_sudo = set(range(1, 10))
            # Os loops internos (i, j) percorrem as 3 linhas e 3 colunas daquele bloco
            for i in range(3):
                for j in range(3):
                    num = matriz[I + i][J + j]
                    if num in bloco_sudo:
                        bloco_sudo.discard(num)
                    else:
                        return "NAO" 

    return "SIM"

# Leitura do número de instâncias
numero_Sudoku = int(input())

for i in range(1, numero_Sudoku + 1):
    matriz = []
    # Lê as 9 linhas do Sudoku atual
    for _ in range(9):
        matriz.append([int(x) for x in input().split()])
    
    # Valida e imprime o resultado
    verificar = verificar_Sudo(matriz)
    print(f"Instancia {i}")
    print(verificar)
    print()  # Linha em branco exigida pelo problema entre as instâncias

"""def adicionar_Sudoku(matriz):
    for _ in range(0, 9):
        matriz.append([int(x) for x in input().split()])
    return verificar_Sudo(matriz)

def verificar_Sudo(matriz):
    verificao = ""
    for i in range(0, 9):
        linha_sudo = set(int(x) for x in range(1, 10))
        for j in range(0, 9):
            if matriz[i][j] in linha_sudo:
                verificao = "SIM"
                linha_sudo.discard(matriz[i][j])
            else:
                verificao = "NAO"
                return verificao

    for i in range(0, 9):
        linha_sudo = set(int(x) for x in range(1, 10))
        for j in range(0, 9):
            if matriz[j][i] in linha_sudo:
                verificao = "SIM"
                linha_sudo.discard(matriz[j][i])
            else:
                verificao = "NAO"
                return verificao
    return verificao

numero_Sudoku = int(input())
todas_Matrizes = []

for i in range(1, numero_Sudoku + 1):
    if i < numero_Sudoku + 1:
        verificar = adicionar_Sudoku(todas_Matrizes)
        print(f"Instancia {i} ")
        print(f"{verificar}")
        print()
    
    else:
        verificar = adicionar_Sudoku(todas_Matrizes)
        print(f"Instancia {i} ")
        print(f"{verificar}"""