set1 = set()
set2 = set()

for i in range(40):
    numeros = int(input())
    if i < 20:
        set1.add(numeros)
    else:
        set2.add(numeros)

conjunto_final = sorted(set1 & set2)

if conjunto_final == []:
    print("VAZIO")
else:
    for i in range(len(conjunto_final)):
        print(conjunto_final[i])