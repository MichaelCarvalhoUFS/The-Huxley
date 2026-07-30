def promocao(valor):
    inteiro_valor = int(valor)
    for i in range(2, inteiro_valor-1):
        if inteiro_valor % i == 0:
            return valor
        else:
            return valor * 0.58
        
qtd_corridas = int(input())
for i in range(qtd_corridas):
    distancia, custo_km = input().split()
    distancia = float(distancia)
    custo_km = float(custo_km)
    valor_total = custo_km * distancia
    promocao(valor_total)