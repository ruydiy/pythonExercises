nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())
sumNaylon = (nylon + 2) * 1.50
sumPaint = (paint + (paint * 0.1)) * 14.50
sumThinner = thinner * 5
sumMaterials = sumNaylon + sumThinner + sumPaint + 0.40
sumWorker = (sumMaterials * 0.3) * hours
print(sumWorker + sumMaterials)