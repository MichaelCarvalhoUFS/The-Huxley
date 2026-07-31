Salario = float(input())
Aumento = float(input())

Salario_Reajustado = Salario*(1+(Aumento/100))

print(f"Seu salario teve aumento de {Aumento} %, passando de R$ {Salario: .2f} para R$ {Salario_Reajustado: .2f}")