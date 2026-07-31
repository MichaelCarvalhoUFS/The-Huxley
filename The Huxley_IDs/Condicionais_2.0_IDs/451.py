valor = float(input())
anos_de_garantia = int(input())

valor_pagar = valor

if anos_de_garantia != 0:
    if anos_de_garantia == 1 :
        valor_pagar = valor * 1.03
    elif anos_de_garantia == 2:
        valor_pagar = valor * 1.05

print(f"{valor_pagar:.2f}")