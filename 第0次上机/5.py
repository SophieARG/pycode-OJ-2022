n = int(input())
for i in range(n):
    dis = int(input())
    if dis > 100:
        print('Bike')
    elif dis < 100:
        print('Walk')
    else:
        print('All')
