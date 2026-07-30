#chat me ensinou busca_binaria:
def procurar(lst_CPFs, lst_Notas, test):
    inicio = 0
    fim = len(lst_CPFs)-1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lst_CPFs[meio] == test:
                return lst_Notas[meio]
        elif lst_CPFs[meio] < test:
             inicio = meio + 1
        else:
             fim = meio - 1
    return "NAO SE APRESENTOU"

num_inscritos = int(input())
CPFs = []
notas = []

for i in range(num_inscritos):
    CPFs.append(int(input()))

for i in range(len(CPFs)):
    notas.append(int(input()))

qtd_testes = int(input())
test = 0

for _ in range(qtd_testes):
    test = int(input())
    print(procurar(CPFs, notas, test))