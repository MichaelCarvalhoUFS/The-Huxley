numero1 = int(input())
numero2 = int(input())

if numero2 < numero1:
    numero1, numero2 = numero2, numero1

while numero1 <= numero2:
    if not numero1 % 2 == 0:
        print(numero1)
    numero1 += 1