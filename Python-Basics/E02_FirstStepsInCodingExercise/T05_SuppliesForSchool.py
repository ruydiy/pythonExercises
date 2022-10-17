numPens = int(input())
numMarkers = int(input())
literDettrigin = int(input())
percentDiscount = int(input())
sum = numPens * 5.80 + numMarkers * 7.20 + literDettrigin * 1.20
print(sum - (sum * (percentDiscount / 100)))