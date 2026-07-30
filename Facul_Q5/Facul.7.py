numero1 = int(input())
numero2 = int(input())

multiplo = 1
maior_multiplo = numero1

if numero1 <= numero2:
    while numero1 <= numero2 and multiplo * numero1 <= numero2:
            maior_multiplo = numero1 * multiplo
            multiplo += 1
    print(maior_multiplo)

else:
    print(f"sem multiplos menores que {numero2}")