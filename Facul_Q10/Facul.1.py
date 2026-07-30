# Gemini fez
def verificar_ganhador(resultado, aposta):
    # Passa por cada número do resultado oficial
    for numero in resultado:
        # Se algum número do resultado NÃO estiver na aposta, não é ganhador
        if numero not in aposta:
            return 0
    # Se o loop terminar sem falhar em nenhum número, a aposta acertou os 6
    return 1


# 1. Lê a quantidade de apostas
qtd_apostas = int(input())

lista_de_apostas = []

# 2. Loop para ler cada aposta
for i in range(qtd_apostas):
    linha = input().split(",")

    # Criamos um conjunto vazio para a aposta atual
    aposta_atual = set()

    # Convertendo cada texto em número e adicionando no conjunto (substituindo o map)
    for x in linha:
        aposta_atual.add(int(x))

    # Guarda essa aposta na lista de apostas
    lista_de_apostas.append(aposta_atual)

# 3. Lê o resultado oficial e converte para uma lista de inteiros
linha_resultado = input().split()
resultado_oficial = []
for x in linha_resultado:  # Correção para a variável correta: linha_resultado
    resultado_oficial.append(int(x))

total_ganhadores = 0

# 4. Verifica cada aposta individualmente
for aposta in lista_de_apostas:
    total_ganhadores += verificar_ganhador(resultado_oficial, aposta)

# 5. Imprime o resultado final
print(f"Total de ganhadores: {total_ganhadores}")

"""def verificar(resultado, aposta):
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
    print(apostas)
resultado = (int(x) for x in input().split())

for i in range(qtd_apostas):
    verificar(resultado, apostas)

print(total_ganhadores)"""