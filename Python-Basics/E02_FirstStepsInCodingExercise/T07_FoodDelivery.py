chikenMenu = int(input())
fishMenu = int(input())
vegMenu = int(input())
sum = chikenMenu * 10.35 + fishMenu * 12.40 + vegMenu * 8.15
sumDessert = sum * 0.2
total = (sum + sumDessert) + 2.50
print(total)