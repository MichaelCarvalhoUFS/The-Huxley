num1 = int(input())
num2 = int(input())

soma = 0

if num1 > num2:
    num1, num2 = num2, num1
    
if num1 <= 0:
    num1 = 0

while num1 <= num2:
    soma += num1
    num1 += 1
 
print(soma)