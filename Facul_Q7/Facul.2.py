numero_Limite = int(input())

stringNumeros = []
stringNumeros += input().split()
numeros = [int(x) for x in stringNumeros]
numeroMenor = numeros[0]
posicao = 0

for i in range(numero_Limite):
    if numeros[i] < numeroMenor:
        numeroMenor = numeros[i]
        posicao = i


print(f"Menor valor: {numeroMenor}")
print(f"Posicao: {posicao}")