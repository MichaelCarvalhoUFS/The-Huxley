quantidade_de_khw = float(input())
kwh = 1.50
valor_a_pagar = quantidade_de_khw * kwh
valor_a_pagar_com_desconto = valor_a_pagar - (valor_a_pagar * 0.15)

print(f"Valor a ser pago: R$ {valor_a_pagar:.2f} reais")
print(f"Valor a ser pago com desconto: R$ {valor_a_pagar_com_desconto:.2f} reais")