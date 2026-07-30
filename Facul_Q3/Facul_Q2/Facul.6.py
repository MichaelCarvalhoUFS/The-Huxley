Valor_altura = float(input())
Valor_raio = float(input())

pi = 3.14
Volume_Cilindro = (pi*Valor_raio**2)*Valor_altura
Area_Cilindro = 2*pi*Valor_raio*(Valor_raio + Valor_altura)

print(f"{Volume_Cilindro:.2f}")
print(f"{Area_Cilindro:.2f}")