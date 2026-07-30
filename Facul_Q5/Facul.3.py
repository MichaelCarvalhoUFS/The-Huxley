#ChatGPT q fez

dias = 1
soma = 0
contador = 0

valor_Da = float(input())
soma += valor_Da

while dias < 7:
    valor = float(input())
    soma += valor

    dias += 1
    if valor >= valor_Da + 0.5:
        contador += 1
    valor_Da = valor
    
print(f"R$ {soma:.2f}")
print(contador)