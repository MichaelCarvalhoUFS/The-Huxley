tipo_media = str(input())
variavel_A = int(input())
variavel_b = int(input())
variavel_c = int(input())

if tipo_media == "A":
    media_aritmetica = (variavel_A + variavel_b +variavel_c) / 3
    print(f"{media_aritmetica:.3f}")
elif tipo_media == "H":
    media_harmonica = 3 / (1/variavel_A + 1/variavel_b + 1/variavel_c)
    print(f"{media_harmonica:.3f}")
elif tipo_media == "G":
    media_geometrica = (variavel_A*variavel_b*variavel_c) ** (1/3)
    print(f"{media_geometrica:.3f}")