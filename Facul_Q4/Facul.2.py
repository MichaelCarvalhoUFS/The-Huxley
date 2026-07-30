#OBS: o "elif" já funciona como delimitante:
#Uma vez que, o codigo testará primeiro a primeira condição "if" e se n pertencer ele impõe q o limite inferior é o valor da condicional anterior.
kwh = int(input())

taxa = 0
valor_minimo = 35.00

if kwh <= 99:
    taxa = 1.35
    valor_a_pagar = (kwh*taxa)

elif 299 >= kwh >= 100:
    taxa = 1.55
    valor_a_pagar = (kwh*taxa)

elif 574 >= kwh >= 300:
    taxa = 1.75
    valor_a_pagar = (kwh*taxa)

elif kwh >= 575:
    taxa = 2.15
    valor_a_pagar = (kwh*taxa)

if kwh > 300:
    valor_a_pagar = (valor_a_pagar*1.10)

if valor_a_pagar < valor_minimo:
    valor_a_pagar = valor_minimo

print(f"{valor_a_pagar:.2f}")
print(f"{taxa:.2f}")