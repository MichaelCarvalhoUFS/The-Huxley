Num_A = int(input())
Num_B = int(input())
Num_C = int(input())

if (Num_A and Num_B and Num_C) in (1,0):
    if Num_A == Num_B != Num_C:
        print("C")
    elif Num_C == Num_B != Num_A:
        print("A")
    elif Num_C == Num_A != Num_B:
        print("B")
    else:
        print("*")