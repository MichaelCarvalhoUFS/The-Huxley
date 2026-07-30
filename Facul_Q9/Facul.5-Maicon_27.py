numero_Sudoku = int(input())
todas_Marizes = []

for _ in range(0, numero_Sudoku-1):
    todas_Marizes.append([])
    for _ in range(9):
        todas_Marizes[i].append([int(x) for x in input().split()])
print(todas_Marizes)