numero_M = int(input())
numero_I = int(input())
numero_S = int(input())

existir = "INEXISTENTE"

for i in range(numero_I, numero_S + 1):
    if i % numero_M == 0:
        print(i)
        existir = "existe"

if existir == "INEXISTENTE":
    print(existir)