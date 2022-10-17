length = int(input())
width = int(input())
high = int(input())
percent = float(input())
tank = length * width * high
tank/=1000
print(tank - (tank * (percent/100)))