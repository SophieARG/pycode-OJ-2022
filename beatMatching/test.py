n = int(input())
wages = map(int, input().split())
num = 0
for wage in wages:
    if wage >= 30:
        num += 1
print(num)
