def verificar(resultado, aposta):
    for _ in aposta:
        for i in resultado:
            if resultado not in aposta:
                return total_ganhadores + 0
        return total_ganhadores + 1

qtd_apostas = int(input())
lst_apostas = []
apostas = set()
total_ganhadores = 0

for i in range(qtd_apostas):
    lst_apostas = (int(x) for x in input().split(","))
    for i in lst_apostas:
        apostas.add(i)

lst_resultado = (int(x) for x in input().split())
resultado = set()
for i in lst_resultado:
    resultado.add(i)

for i in range(qtd_apostas):
    verificar(resultado, apostas)

print(total_ganhadores)