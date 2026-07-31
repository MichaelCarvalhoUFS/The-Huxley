def ordenacao_verificacao(lst):
    for i in range(len(lst)):
        if lst[i] < 0:
            return "Ordenacao cancelada."

    if lst[0] % 2 == 0:
        for j in range(len(lst)):
            for i in range(0, len(lst)-1):
                if lst[i] < lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
    else:
        for j in range(len(lst)):
            for i in range(0, len(lst)-1):
                if lst[i] > lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst


numeros = []
for i in range(3):
    numeros.append(int(input()))
numeros = ordenacao_verificacao(numeros)

if numeros == "Ordenacao cancelada.":
    print(numeros)
else:
    for i in numeros:
        print(i)