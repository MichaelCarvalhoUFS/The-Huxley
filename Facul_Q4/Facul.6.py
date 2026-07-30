num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

if num_1 == num_2 == num_3:
    print("1")

elif num_1 == num_2 != num_3 or num_2 == num_3 != num_1 or num_3 == num_1 != num_2:
    print("3")

else:
    print("2")