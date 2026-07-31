def fat(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return fat(numero-1) * numero

numero = int(input())
while numero != -1:
    print(fat(numero))
    numero = int(input())