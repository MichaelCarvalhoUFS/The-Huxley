quantidade_de_agua, custo_da_agua = input().split()

quantidade_de_agua = float(quantidade_de_agua)
custo_da_agua = float(custo_da_agua)

valor = (quantidade_de_agua*1000)*custo_da_agua
valor_esgoto = valor * 0.8
valor_total = valor + valor_esgoto

print(f"{valor:.2f}")
print(f"{valor_esgoto:.2f}")
print(f"{valor_total:.2f}")