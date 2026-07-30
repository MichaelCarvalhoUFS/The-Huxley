qtd_numeros, numeros_ord = [int(x) for x in input().split()]
lst = [int(x) for x in  input().split()]
for _ in range(numeros_ord):
    for i in range(0, len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
    print(lst)