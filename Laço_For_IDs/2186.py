qtd_testes = int(input())

for _ in range(1, qtd_testes+1):
    vogaisA = input()
    frase = input()
    contador = 0
    
    for i in frase:
        if i in vogaisA:
            contador += 1
    print(contador)