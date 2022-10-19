order = input()
quantity = int(input())
result = lambda a, b: a * b
if(order == 'coffee'):
    order = 1.50
    print(result(order, quantity))
if(order == 'water'):
    order = 1.00
    print(result(order, quantity))
if(order == 'coke'):
    order = 1.40
    print(result(order, quantity))
if(order == 'snacks'):
    order = 2.00
    print(result(order, quantity))