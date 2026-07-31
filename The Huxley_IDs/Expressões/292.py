valor_A, valor_B, valor_C = input().split()

valor_A = float(valor_A)
valor_B = float(valor_B)
valor_C = float(valor_C)
pi = 3.14159

Area_triangulo = (valor_A * valor_C)/2
Area_circulo = pi*valor_C**2
Area_trapezio = ((valor_A + valor_B)*valor_C)/2
Area_quadrado = valor_B**2
Area_retangulo = valor_A*valor_B

print(f"TRIANGULO: {Area_triangulo:.3f}")
print(f"CIRCULO: {Area_circulo:.3f}")
print(f"TRAPEZIO: {Area_trapezio:.3f}")
print(f"QUADRADO: {Area_quadrado:.3f}")
print(f"RETANGULO: {Area_retangulo:.3f}")