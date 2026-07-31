dimensoes = input().split()
n = int(dimensoes[0])
m = int(dimensoes[1])

maior_sequencia_global = 0

for i in range(n):
    linha = [int(x) for x in input().split()]
    
    maior_seq_linha = 1 if m > 0 else 0
    seq_atual = 1 if m > 0 else 0
    
    for j in range(1, m):
        if linha[j] >= linha[j-1]:
            seq_atual += 1
        else:
            if seq_atual > maior_seq_linha:
                maior_seq_linha = seq_atual
            seq_atual = 1
            
    if seq_atual > maior_seq_linha:
        maior_seq_linha = seq_atual
        
    print(f"Linha {i}: {maior_seq_linha}")
    
    if maior_seq_linha > maior_sequencia_global:
        maior_sequencia_global = maior_seq_linha

print(f"Maior Sequencia: {maior_sequencia_global}")