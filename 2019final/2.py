a, b = map(int, input().split())
minl, maxl = abs(a - b), a + b
n = int(input())
print(len(list(filter(lambda x: minl < x < maxl, map(int, input().split())))))
