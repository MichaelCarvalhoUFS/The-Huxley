valor1 = float(input())
valor2 = float(input())
valor3 = float(input())

quantidade = 0
media = (valor1+valor2+valor3)/3
if valor1 > media:
    quantidade += 1
if valor2 > media:
        quantidade += 1
if valor3 >media:
      quantidade += 1

print(quantidade)