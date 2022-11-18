for _ in range(int(input())):
    maxm = 60
    for num in map(int, input().split()[1:]):
        maxm -= 3
        if num >= maxm:
            print(min(num, maxm + 3))
            break
    else:
        print(maxm)
