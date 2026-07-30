diametro = int(input())
altura, largura, profundida = input().split()

altura = int(altura)
largura = int(largura)
profundida = int(profundida)

if diametro > altura or diametro > largura or diametro > profundida:
    print("N")
else:
    print("S")