def imprime_linhas(n):
    for i in range(1, n + 1):
        linha = str(i)
        
        for j in range(i - 1):
            linha += "-" + str(i)
        
        print(linha)

numero = int(input())
imprime_linhas(numero)