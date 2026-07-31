numero = int(input())
tabuada1 = numero * 1
tabuada2 = numero * 2
tabuada3 = numero * 3
tabuada4 = numero * 4
tabuada5 = numero * 5
tabuada6 = numero * 6
tabuada7 = numero * 7
tabuada8 = numero * 8
tabuada9 = numero * 9
print(numero, "X 1 =", tabuada1)
print(numero, "X 2 =", tabuada2)
print(numero, "X 3 =", tabuada3)
print(numero, "X 4 =", tabuada4)
print(numero, "X 5 =", tabuada5)
print(numero, "X 6 =", tabuada6)
print(numero, "X 7 =", tabuada7)
print(numero, "X 8 =", tabuada8)
print(numero, "X 9 =", tabuada9)

# Alex q fez
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Eu fiz (depois)
numero = int(input())
for n in range(1,11):
    print(f"{numero} X {n} = {numero*n}")