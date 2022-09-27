n = int(input())
p1 = sum(map(int, input().split()))
p2 = sum(map(int, input().split()))
if p1 < 55:
    print(2)
else:
    if p1 - 20 < p2:
        print(1)
    elif p1 - 20 > p2:
        print(2)
    else:
        print(3)
