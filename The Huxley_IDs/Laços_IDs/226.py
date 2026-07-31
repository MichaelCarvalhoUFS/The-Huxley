numero = int(input())
numero1 = numero
soma = 0

while numero > 0:
    if numero1 != numero:
        if numero % 3 == 0 or numero % 5 == 0:
           soma += numero
    numero -= 1

print(soma)