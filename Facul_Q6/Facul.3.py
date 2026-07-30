Capital_I, taxa_T, anos = input().split()
Capital_I, taxa_T, anos = float(Capital_I), float(taxa_T), int(anos)

trimestres = anos * 4
montante = Capital_I

for _ in range(1, trimestres + 1):
    Rendimento = montante * taxa_T
    montante += Rendimento
    print(f"Rendimento: {Rendimento:.2f} Montante: {montante:.2f}")