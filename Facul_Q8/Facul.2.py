#gemini fez
entrada = input().split()
qtd_numeros = int(entrada[0])
numeros_ordenados = int(entrada[1])

vetor = [int(x) for x in input().split()]

for i in range(numeros_ordenados):
    indice_menor = i
    for j in range(i + 1, qtd_numeros):
        if vetor[j] < vetor[indice_menor]:
            indice_menor = j
    
    vetor[i], vetor[indice_menor] = vetor[indice_menor], vetor[i]
    
    print(vetor)