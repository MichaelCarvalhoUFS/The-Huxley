numero_leituras = int(input())

soma = 0

for i in range(1, numero_leituras + 1):
    numero = int(input())
    soma += numero
print(soma)