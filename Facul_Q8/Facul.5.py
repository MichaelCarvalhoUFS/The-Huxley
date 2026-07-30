#Ajuda do Gemini

def imprimir(lst):
    for i in lst:
        print(i)

def ordenacao(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

lista_marilda = []
linha_divisoria = "-" * 50
nome_I = input()

while nome_I != "FIM":
    lista_marilda.append(nome_I)
    nome_I = input()

ordenacao(lista_marilda)
imprimir(lista_marilda)

n = int(input())

while n != 0:
    print(linha_divisoria)
    
    for _ in range(n):
        lista_marilda.append(input())
    
    ordenacao(lista_marilda)
    imprimir(lista_marilda)
    
    n = int(input())