#Gemini fez
dimensoes = input().split()
N = int(dimensoes[0])
M = int(dimensoes[1])
O = int(dimensoes[2])

# 2. Leitura da Matriz A (N linhas x M colunas)
A = []
for i in range(N):
    linha = [int(x) for x in input().split()]
    A.append(linha)

# 3. Leitura da Matriz B (M linhas x O colunas)
B = []
for i in range(M):
    linha = [int(x) for x in input().split()]
    B.append(linha)

# 4. Inicialização da Matriz C com zeros (N linhas x O colunas)
C = []
for i in range(N):
    C.append([0] * O)

# 5. Processamento da Multiplicação (Lógica das Imagens)
for i in range(N):          # Percorre as linhas de A
    for j in range(O):      # Percorre as colunas de B
        soma = 0
        for k in range(M):  # Percorre os elementos correspondentes (coluna de A / linha de B)
            soma += A[i][k] * B[k][j]
        C[i][j] = soma

# 6. Impressão do Resultado no formato correto
for i in range(N):
    # Converte cada número para string e junta com um espaço
    print(" ".join(str(x) for x in C[i]))