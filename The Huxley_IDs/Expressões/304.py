valor = int(input())

nota_100 = "100,00"
nota_50 = "50,00"
nota_20 = "20,00"
nota_10 = "10,00"
nota_5 = "5,00"
nota_2 = "2,00"
nota_1 = "1,00"

Nota_100 = valor//100
Nota_50 = (valor%100)//50
Nota_20 = ((valor%100)%50)//20
Nota_10 = (((valor%100)%50)%20)//10
Nota_5 = ((((valor%100)%50)%20)%10)//5
Nota_2 = (((((valor%100)%50)%20)%10)%5)//2
Nota_1 = ((((((valor%100)%50)%20)%10)%5)%2)//1

print(valor)
print(f"{Nota_100} nota(s) de R$ {nota_100}")
print(f"{Nota_50} nota(s) de R$ {nota_50}")
print(f"{Nota_20} nota(s) de R$ {nota_20}")
print(f"{Nota_10} nota(s) de R$ {nota_10}")
print(f"{Nota_5} nota(s) de R$ {nota_5}")
print(f"{Nota_2} nota(s) de R$ {nota_2}")
print(f"{Nota_1} nota(s) de R$ {nota_1}")