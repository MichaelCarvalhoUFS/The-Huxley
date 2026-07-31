def ContaDigitosPares(numero):
    if numero == 0:
        return 0
    if (numero % 10) % 2 == 0:
        return 1 + (ContaDigitosPares(numero // 10))
    else:
        return 0
    
numero = int(input())
print(ContaDigitosPares(numero))