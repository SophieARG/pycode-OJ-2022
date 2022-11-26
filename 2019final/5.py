from functools import reduce
n = int(input())
print(reduce(lambda x, y: abs(x - y), map(int, input().split())))
