genero_Homem = int(input())
idade_Maior_de_40 = int(input())

desconto = 0

if genero_Homem == 0:
    desconto += 1

if idade_Maior_de_40 == 1:
    desconto += 1

if desconto == 2:
    print(1)
else:
    print(0)
