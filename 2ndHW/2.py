n = int(input())
for i in range(n):
    char = input().lower()
    print(*map(lambda x: x.lower().count(char), input().split()))
