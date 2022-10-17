depositSum = float(input())
term = int(input())
percent = float(input())
increase = depositSum * percent/100
oneMounth = increase / 12
#sum = depositSum + term * ((depositSum * term) / 12)
sum = depositSum + term * oneMounth
print(sum)