def verificar_ganhador(resultado, aposta):
    for numero in resultado:
        if numero not in aposta:
            return 0
    return 1

qtd_apostas = int(input())

lista_de_apostas = []

for i in range(qtd_apostas):
    linha = input().split(",")

    aposta_atual = set()

    for x in linha:
        aposta_atual.add(int(x))

    lista_de_apostas.append(aposta_atual)

linha_resultado = input().split()
resultado_oficial = []
for x in linha_resultado:
    resultado_oficial.append(int(x))

total_ganhadores = 0

for aposta in lista_de_apostas:
    total_ganhadores += verificar_ganhador(resultado_oficial, aposta)

print(f"Total de ganhadores: {total_ganhadores}")