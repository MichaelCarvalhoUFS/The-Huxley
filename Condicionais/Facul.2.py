numero = int(input())

if numero > 0:
    unidade = numero % 10
if numero < 0:
    unidade = -((-numero) % 10)

print(unidade)