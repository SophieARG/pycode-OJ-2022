n = int(input())
print(len(list(filter(lambda x: x >= 30, map(int, input().split())))))
