numero1, numero2 = input().split()
numero1, numero2 = int(numero1), int(numero2)

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

for i in range(1, numero2 + 1):
    if i % numero1 == 0:
        print(i)
    else:
        print(i, end=" ")