lado_1 = float(input())
lado_2 = float(input())
lado_3 = float(input())

if lado_1 == lado_2 == lado_3:
    print("equilatero")
elif lado_1 == lado_2 != lado_3 or lado_2 == lado_3 != lado_1 or lado_1 == lado_3 != lado_2:
    print("isosceles")
else:
    print("escaleno")